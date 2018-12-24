import time
import win32gui
import win32api
import win32con
import pyautogui as pag
import random




hwnd = win32gui.FindWindow(None, '阴阳师-网易游戏')			# 得到句柄
# hwnd = win32gui.FindWindow(None, '无标题 - 画图')


def GetMouseLocation():
    """
    获取并返回鼠标位置
    :return:鼠标位置坐标
    """
    ptx, pty = pag.position()  								# 获取当前鼠标的位置
    return ptx,pty


def Click(x, y):											# 向窗口发送点击指令，x、y是相对于窗口的位置

	lParam = win32api.MAKELONG(x, y)
# win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)						# 将窗口调到前台
	win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)
	win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
	win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON,  lParam)


def GetWindowLocation():									# 获得窗口位置及大小
	rect = win32gui.GetWindowRect(hwnd)
	x_left = rect[0]
	y_up = rect[1]
	x_right = rect[2]
	y_down = rect[3]										# 获得窗口边框位置
	w = rect[2] - rect[0]
	h = rect[3] - rect[1]
	print ("Window_name %s:" % win32gui.GetWindowText(hwnd))
	print ("class_name %s:" % win32gui.GetClassName(hwnd))
	print(x_left, x_right, y_up, y_down)					
	print ("Size: (%d, %d)" % (w, h))


def ChallengeLocation():									# 魂十挑战按钮相对窗口位置
	x = random.randint(395, 453)
	y = random.randint(208, 235)
	return x, y


def ClearingLocation():										# 战斗结束点击的位置获取
	x = random.randint(10, 90)
	y = random.randint(190, 270)
	return x, y


