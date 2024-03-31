import time
import pyautogui
from datetime import datetime
import tkinter
from tkinter import *
from PIL import Image
from pytesseract import *
from pywinauto import application





from pywinauto import application
# pip install openCV-python
# pip install pyautogui
# pip install pywinauto
# pip install pyinstaller



#  ////////progam mame Advisor 24/11/2022 06:45 pm /////////////////
#  ////////progam mame Advisor 05/12/2022 11:36 pm /////////////////
#  ////////progam mame Advisor 03/01/2023 11:36 pm /////////////////
#  ////////progam mame Advisor 14/01/2023 04:13 pm /////////////////           opne_text NONE VALLU
#////////progam mame Advisor 15/01/2023 10:34 pm /////////////////           python_text_detection
#  ////////progam mame Advisor 16/01/2023 12:16 pm /////////////////           python_text_detection
#  ////////progam mame Advisor 16/01/2023 12:16 pm /////////////////           python_text_detection
#  ////////progam mame Advisor 16/01/2023 12:23 pm /////////////////           Planning_Templates
#  ////////progam mame Advisor 17/01/2023 02:11 AM /////////////////           def  PEAR
#  ////////progam mame Advisor 17/01/2023 11:14 AM /////////////////           def  ROUND
#  ////////progam mame Advisor 17/01/2023 11:14 AM /////////////////           def  OVAL



def time_():
    time_ = time.strftime("%H:%M:%S", time.localtime())
    return time_
start_time = str(time_())
#////////         current  darty =   ("./PNGFIL/multiplan.PNG")
def none_valu(image, confide_):
    locsan=  "./PNGFIL"
    moveTo_ = pyautogui.locateCenterOnScreen(f"{locsan}/{image}", confidence=confide_)
    while moveTo_ is None:
        time.sleep(1)
        print(moveTo_, f'{image}',"none_valu", time_())
        moveTo_ = pyautogui.locateCenterOnScreen(f"{locsan}/{image}", confidence=confide_)
    else:
        # time.sleep(1)
        print(f'{image}', "NOT none_valu", time_())
        return moveTo_
def locate_leftClick(image, confide_, clicks_):
    moveTo_ = none_valu(image=image, confide_=confide_)
    pyautogui.moveTo(moveTo_, duration=0.10)
    clicks_ = clicks_
    pyautogui.click(clicks=clicks_)

def locate_rightClick(image, confide_, clicks_):
    moveTo_ = none_valu(image=image, confide_=confide_)
    pyautogui.moveTo(moveTo_, duration=0.10)
    clicks_ = clicks_
    pyautogui.click(button='right', clicks=clicks_)


def multiplan(image):
    # time.sleep(1)
    multiplan = locate_leftClick(image=image, confide_=0.80, clicks_=1)
    print(multiplan, "multiplan", time_())
def bestpair(image):
    bestpair = locate_leftClick(image=image, confide_=0.90, clicks_=1)
    pyautogui.dragRel(0, 50, )
    # time.sleep(3)
    print(bestpair, "bestpair", time_())
def suggestion_all(image,okPNG):
    # time.sleep(3)
    locate_leftClick(image=image, confide_=0.80, clicks_=2)
    x,y = pyautogui.position()
    pyautogui.click(button='right', x=x, y=y)
    pyautogui.dragRel(0,25,duration=0.15)
    locate_leftClick(image=okPNG, confide_=0.90, clicks_=1)
    # time.sleep(1)
    print(f"{image}/{okPNG}","suggestion_all", time_())
opne_text_append = []
current = 0.00


def python_text_detection():
    try:
       pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
       img = pyautogui.screenshot(region=(710, 130, 140, 80))
       output = pytesseract.image_to_string(img)
       result = float(output[0:5])
    except ValueError:
        result = python_text_detection()
        print(result, " ValueErro python_text_detection", time_())
    print(result,"python_text_detection", time_())
    return result


# open_text_clear(txt="opne_txt.txt")
current_valu = []
plan_total = []
all_plan_total = []
sawless_count = 0
def sawless(image):
    global sawless_count
    opne_text_ = 0
    current = 0.1
    plan_count = 0
    all_plan_count = 0
    sawless_count = 0
    while float(current) > 0.0039 and opne_text_ < 5:
        locate_leftClick(image=image, confide_=0.90, clicks_=1)
        pyautogui.dragRel(0, 50, )
        none_valu(image=image, confide_=0.80)

        current = python_text_detection()
        current_valu.append(python_text_detection())
        print(current_valu[-1], " current", time_())
        if len(current_valu) > 2:
            if current_valu[-1] == current_valu[-2]:
               opne_text_ = opne_text_ + 1
               # time.sleep(1)
        sawless_count = sawless_count + 1
        print("                                                                        sawless_count :", sawless_count)

    plan_count = plan_count + 1
    plan_total.append(plan_count)
    all_plan_count = all_plan_count + 1
    all_plan_total.append(all_plan_count)
def scroll_click(image,clicks):
    # time.sleep(1)
    scroll_click=locate_leftClick(image=image, confide_=0.95, clicks_=clicks)
    pyautogui.dragRel(-235,120)
    pyautogui.click(clicks=1)
    pyautogui.dragRel(0,100)
    pyautogui.click(clicks=1)
    print(scroll_click, "scroll_click", time_())
def scroll_dwon_click(image,clicks):
    time.sleep(1)
    scroll_click=locate_leftClick(image=image, confide_=0.95, clicks_=clicks)
    pyautogui.dragRel(-235,-700)
    pyautogui.click(clicks=1)
    pyautogui.dragRel(0,100)
    pyautogui.click(clicks=1)
    print(scroll_click, "scroll_click", time_())
def ResultComparison(image):
    time.sleep(1)
    locate_leftClick(image=image, confide_=0.90, clicks_=1)
    print("ResultComparison_leftClick", time_())
def Group_Name_Sort_Confirm(image):
    locsan = "./PNGFIL"
    time.sleep(1)
    moveTo_ = pyautogui.locateCenterOnScreen(f"{locsan}/{image}", confidence=0.90)
    while moveTo_ is None:
          time.sleep(1)
          moveTo_ = locate_leftClick(image="Weight.PNG", confide_=0.80, clicks_=1)
          pyautogui.move(0, 15)
          pyautogui.click(clicks=1)

          print(moveTo_, "Weight.PNG", time_())
          moveTo_ = pyautogui.locateCenterOnScreen(f"{locsan}/Group_Name_Sort.PNG", confidence=0.80)
          # time.sleep(1)
          pyautogui.moveTo(moveTo_, duration=0.10)
    else:
         Group ="Group_Name_Sort.PNG"
         moveTo_Group = pyautogui.locateCenterOnScreen(f"{locsan}/{ Group}", confidence=0.90)
         if moveTo_ == moveTo_Group:
            time.sleep(1)
            pyautogui.moveTo(moveTo_, duration=0.10)
            print(f'{ Group }', "Group_Name_Sort.PNG", time_())
    return moveTo_
def Min_polish_pant(image2,image):
    if sawless_count == 1:
       LIST=[0,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400,425,450,475,500]
       plan_total_ = LIST[sum(plan_total)]
       Group_Name_Sort = locate_leftClick(image=image2, confide_=0.80, clicks_=1)
       pyautogui.move(0, 15)
       time.sleep(1)
       pyautogui.click(clicks=1)
       group_Name_PNG = locate_leftClick(image=image, confide_=0.80, clicks_=2)
       pyautogui.dragRel(0,plan_total_, )
       pyautogui.click(clicks=2)
       Group_Name_Sort2 = locate_leftClick(image=image2, confide_=0.80, clicks_=1)
       pyautogui.move(0, 15)
       pyautogui.click(clicks=1)
       print(f'Group_Name_Sort :{Group_Name_Sort}group_Name_PNG:{group_Name_PNG}//{Group_Name_Sort2}', "Min_polish_pant", time_())
       print(f'pant dunn :{plan_total_}sum(plan_total):{sum(plan_total)}', "Min_polish_pant", time_())
def group_Name_selet(image):
    time.sleep(1)
    Group_Name_Sort_Confirm(image="Group_Name_Sort.PNG")
    if (0.0039) > float(current_valu[-1]) and sawless_count == 1:
        Min_polish_pant(image="group_Name.PNG",image2="Group_Name_Sort.PNG")
    else:
       solution_selet = locate_leftClick(image=image, confide_=0.80, clicks_=1)
       pyautogui.dragRel(0, 50,)
       pyautogui.click(clicks=2)
       time.sleep(1)
       print(solution_selet, sawless_count,current_valu[-1], "group_Name_selet", time_())
def tag_click(image,dragRel,okPNG):
    locsan = "./PNGFIL"
    # time.sleep(1)
    moveTo_ = pyautogui.locateCenterOnScreen(f"{locsan}/{image}", confidence=0.80)
    pyautogui.moveTo(moveTo_, duration=0.20)
    pyautogui.dragRel(0,dragRel, )
    pyautogui.click()
    locate_leftClick(image=okPNG, confide_=0.90, clicks_=1)
    pyautogui.click()
    print(moveTo_, "tag_click", time_())


def Planning_Templates(image):
    Planning_Templates = locate_rightClick(image=image, confide_=0.80, clicks_=1)
    print(f"{image}/{Planning_Templates}", "Planning_Templates", time_())
def ROUND(image):
    Planning_Templates(image="Planning_Templates.PNG")
    ROUND = locate_leftClick(image=image, confide_=0.80, clicks_=1)
    time.sleep(1)
    sawless(image="sawless.PNG")
    ResultComparison(image="ResultComparison.PNG")
    group_Name_selet(image="group_Name.PNG")
    tag_click(image="Tag_click.PNG", dragRel=120, okPNG="ok.PNG")
    print(f"{image} / {ROUND}", "ROUND", time_())
    time_difference_seconds(start_time=start_time)
def PEAR(image):
    Planning_Templates(image="Planning_Templates.PNG")
    PEAR = locate_leftClick(image=image, confide_=0.80, clicks_=1)
    time.sleep(1)
    sawless(image="sawless.PNG")
    ResultComparison(image="ResultComparison.PNG")
    group_Name_selet(image="group_Name.PNG")
    tag_click(image="Tag_click.PNG", dragRel=160, okPNG="ok.PNG")
    print(f"{image}/{PEAR}", "PEAR", time_())
    time_difference_seconds(start_time=start_time)
def OVAL(image):
    Planning_Templates(image="Planning_Templates.PNG")
    OVAL = locate_leftClick(image=image, confide_=0.80, clicks_=1)
    time.sleep(1)
    sawless(image="sawless.PNG")
    ResultComparison(image="ResultComparison.PNG")
    group_Name_selet(image="group_Name.PNG")
    tag_click(image="Tag_click.PNG", dragRel=180, okPNG="ok.PNG")
    print(f"{image} / {OVAL}", "MARQUISE", time_())
    time_difference_seconds(start_time=start_time)
def MARQUISE(image):
    Planning_Templates(image="Planning_Templates.PNG")
    PEAR = locate_leftClick(image=image, confide_=0.80, clicks_=1)
    time.sleep(1)
    sawless(image="sawless.PNG")
    ResultComparison(image="ResultComparison.PNG")
    group_Name_selet(image="group_Name.PNG")
    tag_click(image="Tag_click.PNG", dragRel=160, okPNG="ok.PNG")
    print(f"{image}/{PEAR}", "PEAR", time_())
    time_difference_seconds(start_time=start_time)



def makebal(image):
    # time.sleep(1)
    makebal =locate_leftClick(image=image, confide_=0.50, clicks_=1)
    pyautogui.dragRel(0, 50, )
    print(makebal, "makebal", time_())
def flip(image):
    makebal(image="makebal.PNG")
    # time.sleep(1)
    flip =locate_leftClick(image=image, confide_=0.50, clicks_=1)
    pyautogui.dragRel(0, 50, )
    print(flip, "flip", time_())
def alert_mgs():
    count_alert = 0
    while count_alert < 1:
        time_end = time_difference_seconds(start_time=start_time)
        pyautogui.alert(f'MANOJ KUKANA \nTime difference \nseconds/{time_end}/ alert box')
        count_alert = count_alert + 1
        # time.sleep(1)
def pant_1_2_3():


    PEAR(image="PEAR.PNG")
    MARQUISE(image="MARQUISE.PNG")
    ROUND(image="ROUND.PNG")
    OVAL(image="OVAL.PNG")


    multiplan(image="multiplan.PNG")
    bestpair(image="bestpair.PNG")
    suggestion_all(image="group_Name.PNG", okPNG="ok.PNG")
    scroll_click(image="scroll_click.PNG", clicks=55)
    sawless(image="sawless.PNG")
    ResultComparison(image="ResultComparison.PNG")
    group_Name_selet(image="group_Name.PNG")
    tag_click(image="Tag_click.PNG", dragRel=43, okPNG="ok.PNG")
    time_difference_seconds(start_time=start_time)

    scroll_click(image="scroll_click.PNG", clicks=55)
    scroll_dwon_click(image="scroll_dwon_click.PNG", clicks=2)
    sawless(image="sawless.PNG")
    ResultComparison(image="ResultComparison.PNG")
    group_Name_selet(image="group_Name.PNG")
    tag_click(image="Tag_click.PNG", dragRel=50, okPNG="ok.PNG")
    time_difference_seconds(start_time=start_time)

    scroll_click(image="scroll_click.PNG", clicks=90)
    scroll_dwon_click(image="scroll_dwon_click.PNG", clicks=4)
    sawless(image="sawless.PNG")
    ResultComparison(image="ResultComparison.PNG")
    group_Name_selet(image="group_Name.PNG")
    tag_click(image="Tag_click.PNG", dragRel=75, okPNG="ok.PNG")
    time_difference_seconds(start_time=start_time)
def pant_4_5():
    scroll_click(image="scroll_click.PNG", clicks=150)
    scroll_dwon_click(image="scroll_dwon_click.PNG", clicks=6)
    sawless(image="sawless.PNG")
    ResultComparison(image="ResultComparison.PNG")
    group_Name_selet(image="group_Name.PNG")
    tag_click(image="Tag_click.PNG", dragRel=80, okPNG="ok.PNG")
    time_difference_seconds(start_time=start_time)
    scroll_click(image="scroll_click.PNG", clicks=150)
    time.sleep(2)
    scroll_dwon_click(image="scroll_dwon_click.PNG", clicks=8)
    sawless(image="sawless.PNG")
    ResultComparison(image="ResultComparison.PNG")
    group_Name_selet(image="group_Name.PNG")
    tag_click(image="Tag_click.PNG", dragRel=100, okPNG="ok.PNG")
    (time_difference_seconds(start_time=start_time))
def pant_1_2_3_4_5():
    pant_1_2_3()
    pant_4_5()
    (time_difference_seconds(start_time=start_time))
def breakpoin_():
    breakpoint()
def makeba_flip():
    makebal(image="makebal.PNG")
    sawless(image="sawless.PNG")
    ResultComparison(image="ResultComparison.PNG")
    group_Name_selet(image="group_Name.PNG")
    tag_click(image="Tag_click.PNG", dragRel=120, okPNG="ok.PNG")
    time_difference_seconds(start_time=start_time)
    flip(image="flip.PNG")
    sawless(image="sawless.PNG")
    ResultComparison(image="ResultComparison.PNG")
    group_Name_selet(image="group_Name.PNG")
    tag_click(image="Tag_click.PNG", dragRel=140, okPNG="ok.PNG")
    time_difference_seconds(start_time=start_time)
def Advisor_Auto_SEVE_OPNE(image, clicks):
    time.sleep(2)
    Advisor_Auto_SEVE_OPNE = locate_leftClick(image=image, confide_=0.80, clicks_=clicks)
    time.sleep(2)
    none_valu(image="Comment.PNG", confide_=0.80)
    moveTo_ = none_valu(image="selet_opne_FILE.PNG", confide_=0.95)
    time.sleep(1)
    pyautogui.moveTo(moveTo_, duration=0.10)
    pyautogui.move(10,25)
    pyautogui.click(clicks=1)
    time.sleep(1)
    pyautogui.click(clicks=2)
    print(Advisor_Auto_SEVE_OPNE, "Advisor_Auto_SEVE_OPNE", time_())
def multi_png(image):
    locsan = "./PNGFIL"
    moveTo_ = pyautogui.locateCenterOnScreen(f"{locsan}/{image}", confidence=0.90)
    while moveTo_ is None:
          list =["Bodrline.PNG","processor_end.png","Finalize.PNG","Haf_damond.PNG",]
          for  imagelist in list:
               time.sleep(1)
               print(moveTo_, "multi_PNG", time_())
               moveTo_ = pyautogui.locateCenterOnScreen(f"{locsan}/{imagelist}", confidence=0.90)
    else:
          time.sleep(1)
          pyautogui.moveTo(moveTo_, duration=0.10)
          locate_leftClick(image="makebal.PNG", confide_=0.50, clicks_=1)
          print(f'{image}', "NOT multi_png", time_())
    return moveTo_
def Delete_ALL_non_seleted(image):
    time.sleep(1)
    plan_total.clear()
    Delete_ALL_non_seleted = multi_png(image="processor_end.png")
    pyautogui.dragRel(0, 50, )
    pyautogui.click()
    time.sleep(1)
    locate_rightClick(image="processor_end.png", confide_=0.90, clicks_=1)
    time.sleep(1)
    locate_leftClick(image="Delete_ALL_non_seleted.png", confide_=0.95, clicks_=1)
    time.sleep(1)
    locate_leftClick(image="YSE_ENTER.PNG", confide_=0.80, clicks_=1)
    print(Delete_ALL_non_seleted, "Delete_ALL_non_seleted", time_())
Auto_cunt = 0
def Advisor_Auto_planning(Auto_cunt_panig=10):
    global time_end , Auto_cunt
    Auto_cunt = 0
    while Auto_cunt < Auto_cunt_panig:
        Auto_cunt = Auto_cunt + 1
        Delete_ALL_non_seleted(image="makebal.PNG")
        pant_1_2_3()
        # pant_4_5()
        # makeba_flip()
        Advisor_Auto_SEVE_OPNE(image="seve.PNG", clicks=1)
        print(time_difference_seconds(start_time=start_time))
    time_difference_seconds(start_time=start_time)
def time_difference_seconds(start_time):
    global Average_plan_par_Time , Average_All_Atoplanig_total_par_Time,Auto_cunt
    end_time = str(time_())
    t1 = datetime.strptime(start_time, "%H:%M:%S")
    t2 = datetime.strptime(end_time, "%H:%M:%S")
    time_caulet = t2 - t1


    if sum(all_plan_total) == 0:
        Average_plan_par_Time = time_caulet / sum(all_plan_total) + 0.0000001
    else:
        Average_plan_par_Time = time_caulet / sum(all_plan_total)

    if Auto_cunt == 0:
       Average_All_Atoplanig_total_par_Time = time_caulet / 1

    else:
        Average_All_Atoplanig_total_par_Time = time_caulet / (Auto_cunt)
        Average_plan_par_Time = time_caulet / sum(all_plan_total)
    print('                                                              Atoplanig_total     :', Auto_cunt)
    print('                                                              all_plan_totall     :', sum(all_plan_total))
    print('                                                                  plan_totall     :', sum(plan_total))
    print('                                                                   Start time     :', t1.time())
    print('                                                                     End time     :', t2.time())
    print(f"                                            total  Time difference   seconds      :  {time_caulet.total_seconds()}")
    print(f"                                                   Time difference    Miniut      :  {time_caulet}")
    print(f"                               Average  par  plan  Time difference    Miniut      :  {Average_plan_par_Time}")
    print(f"                            Average_All_plan_par_  Time difference    Miniut      :  {Average_All_Atoplanig_total_par_Time}")
    return time_caulet.total_seconds()





# Advisor_Auto_planning(Auto_cunt_panig=10)
#

# pyinstaller -w -F -i "./PNGFIL/Advisor.ico" Advisor_EXE30.py

pant_1_2_3()
# pant_4_5()

root = tkinter.Tk()
root.title("MANOJ KUKANA")
root.geometry("330x400")
root.config(background="#ffffff")
root.resizable(50,50)


# img1 = PhotoImage(file="./PNGFIL/Advisor1.PNG")
# labelimage = Label(root,image =img1,background ="#ffffff",)
# labelimage.pack(pady=(0,0))
# labeltext = Label(root, text="Advisor.5.3", font=("Comic sans MS", 30, "bold"), background="#ffffff",)
# labeltext.place(x=60,y=180)
#
#
# butan1 = Button(root,text="MULTI PLAN 5",bg="black",bd=10,fg="green",font=("Arial Black",10, "bold"), command=pant_1_2_3_4_5)
# butan1.place(x=30,y=240)
# butan2 = Button(root,text="MULTI PLAN 3",bg="black",bd=10,fg="green",font=("Arial Black",10, "bold"), command=pant_1_2_3)
# butan2.place(x=180,y=240)
# butan3 = Button(root,text="MAKEBAL FLIP",bg="black",bd=10,fg="green",font=("Arial Black",10, "bold"), command=makeba_flip)
# butan3.place(x=30,y=300)
# butan4 = Button(root,text="MULTI___3 / 5",bg="black",bd=10,fg="green",font=("Arial Black",10, "bold"),command=pant_4_5)
# butan4.place(x=180,y=300)
# butan5 = Button(root,text="AUTO PLANNING",bg="black",bd=10,fg="green",font=("Arial Black",10, "bold"),command=Advisor_Auto_planning)
# butan5.place(x=100,y=360)

# root.mainloop()
#
# #




# pyinstaller -w -F -i "./PNGFIL/Advisor.ico" Advisor_EXE_4!1!2023.py

# pyinstaller --add-data './PNGFIL/:.'Advisor_EXE_4!1!2023.py

# pyinstaller tikar.py
# pyinstaller tikar


# pip --version
# pip install openCV-python
# pip install pyautogui
# pip install pyinstaller
# pip install pywinauto
# pyinstaller --version
# pip install auto-py-to-exe
# auto-py-to-exe


             # //eerall     kadhvamate   3/1/2023
#     from #_greenlet import _C_API # pylint:disable=no-name-in-module
# ImportError: DLL load failed: The specified module could not be foun
# pip install msvc-runtime