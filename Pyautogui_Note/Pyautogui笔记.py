import pyautogui

# 当前鼠标的信息
pyautogui.mouseInfo()

# 返回活动窗体的名称
# title = pyautogui.getActiveWindowTitle()
# print(title)

# 获取屏幕的大小
# S_size = pyautogui.size()
# print(S_size)

# 在指定位置按下/松开鼠标
# pyautogui.mouseDown(1775,31)
# pyautogui.mouseUp(1775,31)

# 鼠标左/右键单击,中键(滚轮键)单击
# pyautogui.click()  # 左键单击
# pyautogui.leftClick()  # 左键单击
# pyautogui.rightClick()  # 右键单击
# pyautogui.middleClick()  # 中键单击
# pyautogui.doubleClick()  # 左键双击
# pyautogui.tripleClick()  # 左键三击
#
# # 中键(滚轮键)滚动
# pyautogui.scroll(100) # 向上滚动100像素
# pyautogui.scroll(-100) # 向下滚动100像素
# pyautogui.hscroll(100)
# pyautogui.vscroll(100)
#
# # 鼠标移动位置
# pyautogui.moveTo(800, 150)  # 鼠标移动到指定位置
# pyautogui.moveRel(160, 390)  # 鼠标移动（按相对位置）
#
# pyautogui.dragTo(800, 250, duration=2)  # 拖动至坐标(800, 250)，耗时2秒
# pyautogui.dragRel(160, 390, duration=2)  # 拖动至相对位置，正数表示向右下拖拽，负数则相反


# 键盘相关
# print(pyautogui.isValidKey("|"))
# pyautogui.keyDown("g") # 按下
# pyautogui.keyUp("g")# 松开
#
# pyautogui.press(list('abcd'),5,0.5) # 按多个键,按的次数,间隔秒数
# pyautogui.write('Hello,world!',interval=0.5) # 键入指定字符串,每次间隔0.5秒
# pyautogui.hotkey('ctrl','shift','c') # 组合键,模拟ctrl+shift+c快捷键


# 截屏相关
# 全部
# screenshot = pyautogui.screenshot()
# # screenshot.show() # 展示
# screenshot.save("D:\screenshot.jpg") # 保存,里面添加路径

# 部分(截取屏幕的一部分)
# region = (100,100,300,300) # (left,top,width,height)
# part_screen = pyautogui.screenshot(region=region)
# part_screen.save('D:\part_screen.jpg')


# 其他
# pyautogui.displayMousePosition()  # 显示鼠标坐标和坐标点的RGB（在命令行中按Ctrl+C结束）
# pyautogui.sleep(0.1)  # 同time.sleep()
# pyautogui.printInfo()  # 输出 getinfo() 的内容

