






# Initialize library
import os
import sys
import time
import subprocess
import ctypes
import uiautomation as auto
# Open Notepad  uiautomation  WindowControl
# subprocess.Popen('notepad')

subprocess.Popen(r'C:\Windows\System32\notepad.exe')

 # keyboard!!!!

# Identify Notepad Class
window = auto.WindowControl(searchDepth=1, ClassName = 'Notepad', RegexName = '.* - Notepad')

#Identify the screensize
# screenWidth, screenHeight = auto.GetScreenSize()
# window.MoveWindow(screenWidth // 4, screenHeight // 4, screenWidth // 2, screenHeight // 2)
# window.SetActive()h keyboard!!!!

#Find the format menuitem
window.MenuItemControl(Name = 'Format').Click()
#Click the Font within format menuitem
window.MenuItemControl(Name = 'Font...').Click()
windowFont = window.WindowControl(Name = 'Font')
# Select Font Family
windowFont.ComboBoxControl(AutomationId='1136').Select('Trebuchet MS')
# Select Font Style
windowFont.ComboBoxControl(AutomationId ='1137').Select('Bold Italic')
# Select Font Size
windowFont.ComboBoxControl(AutomationId = '1138').Select('28')
# Confirm the selection
windowFont.ButtonControl(Name = 'OK').Click()
edit = auto.EditControl(searchFromControl = window)  #or edit = window.EditControl()
edit.Click(waitTime = 0)
#Typing rich text on notepad
edit.SendKeys('Hello from UI Automation!!')
edit.SendKeys('{Ctrl}{A}', 0.2, 0)
window.MenuItemControl(Name = 'Format').Click()
window.MenuItemControl(Name = 'Font...').Click()
windowFont = window.WindowControl(Name = 'Font')
windowFont.ComboBoxControl(AutomationId = '1136').Select('Segoe UI Symbol')
windowFont.ComboBoxControl(AutomationId = '1138').Select('18')
windowFont.ButtonControl(Name = 'OK').Click()
edit.SendKeys('{Ctrl}{End}{Enter}Lets test with keyboard{! 4}{ENTER}', 0.2, 0)
edit.SendKeys('{Enter 2}0123456789{Enter}', waitTime = 0)
edit.SendKeys('{Enter}ABCDEFGHIJKLMNOPQRSTUVWXYZ{Enter}', waitTime = 0)
edit.SendKeys('{Enter}abcdefghijklmnopqrstuvwxyz{Enter}', waitTime = 0)
edit.SendKeys('{Enter}`~!@#$%^&*()-_=+{Enter}', waitTime = 0)
edit.SendKeys('{Enter}[]{{}{}}\\|;:\'\",<.>/?{Enter}{Ctrl}a')
# Click close button before exit
window.ButtonControl(searchDepth=2, Name='Close').Click()






# # Name the notepad
# window.ButtonControl(Name="Save").Click()
# auto.SendKeys('UIA')
# #Exit
# window.ButtonControl(Name="Save").Click()
