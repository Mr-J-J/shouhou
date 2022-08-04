# -*- coding: utf-8 -*-

import pywinauto
import pyautogui

def input_account(account, password):
    # 禁用鼠标
    pyautogui.FAILSAFE = False
    # 按两次tap
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite(account)
    # 回车
    pyautogui.press('enter')

# 主类
class MainWindow():
     # 初始化
    def __init__(self):
#         启动软件并关联
        self.app = pywinauto.Application(backend='uia')
        self.app.start('RustDesk')
#       获取最顶层窗口
        self.main_window = self.app.top_window()
        self.main_window.wait('visible')

        input_account('123', '123')
        # 获取连接按钮
        # self.main_window.child_window(title="连接", control_type="Button").click()
            # self.main_window.123

# 主函数
if __name__ == '__main__':123

    rust = MainWindow()