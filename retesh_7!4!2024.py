

import cv2
import pytesseract


import pyautogui
from PIL import Image
from pytesseract import *
#Note: You have to change the path below to your tesseract.exe location


# css
#



# Path to the image file
image_path = 'photo_2024-04-07_14-13-34.jpg'

locsan = "./PNGFIL"

# Read the image using OpenCV
# image = cv2.imread(image_path)
#
# # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform text detection using PyTesseract
text = pytesseract.image_to_string(f"{locsan}")




# Print the detected text
# print("Detected text:")
# print(text)


# It seems like you've provided some text data with phone numbers and other miscellaneous content. If you're looking to extract phone numbers from this text data in Python, you can use regular expressions. Here's a simple example:
# import re
#
# text_data = """
# +91 95868 32889
#
# +91 96244 71708
# | love you PAPA &
#
# +91 96245 55152
# Hey there! I am using WhatsApp.
#
# +91 96878 46627
#
# +91 97243 97422
# Hey there! I am using WhatsApp.
#
# +91 98250 88744
# Available
#
# +91 98251 72946
#
# +91 98255 82200
# Om
#
# 0 ~ 8 a t 8 $
#
# +91 99090 95050
#
# +91 99092 78547
# Kbhi kisi pr bhrosa mt kma kuki ........
#
# Ce
# """
#
# phone_numbers = re.findall(r'\+\d{2} \d{5} \d{5}', text_data)

# for number in phone_numbers:
#     print(number)
#







#
import re
import csv
#
# text_data = """
# +91 95868 32889
#
# +91 96244 71708
# | love you PAPA &
#
# +91 96245 55152
# Hey there! I am using WhatsApp.
#
# +91 96878 46627
#
# +91 97243 97422
# Hey there! I am using WhatsApp.
#
# +91 98250 88744
# Available
#
# +91 98251 72946
#
# +91 98255 82200
# Om
#
# 0 ~ 8 a t 8 $
#
# +91 99090 95050
#
# +91 99092 78547
# Kbhi kisi pr bhrosa mt kma kuki ........
#
# Ce
# """


print(type(text),text)




phone_numbers1 = re.findall(r'\+\d{2} \d{5} \d{5}', text)



print(type(phone_numbers1),phone_numbers1)


# # Writing phone numbers to a CSV file
# with open('phone_numbers.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Phone Numbers'])
#     for number in phone_numbers1:
#         writer.writerow([number])
#
# print("Phone numbers have been saved to phone_numbers.csv file.")
#
#




# Writing phone numbers to a CSV file
with open('phone_numbers.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Phone Numbers'])
    for number in phone_numbers1:
        writer.writerow([number])

print("Phone numbers have been saved to phone_numbers.csv file.")



import pandas as pd



data = {'Phone numbers':phone_numbers1}

df = pd.DataFrame(data)




print(df)


# #
# # breakpoint()
# # def python_text_detection():
# #     pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
# #     img = pyautogui.screenshot(region=(710, 130, 140, 80))
# #     output = pytesseract.image_to_string(img)
# #     output_index_3 = float(output[0:5])
# #     # print(type(output_index_3))
# #     print(output_index_3)
# #     return output_index_3
#
# python_text_detection()









#
# https://stackoverflow.com/questions/66480785/using-python-pywinauto-not-able-to-get-control-of-a-tab
#
#





#
# How found:	Mouse move (47,53)
# 	hwnd=0x00080E38 64bit class="SysTabControl32" style=0x54008440 ex=0x0
# RuntimeId:	"[42.527928.2.-2147483647.527928.-4.1]"
# BoundingRectangle:	{l:2 t:44 r:592 b:81}
# ProcessId:	6504
# ControlType:	UIA_TabItemControlTypeId (0xC363)
# LocalizedControlType:	"tab item"
# Name:	"Dummy"
# AccessKey:	""
# HasKeyboardFocus:	false
# IsKeyboardFocusable:	true
# IsEnabled:	true
# HelpText:	""
# IsPassword:	false
# IsOffscreen:	false
# ProviderDescription:	"[pid:6504,hwnd:0x0 Annotation:Microsoft: Annotation Proxy (unmanaged:uiautomationcore.dll); Main(parent link):Microsoft: MSAA Proxy (unmanaged:uiautomationcore.dll)]"
# SelectionItem.IsSelected:	true
# SelectionItem.SelectionContainer:	"" tab
# IsDockPatternAvailable:	false
# IsExpandCollapsePatternAvailable:	false
# IsGridItemPatternAvailable:	false
# IsGridPatternAvailable:	false
# IsInvokePatternAvailable:	false
# IsMultipleViewPatternAvailable:	false
# IsRangeValuePatternAvailable:	false
# IsScrollPatternAvailable:	false
# IsScrollItemPatternAvailable:	false
# IsSelectionItemPatternAvailable:	true
# IsSelectionPatternAvailable:	false
# IsTablePatternAvailable:	false
# IsTableItemPatternAvailable:	false
# IsTextPatternAvailable:	false
# IsTogglePatternAvailable:	false
# IsTransformPatternAvailable:	false
# IsValuePatternAvailable:	false
# IsWindowPatternAvailable:	false
# IsItemContainerPatternAvailable:	false
# IsVirtualizedItemPatternAvailable:	false
# FirstChild:	[null]
# LastChild:	[null]
# Next:	[null]
# Previous:	[null]
# Other Props:	Object has no additional properties
# Children:	Container has no children
# Ancestors:	"" tab
# 	"" dialog
# 	"Advisor 5.3 Professional Lens 2    214-2   0.811 ct. ***
# 	"Desktop" pane
# 	[ No Parent ]









# # Loop through each tab control and retrieve its texts
# for tab_control in tab_controls:
#     tab_wrapper = TabControlWrapper(tab_control)
#     tab_texts = tab_wrapper.texts()
#     print(tab_texts)
#
#
#
# # Get all tab controls in the main window
# tab_controls = main_window.children(class_name='SysTabControl32')
#
# # Loop through each tab control and print its access name
# for tab_control in tab_controls:
#     print(tab_control.window_text())
    #
    # User
    # | TabControl - ''(L3, T45, R593, B82)
    # | | ['TabControl', 'TabControlDummy', 'TabControl0', 'TabControl1', 'TabControlDummy0', 'TabControlDummy1']
    # | | child_window(class_name="SysTabControl32")
    # | |
    #
    # Impl: Local
    # oleacc
    # proxy
    # AnnotationID: 010000
    # 80
    # CE020100FCFFFFFF01000000
    # Name: "Dummy"
    # Value: [null]
    # Role: page
    # tab(0x25)
    # State: selected, focusable, selectable(0x300002)
    # Location: {l: 5, t: 47, w: 590, h: 37}
    # Description: [null]
    # Kbshortcut: [null]
    # DefAction: "Switch"
    # Help: [null]
    # HelpTopic: ""
    # ChildCount: 0
    # Window: 0x102CE
    # FirstChild: [null]
    # LastChild: [null]
    # Next: [null]
    # Previous: [null]
    # Left: [null]
    # Up: [null]
    # Right: [null]
    # Down: [null]
    # Other
    # Props: Object
    # has
    # no
    # additional
    # properties
    # Children: Container
    # has
    # no
    # children
    # Ancestors: none: page
    # tab
    # list: focusable
    # none: window: focusable
    # none: dialog: focusable
    # none: window: focusable
    # "Advisor 5.3 Professional Lens 2    214-2   0.811 ct. ***
    # "Advisor 5.3 Professional Lens 2    214-2   0.811 ct. ***
    # "Desktop": client: focusable
    # "Desktop": window: focusable
    # [No Parent]


