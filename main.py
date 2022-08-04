# -*- coding: utf-8 -*-
# '''远程售后,记录窗口时长'''
import time
import os
import win32gui
import requests
import subprocess
# 查询字符
def find_str(content,str):
    start = content.find(str)
    if start == -1:
        return ''
    end = content.find("'", start + len(str))
    # 获取指定字符串
    alias = content[start + len(str):end]
    return alias

def file_info(title):
#     读取当前用户目录下AppData\Roaming\RustDesk\config\peers的文件内容
    file_path = os.path.expanduser('~') + "\AppData\Roaming\RustDesk\config\peers" + "\\" + title + '.toml'
#     如果文件存在，则读取文件内容
    if os.path.exists(file_path):
        # utf-8编码读取文件
        with open(file_path, 'r', encoding='utf-8') as f:
            # 获取文件内容
            content = f.read()
            # 查找指定字符串
            alias = find_str(content, "alias = '")
            username = find_str(content, "username = '")
            hostname = find_str(content, "hostname = '")
        return {'name': alias, 'username': username, 'hostname': hostname}
    else:
        return None
# 上传数据
def upload_data(data):

#     发送get请求
    url = 'https://4bd6b408-e7ec-438f-83d2-8cba6cc6b874.bspapp.com/add/add?name=' + data['name'] + '&username=' + data['username'] + '&hostname=' + data['hostname'] + '&time=' + str(data['time']) + '&start_time=' + str(data['start_time']) + '&end_time=' + str(data['end_time']) + '&my_hostname=' + data['my_hostname']
    # print(url)
    r = requests.get(url)
    # print(r.text)
if __name__ == '__main__':
    had = False
    subprocess.Popen("RustDesk", close_fds=True)
    while True:
        # 获取‘Rustdesk’窗口的句柄
        hwn = win32gui.FindWindow('H-SMILE-FRAME', None)
        # 如果有窗口则进行监督，窗口关闭推出程序
        if hwn:
            had = True
            break
    windows = []
    windows_time = {}
    if had:
        while True:
            # 获取‘Rustdesk’窗口的句柄
            hwnd = win32gui.FindWindow('H-SMILE-FRAME', None)
            # 如果有窗口则进行监督，窗口关闭推出程序
            if hwnd:
                title = win32gui.GetWindowText(hwnd)
                # print(title)
                #     如果windows列表中不存在该下标，则添加进去
                if title not in windows:
                    # 将此窗口标题付给windows
                    time.sleep(1)
                    title = win32gui.GetWindowText(hwnd)
                    # 获得当前时间
                    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                    # 将时间和窗口标题添加进windows_time对象
                    windows_time[title] = now
                    windows.append(title)
                #     如果windows列表中不存在该窗口，则删除这个窗口
                for window in windows:
                    hwnd1 = win32gui.FindWindow(None, window)
                    if hwnd1 == 0:

                        # 获取当前时间
                        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                        # 计算now到windows_time[window]过了多少秒
                        time_diff = time.mktime(time.strptime(now, '%Y-%m-%d %H:%M:%S')) - time.mktime(
                            time.strptime(windows_time[window], '%Y-%m-%d %H:%M:%S'))
                        # 获取文件信息
                        data = file_info(window)
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
                        windows.remove(window)
                        windows_time.pop(window)
            else:
                time.sleep(1)
                break



    # # 运行Bent.exe文件
    # a = os.system('RustDesk.exe')
    # while True:
    #     # 获取‘Rustdesk’窗口的句柄
    #     hwnd = win32gui.FindWindow('H-SMILE-FRAME', None)
    #     # 如果有窗口则进行监督，窗口关闭推出程序
    #     if hwnd:
    # main()
            # break
