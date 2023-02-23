import time
import pyautogui as pag
import keyboard
import numpy as np
import cv2
import os


# pyautogui.press+sleep組合鍵
def press_sleep(key, t):
    pag.press(key)
    time.sleep(t)


# 點擊座標組合鍵
def click_xy(x, y, t):
    pag.moveTo(x, y)
    time.sleep(0.2)
    pag.click()
    time.sleep(t)


# 購買指定商品 buy = [itemDict指定商品]
def buyGood(buy):
    itemDict = {1: [238, 217], 2: [521, 210], 3: [246, 357], 4: [508, 361], 5: [246, 504], 6: [542, 504], 7: [240, 646],
                8: [527, 646]}

    time.sleep(0.8)
    press_sleep("t", 1.6)
    for i in buy:
        click_xy(itemDict[i][0], itemDict[i][1], 0.6)
        img = pag.locateOnScreen('./image/verifyImg/price_off.png', confidence=0.8, region=(680, 700, 300, 160))
        if img:
            press_sleep("num3", 0.6)
        click_xy(1157, 244, 0.6)
    pag.press("num7")


# 交易介面
def trading(x=None):
    time.sleep(1.2)
    press_sleep("t", 1.5)
    if x == 1:
        press_sleep("num4", 6)
    else:
        press_sleep("num1", 6)
    pag.press("num7")


# 出港介面
def out_port():
    time.sleep(0.7)
    press_sleep("m", 1.5)
    press_sleep("num2", 4)


# 導航介面
def navigation(t):
    time.sleep(1.5)
    press_sleep("num3", 2.1)
    pag.press("space")
    time.sleep(t)


# 縮小地圖
def zoomOutMap(t):
    time.sleep(2)
    for i in range(t):
        time.sleep(1.1)
        pag.press("num9")
    time.sleep(1.5)


# 點擊下一個港口+合併縮小地圖
def next_port(x, y, zoom=None):
    if zoom == None:
        click_xy(x, y, 0)
    else:
        zoomOutMap(zoom)
        click_xy(x, y, 0)


# 搜尋港口+導航至下一個港口
def search_port(p, t):
    click_xy(490, 110, 1)
    keyboard.write(p)
    time.sleep(0.7)
    click_xy(650, 110, 1)
    click_xy(650, 110, 1.6)
    next_port(793, 473)
    navigation(t)


# 出售貨物
def selfGoods():
    time.sleep(1)
    press_sleep("t", 1.5)
    press_sleep("space", 1)
    press_sleep("num8", 1)
    pag.press("num7")


# 使用海盜旗
def flag(t):
    time.sleep(6)
    click_xy(933, 840, t)


# 買賣合一
def run_st(s, t=None):
    if s == 1:
        selfGoods()
    trading(t)
    out_port()


# 跑商流程合併(推薦品)
def run_trading(x, y, t, st, zoom=None):
    next_port(x, y, zoom)
    navigation(t)
    run_st(st)


# 跑商流程合併(指定商品)
def run_tradingItems(x, y, t, buy, zoom=None):
    next_port(x, y, zoom)
    navigation(t)
    buyGood(buy)
    out_port()


# 自動貿易(遊戲內建功能(18mins))
def autoTrading():
    time.sleep(4)
    click_xy(1533, 460, 2)
    click_xy(1340, 676, 2)
    click_xy(1281, 796, 0)


# 貿易卷使用
def tradebook():
    time.sleep(2)
    press_sleep("t", 1.5)
    click_xy(1159, 174, 1.2)
    click_xy(1159, 289, 1.2)
    press_sleep("num7", 1.5)


# 辨識+出售貿易商品 Point(x=735, y=210) Point(x=1420, y=675)
def ImgAutoSold():
    img_list = os.listdir("./image/tradeImg")  # 遍歷資料夾內檔案
    time.sleep(1)
    press_sleep("t", 1.5)

    for i in img_list:
        img = pag.locateOnScreen('./image/tradeImg/{}'.format(i), confidence=0.9, region=(735, 210, 685, 465))
        if img:
            x, y = pag.center(img)
            click_xy(x, y, 0.7)
    click_xy(1045, 742, 0.7)
    click_xy(705, 242, 0.5)
    click_xy(1267, 185, 0.7)
    press_sleep("num7", 1.2)


# 辨識+購買黑市商人商品
def black_market(p=None, t=None):
    img_list = os.listdir("./img")  # 遍歷資料夾內檔案
    goodItems = {0: [75, 165], 1: [365, 165], 2: [75, 275], 3: [365, 275], 4: [75, 385]}  # totalHeight:475
    time.sleep(1)
    if p != None:
        search_port(p, t)

    time.sleep(1)
    press_sleep("num0", 3)
    for i in img_list:
        if i == 'ghostFlag.png':
            for j in goodItems:
                img = pag.locateOnScreen('./img/ghostFlag.png', confidence=0.9 \
                                         , region=(goodItems[j][0], goodItems[j][1], 280, 95))
                if img:
                    x, y = pag.center(img)
                    click_xy(x, y, 0.7)
                    click_xy(947, 714, 0.7)
                    press_sleep('num8', 1)
        else:
            img = pag.locateOnScreen('./img/{}'.format(i), confidence=0.9, region=(70, 160, 580, 320))
            if img:
                x, y = pag.center(img)
                click_xy(x, y, 0.7)
                click_xy(947, 714, 0.7)
                press_sleep('num8', 1)
    press_sleep('num7', 1)
    press_sleep('num2', 1.5)


# 辨識驗證
def verifyImg():
    verify = False
    img = pag.locateOnScreen('./image/verifyImg/verify01.png', confidence=0.8, region=(740, 35, 100, 40))
    verify = True if img else False
    return verify
