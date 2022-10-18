from selenium import webdriver
from selenium.webdriver.common.by import By

cnt_tries = 0

def getKeyboard(driver):
    keys = driver.find_elements(By.XPATH, "//div[@class = 'Game-keyboard-button']")
    keyboard = {
        "q": keys[0],
        "w": keys[1],
        "e": keys[2],
        "r": keys[3],
        "t": keys[4],
        "y": keys[5],
        "u": keys[6],
        "i": keys[7],
        "o": keys[8],
        "p": keys[9],
        "a": keys[10],
        "s": keys[11],
        "d": keys[12],
        "f": keys[13],
        "g": keys[14],
        "h": keys[15],
        "j": keys[16],
        "k": keys[17],
        "l": keys[18],
        "z": keys[19],
        "x": keys[20],
        "c": keys[21],
        "v": keys[22],
        "b": keys[23],
        "n": keys[24],
        "m": keys[25]
    }

    return keyboard

def getPanels(driver):
    panels = []
    cnt_row = 0
    elm_rows = driver.find_elements(By.XPATH, "//div[@class='Row']")
    for elm_row in elm_rows:
        panels.append([])
        cnt_panel = 0
        elm_panels = elm_row.find_elements(By.XPATH, ".//*")
        for elm_panel in elm_panels:
            panels[cnt_row].append(elm_panel)
            cnt_panel += 1
        cnt_row += 1
    return panels