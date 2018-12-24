# 此脚本只可使用于窗口的大小为宽568高320的脚本，请自行修改窗口大小
# 为魂十单刷脚本
# by 橙汁

from function import *
import os

# hwnd = win32gui.FindWindow(None, '阴阳师-网易游戏')
os.system('cls')
number = 0
while True:
	print('已经刷了%d次啦' % number)
	(x, y) = ChallengeLocation()					# 战斗开始前点击
	Click(x, y)
	time.sleep(random.uniform(65, 67))				# 等待战斗时间
	(x, y) = ClearingLocation()
	Click(x, y)										# 结算点击
	# Click()
	time.sleep(random.uniform(2, 4))
	# ptx, pty = GetMouseLocation()
	# print(ptx, pty)
	number += 1
	os.system('cls')

