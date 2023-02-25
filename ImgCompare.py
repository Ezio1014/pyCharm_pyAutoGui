import importlib as imp
import time
import pyautogui as pag
import keyboard
import numpy as np
import cv2
import msvcrt
from datetime import datetime
import trade_def as td
import trade_route as tr

imp.reload(td)
imp.reload(tr)


# 黑市購買迴圈
def route_bm():
    place_dict = {'阿姆斯特丹': 16, '安特衛普': 16, '倫敦': 15, '加來': 18, '普利茅斯': 17, '南特': 20 \
        , '波爾多': 15, '波爾圖': 25, '里斯本': 16, '塞維利亞': 16, '休達': 13, '阿爾及爾': 20}
    time.sleep(2)

    td.black_market()  # 漢堡

    # 搭配字典應用 v2.0
    for key, value in place_dict.items():
        td.black_market(key, value)

    td.search_port('漢堡', 61)  # 返回漢堡


def route_bm2():
    place_dict = {'突尼斯': 17, '錫拉庫薩': 19, '那不勒斯': 16, '比薩': 17, '熱那亞': 15 \
        , '馬賽': 17, '巴賽隆納': 16, '瓦倫西亞': 15, '阿爾及爾': 16, '休達': 20 \
        , '塞維利亞': 13, '里斯本': 15, '波爾圖': 15}
    # , '波爾多': 23, '南特': 14
    time.sleep(2)
    td.black_market()  # 的黎波里
    # 搭配字典應用 v2.0
    for key, value in place_dict.items():
        td.black_market(key, value)
    time.sleep(1)
    td.search_port('的黎波里', 1)  # 的黎波里


def next_month(m):
    if m == 12:
        m = 1
    else:
        m += 1


# 判斷日期進程啟動(運行OK)
month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 30}

stop = eval(input("運作次數："))  # times
m = eval(input("請輸入月份："))  # 月
d = eval(input("請輸入日期："))  # 日
times = 0

while True:
    if d == month[m]:  # 當月最後一天
        time.sleep(600 + 61 - int(datetime.now().strftime('%S')))
        d = 10
        next_month(m)
    elif 10 < d < month[m]:
        time.sleep(600 + 61 - int(datetime.now().strftime('%S')) + (month[m] - d - 1) * 60)
        d = 10
        next_month(m)
    elif d < 10:
        time.sleep(61 - int(datetime.now().strftime('%S')) + (60 * (10 - (d + 1))))
        d = 10

    if d == 10:
        td.click_xy(363, 17, 1)
        st = time.time()
        route_bm2()
        print("採購完成 {} 次，剩餘 {} 次".format(times + 1, stop - (times + 1)))
        if times == 0:
            print("用時:{:.1f} s".format(time.time() - st))
        times += 1
        if times == stop:
            break
        edm = int((time.time() - st) / 60)
        time.sleep((60 - int(datetime.now().strftime('%S'))) + ((month[m] - (d + edm + 1) + 1) * 60) + 601)
        next_month(m)
