import importlib as imp
import time
import pyautogui as pag

# .py file import
import trade_route as tr
import trade_def as td

imp.reload(tr)
imp.reload(td)


# 計時器
def timer(func, timer_show):
    if i == 0:
        time_st = time.time()  # 開始計時
        func()
        time_end = time.time()  # 結束計時
        print(timer_show, '{:.1f}'.format(time_end - time_st), 's')
    else:
        func()


# 啟動循環跑商
# moneyNote = eval(input("紀錄目前存款"))
t = eval(input("跑商次數: "))
pag.hotkey('alt', 'tab', interval=0.1)
i = 0
time.sleep(5)

while True:
    if i == t:
        print('收工')
        break
    time.sleep(3)

    # 貿易路線1(東南亞+日本線(天津衛出發(758.9 s)))
    timer(tr.runJP, '日本線貿易時間:')
    
    # 驗證循環正常運作1
    # if not td.verifyImg():
    #     print('中斷01')
    #     break

    # 貿易路線2(歐非線(天津衛出發)(2069.4 s))
    timer(tr.runAF_EU, '歐非線貿易時間:')

    # 驗證循環正常運作2
    # if not td.verifyImg():
    #     print('中斷02')
    #     break

    # 自動貿易(遊戲內建功能(762.4 s))
    timer(tr.AT, '自動貿易時間:')
    print("貿易完成 {} 次，剩餘 {} 次".format(i + 1, t - (i + 1)))

    # 貿易卷使用
    if i < t - 1:
        td.tradebook()

    # 驗證循環正常運作3
    if not td.verifyImg():
        print('中斷03')
        break

    i += 1

# 總路線耗時約 61 mins 利潤 1450w
