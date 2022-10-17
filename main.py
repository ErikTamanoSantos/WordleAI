from initVariables import *
import time

# create webdriver object
driver = webdriver.Chrome()
# get google.co.in
driver.get("https://wordlegame.org/")
keyboard = getKeyboard(driver)

panels = getPanels(driver)

for i in range(0, 4):
    print(str(i).center(20, "-"))
    for panel_row in panels:
        for panel in panel_row:
            print(panel.text, end="")
        print()
    keyboard["b"].click()
    keyboard["r"].click()
    keyboard["e"].click()
    keyboard["a"].click()
    keyboard["d"].click()
    time.sleep(1)

