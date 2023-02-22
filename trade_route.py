import time
import pyautogui as pag

import trade_def as td


# 貿易路線1(東南亞+日本線(天津衛出發))
def runSA_JP():
    td.out_port()  # 天津衛出發

    # 淮安
    td.run_trading(942, 745, 25, 0)
    # 基隆
    td.next_port(871, 886, 1)
    td.navigation(3)
    td.flag(17)  # 海盜旗使用
    td.run_st(0)
    # 安汶
    td.search_port('安汶', 54)
    td.run_st(0)
    # 帝利
    td.run_trading(613, 778, 21, 0)
    # 巴達維亞
    td.search_port('巴達維亞', 38)
    td.run_st(0)
    # 巴領旁
    td.run_trading(708, 259, 17, 0)
    # 汶萊
    td.next_port(1301, 81)
    td.navigation(28)
    td.run_st(1)
    # 長崎
    td.search_port('長崎', 55)
    td.run_st(0)

    td.run_tradingItems(1131, 391, 26, [2, 3, 1])  # 京都
    td.run_trading(1005, 75, 36, 0, 1)  # 札幌
    td.run_trading(306, 457, 24, 0)  # 符拉迪沃斯托克
    td.run_trading(674, 887, 23, 0, 1)  # 釜山
    td.run_tradingItems(624, 265, 28, [4, 1, 3, 5])  # 平壤

    # 返回天津衛
    td.next_port(388, 462)
    td.navigation(21)
    td.selfGoods()


# 貿易路線2(歐非線(天津衛出發))
def runAF_EU():
    # 天津衛出發
    td.out_port()
    # 應天府
    td.run_tradingItems(896, 889, 32, [3, 1, 2, 4])
    # 廣州府
    td.search_port('廣州府', 32)
    td.buyGood([1, 5])
    td.out_port()
    # 汶萊(東南亞日本線殺價過不能再次執行，額外獨立寫)
    td.search_port('汶萊', 32)
    td.press_sleep("t", 1.5)
    td.click_xy(508, 361, 0.5)
    td.click_xy(1157, 244, 0.5)
    pag.press("num7")
    td.out_port()
    # 莫三比克
    td.search_port('莫三比克', 22)
    td.flag(74)  # 海盜旗使用
    td.buyGood([3, 5, 8])
    td.out_port()

    td.run_tradingItems(438, 881, 29, [4, 3, 6], 1)  # 索法拉
    td.run_tradingItems(787, 631, 16, [4, 5])  # 納塔爾
    td.run_tradingItems(120, 710, 35, [2, 5])  # 開普敦
    td.run_tradingItems(659, 53, 28, [6], 2)  # 卡里比布
    td.run_tradingItems(788, 57, 25, [3], 1)  # 本格拉

    # 魯安達(使用滑鼠滾輪)
    td.next_port(730, 177)
    td.navigation(20)
    td.press_sleep("t", 1.5)
    pag.moveTo(359, 445)
    time.sleep(0.2)
    pag.scroll(-200)
    time.sleep(0.3)
    td.click_xy(240, 646, 0.5)
    td.press_sleep("num3", 0.5)
    td.click_xy(1157, 244, 0.8)
    pag.press("num7")
    td.out_port()

    td.run_tradingItems(464, 163, 25, [4], 1)  # 聖多美
    td.run_tradingItems(820, 229, 20, [1])  # 貝南
    td.run_tradingItems(603, 381, 18, [2, 6])  # 聖喬治
    td.run_tradingItems(74, 425, 34, [4])  # 獅子山
    td.run_tradingItems(657, 57, 30, [7], 2)  # 阿爾金

    # 錫拉庫薩(圖片辨識出售商品)
    td.search_port('錫拉庫薩', 63)
    td.ImgAutoSold()
    td.buyGood([6])
    td.out_port()
    # 伊斯坦布爾
    td.search_port('伊斯坦布爾', 32)
    td.buyGood([6, 2])
    td.out_port()
    # 塞瓦斯托波爾
    td.run_tradingItems(1056, 204, 21, [2, 3, 4])
    # 基輔
    td.next_port(623, 143)
    td.navigation(23)
    td.selfGoods()
    td.buyGood([2, 3, 5])
    td.out_port()
    # 貝魯特
    td.search_port('貝魯特', 52)
    td.run_st(1)
    # 法馬古斯塔
    td.next_port(666, 494)
    td.navigation(19)
    td.run_st(0)
    # 雅法
    td.next_port(920, 520)
    td.navigation(13)
    td.run_st(0)
    # 亞歷山大
    td.next_port(458, 621)
    td.navigation(3)
    td.flag(17)  # 海盜旗使用
    td.run_st(1)
    # 威尼斯
    td.search_port('威尼斯', 40)
    td.buyGood([7, 5])
    td.out_port()
    # 那不勒斯
    td.next_port(885, 791)
    td.navigation(32)
    td.buyGood([8, 7, 2])
    td.out_port()
    # 馬拉加
    td.run_trading(54, 659, 31, 0, 1)
    # 南特
    td.search_port('南特', 39)
    td.run_st(0)
    # 漢堡
    td.search_port('漢堡', 35)
    td.run_st(1)
    # 波爾多
    td.search_port('波爾多', 36)
    td.run_st(0)
    # 塞維利亞
    td.search_port('塞維利亞', 33)
    td.run_st(0)
    # 瓦倫西亞
    td.run_trading(1110, 291, 25, 1)
    # 馬賽
    td.run_trading(1048, 241, 20, 0)
    # 比薩
    td.next_port(1135, 506)
    td.navigation(20)
    td.run_st(1, 1)
    # 雅典
    td.next_port(1442, 784)
    td.navigation(34)
    td.buyGood([4, 2, 5, 6, 7, 8, 1])
    td.out_port()
    # 返回天津衛
    td.search_port('天津衛', 146)
    td.flag(120)  # 海盜旗使用
    td.selfGoods()


# 自動貿易(最後一港脫離卡死 time:760s)
def AT():
    td.autoTrading()
    time.sleep(734)

    # 避免該死的漂流瓶...
    td.click_xy(1077, 217, 1)
    td.click_xy(757, 65, 1)

    td.press_sleep("m", 3)
    td.click_xy(1373, 823, 8)
    td.selfGoods()


# 貿易路線3(黑市商品流程使用)
def runBM():
    time.sleep(2)
    # 加來
    td.search_port('加來', 30)
    td.run_st(0)
    # 阿爾及爾 30
    td.search_port('阿爾及爾', 48)
    td.run_st(0)
    # 的黎波里 30
    td.search_port('的黎波里', 27)
    td.run_st(0)
    # 錫拉庫薩 30
    td.search_port('錫拉庫薩', 18)
    td.run_st(1)
    # 馬賽 30
    td.search_port('馬賽', 26)
    td.run_st(0)
    # 薩薩里 30
    td.search_port('薩薩里', 17)
    td.run_st(0)
    # 返回的黎波里
    td.search_port('的黎波里', 25)
    td.selfGoods()
