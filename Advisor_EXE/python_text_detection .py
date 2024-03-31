
import pyautogui
from PIL import Image
from pytesseract import *
#Note: You have to change the path below to your tesseract.exe location


def python_text_detection():
    pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    img = pyautogui.screenshot(region=(710, 130, 140, 80))
    output = pytesseract.image_to_string(img)
    output_index_3 = float(output[0:5])
    # print(type(output_index_3))
    print(output_index_3)
    return output_index_3

python_text_detection()




# pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
#
# #This line stores the image texttoconvert.png inside the img variable
# img = Image.open("Frame.png")
# img = pyautogui.screenshot(region=(710, 130, 140, 80))
# #Note: You can use pyautogui to fetch the screenshot instead of fetching it from a file
# # img = pyautogui.screenshot(region=(10,10,10,10))
#
# print(img)
# #
# # img = Image.open(img )
# # print(img)
# #This line uses pytesseract's image_to_string function to convert the image stored in the variable (img) into a string (text) that will be stored in the (output variable)
# output = pytesseract.image_to_string(img)
#
# #We can now print out the output
# print(output)
#
#
# print(type(output))
#output = output.split(',')
#print(output[0])
#print(output[1])
#print(output)
#print(len(output))
# python -m pip install --upgrade pip
# Python 3.7.7
# pip install Pillow
# pip install openCV-python  version 4.7.0.68
# pip install pytesseract


# pip --version
# pip install pyautogui
# pip install pyinstaller
# pip install pywinauto
# pyinstaller --version
# pip install auto-py-to-exe
# auto-py-to-exe



