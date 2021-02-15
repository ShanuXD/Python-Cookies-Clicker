from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import time


chrome_driver_path = r"C:\Users\LENOVO\Devlopment\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Cookie
cookie = driver.find_element_by_id("cookie")
# Right panel all id
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time() + 5
five_min = time() + 60*5

while True:
    cookie.click()

    if time() > timeout:

        # Get all upgrade price,<b>
        all_upgrade_price = driver.find_elements_by_css_selector("#store b")
        items_price = []

        # Convert price into int
        for price in all_upgrade_price:
            if price.text != "":
                amount = price.text.split("-")[1].strip().replace(",", "")
                items_price.append(int(amount))

        # Cookie dict, 100 : buyGrandma
        cookie_upgrades = {}
        for i in range(len(items_price)):
            cookie_upgrades[items_price[i]] = item_ids[i]

        # Current count
        money_count = driver.find_element_by_id("money").text

        if "," in money_count:
            money_count = money_count.replace(",", "")
        cookie_count = int(money_count)

        # Find upgrade that are possible
        possible_upgrades = {}
        for price_key in cookie_upgrades:
            if cookie_count > price_key:
                possible_upgrades[price_key] = cookie_upgrades[price_key]

        # Upgrade expensive item
        max_price_possible = max(possible_upgrades)
        purchase_id = possible_upgrades[max_price_possible]
        driver.find_element_by_id(purchase_id).click()

        # Add another 5mins until next check
        timeout = time()+5

    if time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break














