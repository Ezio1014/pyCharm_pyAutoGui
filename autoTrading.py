import importlib as imp
import time
import pyautogui as pag

# .py file import
import trade_route as tr
import trade_def as td

imp.reload(tr)
imp.reload(td)

# 啟動循環跑商
# moneyNote = eval(input("紀錄目前存款"))
t = eval(input("跑商次數: "))
pag.hotkey('alt', 'tab', interval=0.1)
time.sleep(5)

for i in range(t):
    time.sleep(3)

    # 貿易路線1(東南亞+日本線(天津衛出發(758.9 s)))
    time_start = time.time()  # 開始計時
    tr.runSA_JP()
    time_end = time.time() - time_start  # 執行所花時間
    if i == 0:
        print('東南亞+日本線貿易時間:{:.1f}'.format(time_end), 's')
    if not td.verifyImg():
        break

    # 貿易路線2(歐非線(天津衛出發)(2069.4 s))
    time_start = time.time()  # 開始計時
    tr.runAF_EU()
    time_end = time.time() - time_start  # 執行所花時間
    if i == 0:
        print('歐非線貿易時間:{:.1f}'.format(time_end), 's')
    if not td.verifyImg():
        break

    # 自動貿易(遊戲內建功能(755+13 s))
    tr.AT()
    print("貿易完成 {} 次，剩餘 {} 次".format(i + 1, t - (i + 1)))
    # 貿易卷使用
    if i < t - 1:
        td.tradebook()

    # 驗證循環正常運作
    if not td.verifyImg():
        break

# 總路線耗時約 61 mins 利潤 1450w
