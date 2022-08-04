# -*- coding: utf-8 -*-
# '''打开软件，自动链接'''


import subprocess
import time
import pyautogui
import win32con
import win32gui


# 远程类
class Remote:
    # 初始化
    # 阻塞运行
    def __init__(self):
        # 脚本运行间隔
        # pyautogui.PAUSE = 0.5
        # 启动软件
        subprocess.Popen('RustDesk.exe', close_fds=True)
        #     等到窗口可见
        while True:
            self.hwnd = win32gui.FindWindow('H-SMILE-FRAME', None)
            if self.hwnd != 0:
                break
        # 开启保护模式
        pyautogui.FAILSAFE = True
        # 改变窗口标题
        self.change_title(self.hwnd, '奔腾电脑远程售后')

    # 改变窗口标题
    def change_title(self, hwnd, title):
        time.sleep(0.1)
        win32gui.SetWindowText(hwnd, title)

    # 使用钩子函数输入账号密码
    def input_account(self, account, password):
        # 窗口重新获取焦点
        hwnd = win32gui.FindWindow('H-SMILE-FRAME', None)
        win32gui.SetForegroundWindow(hwnd)

        # 按两次tap
        pyautogui.press('tab')
        win32gui.SetForegroundWindow(hwnd)
        pyautogui.press('tab')
        win32gui.SetForegroundWindow(hwnd)
        pyautogui.typewrite(account)
        win32gui.SetForegroundWindow(hwnd)
        # 回车
        pyautogui.press('enter')
        # win32gui.SetForegroundWindow(hwnd)
        # # 输入密码
        # pyautogui.press(password)
        # win32gui.SetForegroundWindow(hwnd)
        # pyautogui.press('enter')


if __name__ == '__main__':
    Remote = Remote()
    Remote.input_account('528902606', 'mjn2mk')
