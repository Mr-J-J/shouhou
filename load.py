# -*- coding: utf-8 -*-
# '''打开软件，自动链接'''
# '''使用方法：python3 main.py'''
# 将主程序与rustdesk放在同一目录下
# 初始化类会自动打开软件
# api:
# 改变标题：change_title(hwnd, title):
# 自动远程：input_account('id', '密码',title)
# 获取该远程信息:file_info('id'):
# 提交数据: submit_data(account,password)/提交数据会自动获取远程信息并且提交/





import subprocess
import time
import pyautogui
import pywinauto
import requests
import win32con
import win32gui
import os




# 远程类
class Remote:
    # 初始化
    # 阻塞运行
    def __init__(self):
        # 远程开始时间结束时间
        self.start_time = 0
        self.end_time = 0
        # 脚本运行间隔
        # pyautogui.PAUSE = 0.5
        # 启动软件
        self.app = pywinauto.Application(backend='uia')
        # 通过句柄绑定
        self.app.start('RustDesk')
        #       获取最顶层窗口
        self.main_window = self.app.top_window()
        self.main_window.wait('visible')
        # 最小化窗口
        self.main_window.minimize()
        self.hwnd = win32gui.FindWindow('H-SMILE-FRAME', None)
        # 开启保护模式
        pyautogui.FAILSAFE = True
        # 改变窗口标题
        self.change_title(self.hwnd, '奔腾电脑远程售后')

    # 改变窗口标题
    def change_title(self, hwnd, title):
        time.sleep(0.1)
        win32gui.SetWindowText(hwnd, title)

    # 获取该远程信息
    def file_info(self, title):
        #     读取当前用户目录下AppData\Roaming\RustDesk\config\peers的文件内容
        file_path = os.path.expanduser('~') + "\AppData\Roaming\RustDesk\config\peers" + "\\" + title + '.toml'
        #     如果文件存在，则读取文件内容
        if os.path.exists(file_path):
            # utf-8编码读取文件
            with open(file_path, 'r', encoding='utf-8') as f:
                # 获取文件内容
                content = f.read()
                # 查找指定字符串
                alias = self.find_str(content, "alias = '")
                username = self.find_str(content, "username = '")
                hostname = self.find_str(content, "hostname = '")
            return {'name': alias, 'username': username, 'hostname': hostname}
        else:
            return None

    # 查找指定字符串
    def find_str(self, content, str):
        start = content.find(str)
        if start == -1:
            return ''
        end = content.find("'", start + len(str))
        # 获取指定字符串
        alias = content[start + len(str):end]
        return alias

    # 上传数据
    def upload_data(self,data):
        #     发送get请求
        url = 'https://4bd6b408-e7ec-438f-83d2-8cba6cc6b874.bspapp.com/add/add?name=' + data['name'] + '&username=' + \
              data['username'] + '&hostname=' + data['hostname'] + '&time=' + str(data['time']) + '&start_time=' + str(
            data['start_time']) + '&end_time=' + str(data['end_time']) + '&my_hostname=' + data['my_hostname']
        requests.get(url)

    # 提交数据
    def submit_data(self,account,password):
        data = self.file_info(account)
        if data is not None:
            time_diff = int(time_diff)
            # now转换成时间戳
            now = int(time.mktime(time.strptime(now, '%Y-%m-%d %H:%M:%S')))
            stat = int(time.mktime(time.strptime(windows_time[window], '%Y-%m-%d %H:%M:%S')))
            data['time'] = time_diff
            data['start_time'] = stat
            data['end_time'] = now
            hostname = os.popen('hostname').read()
            data['my_hostname'] = hostname[:-1]
            # 上传数据
            upload_data(data)

    # 自动远程
    def input_account(self, account, password, title):
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
        # 等带输入框出现
        while True:
            # 获取account窗口
            account_hwnd = win32gui.FindWindow('H-SMILE-FRAME', account)
            if account_hwnd != 0:
                # 等带编辑框组件加载完成
                while True:
                    # 如果该控件存在
                    if self.app.connect(handle=account_hwnd).top_window().child_window(title="确认", control_type="Button").exists():
                        # 设置该窗口的title
                        self.change_title(account_hwnd, title)
                        win32gui.SetForegroundWindow(account_hwnd)
                        pyautogui.typewrite(password)
                        win32gui.SetForegroundWindow(account_hwnd)
                        pyautogui.press('enter')
                        pyautogui.press('enter')
                        # 最小化窗口
                        self.main_window.minimize()
                        if self.start_time == 0:
                            self.start_time = time.time()
                        # 点击确认
                        break
                    else:
                #         判断是否超过1分钟
                        if time.time() - self.start_time > 60:
                            break

                break

if __name__ == '__main__':
    Remote = Remote()
    # Remote.input_account('1078258647', 'iwvwhi','asdfa')
    print(Remote.file_info('1078258647'))
