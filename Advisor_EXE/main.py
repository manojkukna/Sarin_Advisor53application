import os
from tkinter import *
from tkinter import filedialog as fd
from PIL import Image
import pytesseract
from pytesseract import image_to_string

win = Tk()
win.geometry("600x400")
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
#  C:\Program Files (x86)\Tesseract-OCR


def done():
    filename = fd.askopenfilename()
    s = filename
    s=s.replace("\\","//")
    img = Image.open(s)
    t = image_to_string(img)
    label = Text(win,bd=2,font="Times 32",width=40,height=20,wrap=WORD)
    label.insert(INSERT,t)
    label.pack()
    f = open("new.txt","w")
    f.write(t)

l = Label(win,text ="click to run parser").pack()
button = Button(win,text="Parser",command=done).pack()


win.mainloop()



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



