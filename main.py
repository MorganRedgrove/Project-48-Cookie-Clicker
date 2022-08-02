from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time


def num_value(item):
    text = item.text
    list = re.split("- |\n", text)
    num = list[1]
    num_clean = num.replace(",", "")
    return int(num_clean)


def upgrade_check():
    money = driver.find_element_by_css_selector("#money")
    money_num = int(money.text)

    cursor = driver.find_element_by_css_selector("#buyCursor")
    cursor_num = num_value(cursor)

    grandma = driver.find_element_by_css_selector("#buyGrandma")
    grandma_num = num_value(grandma)

    factory = driver.find_element_by_css_selector("#buyFactory")
    factory_num = num_value(factory)

    mine = driver.find_element_by_css_selector("#buyMine")
    mine_num = num_value(mine)

    shipment = driver.find_element_by_css_selector("#buyShipment")
    shipment_num = num_value(shipment)

    alchemy_lab = driver.find_element_by_css_selector("#buyAlchemy\ lab")
    alchemy_lab_num = num_value(alchemy_lab)

    portal = driver.find_element_by_css_selector("#buyPortal")
    portal_num = num_value(portal)

    time_machine = driver.find_element_by_css_selector("#buyTime\ machine")
    time_machine_num = num_value(time_machine)

    if money_num >= cursor_num:
        cursor.click()
        cookie.click()
    elif money_num >= grandma_num:
        grandma.click()
        cookie.click()
    elif money_num >= factory_num:
        factory.click()
        cookie.click()
    elif money_num >= mine_num:
        mine.click()
        cookie.click()
    elif money_num >= shipment_num:
        shipment.click()
        cookie.click()
    elif money_num >= alchemy_lab_num:
        alchemy_lab.click()
        cookie.click()
    elif money_num >= portal_num:
        portal.click()
        cookie.click()
    elif money_num >= time_machine_num:
        time_machine.click()
        cookie.click()
    else:
        pass

driver = webdriver.Chrome(executable_path="./chromedriver.exe")

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_css_selector("#cookie")

current_time = time.time()
end_time = current_time + 300

while time.time() < end_time:
    cookie.click()
    upgrade_check()

cps = driver.find_element_by_css_selector("#cps")
print(cps.text)

driver.quit()
