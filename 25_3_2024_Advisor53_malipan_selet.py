from pywinauto import Application
import time


# Easy Way for Beginners to Automate Desktop GUI Applications || Swapy Tool || Python|| pywinauto
# https://www.youtube.com/watch?v=QtJXqF7rf54

# https://www.youtube.com/watch?v=QtJXqF7rf54

# Path to Sarin Advisor 5.3 executable
sarin_path = r"C:\Program Files\Sarin Technologies\Advisor5.3\Advisor.exe"

# Start Sarin Advisor 5.3 application
app = Application().connect(path=sarin_path)

app = app[u'Advisor 5.3 Professional']


# app.print_control_identifiers()
# breakpoint()


# app.menu_select("Stone -> Save")

app.menu_select("Planning -> Makeable")
time.sleep(5)
app.menu_select("Planning -> Multiplan")

time.sleep(5)

app.menu_select("Planning -> Best Pair")
time.sleep(10)







# breakpoint()
# pywinauto.findbestmatch.MatchError: Could not find 'YourDialog' in
# 'dict_keys(['#32770', 'CUIMainViewDlg', 'CUIMainViewDlg#32770',
# 'Sort Group by#32770', '#327700', '#327701', '#327702', 'WndListBox2',
# 'Afx:0000000140000000:0:0000000000000000:0000000001900010:0000000000000000',
# 'WndListBox2Afx:0000000140000000:0:0000000000000000:0000000001900010:0000000000000000',
# 'AfxFrameOrView100', '+/-AfxFrameOrView100', '+/-AfxWnd100', 'AfxWnd100', '+/-AfxWnd1000',
# '+/-AfxWnd1001', '+/-AfxWnd1002', 'AfxWnd1000', 'AfxWnd1001', 'AfxWnd1002', '+/-AfxWnd1003',
# 'AfxWnd1003', '+/-AfxWnd1004', 'AfxWnd1004', 'Dual Viewer 1556183648', 'AfxWnd1005',
# 'Dual Viewer 1556183648AfxWnd100', '#327703', '+/-#32770', '+/-', 'Button', '+/-Button',
# '3D View 1555228544AfxWnd100', '3D View 1555228544', 'AfxWnd1006', 'AfxFrameOrView1000',
# 'AfxFrameOrView1001', 'AfxFrameOrView1002', '+/-AfxFrameOrView1000', '+/-AfxFrameOrView1001',
# '+/-AfxFrameOrView1002', '+/-AfxWnd1005', 'AfxWnd1007', '+/-AfxWnd1006', 'AfxWnd1008',
# '+/-AfxWnd1007', 'AfxWnd1009', '+/-AfxWnd1008', 'AfxWnd10010',
# 'Dual Viewer 1549365264AfxWnd100', 'AfxWnd10011', 'Dual Viewer 1549365264',
# '#327704', '+/-#327700', '+/-#327701', '+/-#327702', '+/-0', '+/-1', '+/-2',
# 'Button0', 'Button1', 'Button2', '+/-Button0', '+/-Button1', '+/-Button2',
# '3D View 1547250208', '3D View 1547250208AfxWnd100', 'AfxWnd10012', 'AfxFrameOrView1003',
# '+/-AfxFrameOrView1003', '+/-AfxWnd1009', 'AfxWnd10013', '+/-AfxWnd10010', 'AfxWnd10014',
# '+/-AfxWnd10011', 'AfxWnd10015', '+/-AfxWnd10012', 'AfxWnd10016',
# 'Dual Viewer 1541487168', 'AfxWnd10017', 'Dual Viewer 1541487168AfxWnd100', '#327705',
# '+/-#327703', '+/-3', 'Button3', '+/-Button3', '3D View 1547249456AfxWnd100',
# '3D View 1547249456', 'AfxWnd10018', 'AfxFrameOrView1004', '+/-AfxFrameOrView1004',
# '+/-AfxWnd10013', 'AfxWnd10019', '+/-AfxWnd10014', 'AfxWnd10020', '+/-AfxWnd10015',
# 'AfxWnd10021', '+/-AfxWnd10016', 'AfxWnd10022', 'Dual Viewer 1477021904AfxWnd100',
# 'AfxWnd10023', 'Dual Viewer 1477021904', '#327706', '+/-#327704', '+/-4', 'Button4',
# '+/-Button4', '3D View 1419143216', 'AfxWnd10024', '3D View 1419143216AfxWnd100'
# 'AfxFrameOrView1005', '+/-AfxFrameOrView1005', '+/-AfxWnd10017', 'AfxWnd10025',
# '+/-AfxWnd10018', 'AfxWnd10026', 'AfxWnd10027', '+/-AfxWnd10019', 'AfxWnd10028',
# 'Dual Viewer 1449285536', 'Dual Viewer 1449285536AfxWnd100', 'AfxWnd10029',
# '#327707', '+/-#327705', '+/-5', 'Button5', '+/-Button5', '3D View 1419145472',
# 'AfxWnd10030', '3D View 1419145472AfxWnd100', 'AfxFrameOrView1006',
# '+/-AfxFrameOrView1006', '+/-AfxWnd10020', 'AfxWnd10031', '+/-AfxWnd10021'
# , 'AfxWnd10032', 'AfxWnd10033', '+/-AfxWnd10022', 'AfxWnd10034',
# 'Dual Viewer 1443324112', 'Dual Viewer 1443324112AfxWnd100',
# 'AfxWnd10035', '#327708', '+/-#327706', '+/-6', 'Button6', '+/-Button6',
# '3D View 1419144720AfxWnd100', 'AfxWnd10036',. '3D View 1419144720',
# 'AfxFrameOrView1007', '+/-AfxFrameOrView1007', '+/-AfxWnd10023', 'AfxWnd10037',
# '+/-AfxWnd10024', 'AfxWnd10038', 'AfxWnd10039', '+/-AfxWnd10025', 'AfxWnd10040',
# 'Dual Viewer 1409260800AfxWnd100', 'Dual Viewer 1409260800', 'AfxWnd10041', '#327709',
# '+/-#327707', '+/-7', 'Button7', '+/-Button7', '3D View 1419143968AfxWnd100',
# '3D View 1419143968', 'AfxWnd10042', 'AfxFrameOrView1008', '+/-AfxFrameOrView1008',
# '+/-AfxWnd10026', 'AfxWnd10043', '+/-AfxWnd10027', 'AfxWnd10044', 'VAfxWnd100',
# 'AfxWnd10045', '+/-AfxWnd10028', 'AfxWnd10046', 'Dual Viewer 1513315808',
# 'AfxWnd10047', 'Dual Viewer 1513315808AfxWnd100', '#3277010', '+/-#327708',
# '+/-8', 'Button8', '+/-Button8', '3D View 1419142464', 'AfxWnd10048',
# '3D View 1419142464AfxWnd100', 'AfxFrameOrView1009', '+/-AfxFrameOrView1009',
# '+/-AfxWnd10029', 'AfxWnd10049', '+/-AfxWnd10030', 'AfxWnd10050', 'VAfxWnd1000',
# 'VAfxWnd1001', 'VAfxWnd1002', 'AfxWnd10051', '+/-AfxWnd10031', 'AfxWnd10052',
# 'Dual Viewer 1446557808', 'AfxWnd10053', 'Dual Viewer 1446557808AfxWnd100',
# '#3277011', '+/-#327709', '+/-9', 'Button9', '+/-Button9', '3D View 1455391904AfxWnd100',
# '3D View 1455391904', 'AfxWnd10054', 'AfxFrameOrView10010', '+/-AfxFrameOrView10010',
# '+/-AfxWnd10032', 'AfxWnd10055', '+/-AfxWnd10033', 'AfxWnd10056', '+/-AfxWnd10034',
# 'AfxWnd10057', '+/-AfxWnd10035', 'AfxWnd10058', 'Dual Viewer 1327623536',
# 'Dual Viewer 1327623536AfxWnd100', 'AfxWnd10059', '#3277012', '+/-#3277010',
# '+/-10', 'Button10', '+/-Button10', '3D View 1455392656AfxWnd100',
# 'AfxWnd10060', '3D View 1455392656', 'MFCGridCtrl', '+/-MFCGridCtrl',


# 'OK', 'Button11', 'OKButton', 'Settings', 'Button12', 'SettingsButton',
# 'PolishDisplay', 'Button13', 'PolishDisplayButton', 'Button14', 'InclusionsDisplay',
# 'InclusionsDisplayButton', 'ResetRough', 'ResetRoughButton', 'Button15', 'Static',
# 'Sort Group byStatic', 'Sort Group by', 'ComboBox', 'Sort Group byComboBox',
# 'VButton', 'Button16', 'V', 'Video', 'VideoButton', 'Button17', 'Button18',
# 'Lock viewes', 'Lock viewesButton', 'CheckBox', 'Show Grid', 'Show GridCheckBox',
# 'ExpAll', 'ExpAllButton', 'Button19', 'Button20', 'ColAll', 'ColAllButton', 'Static0'
# , 'Static1', 'Static2', '+/-Static', 'AfxFrameOrView10011',
# 'Sort Group byAfxFrameOrView100', 'Sort Group byAfxWnd100', 'AfxWnd10061',
# 'ResetRoughAfxWnd100', 'AfxWnd10062', 'ColAllAfxWnd100', 'AfxWnd10063',


# 'SettingsAfxWnd100', 'AfxWnd10064', 'Dual Viewer 1339328416', 'AfxWnd10065',
# 'Dual Viewer 1339328416AfxWnd100', '#3277013', '+/-#3277011', '+/-11', 'Button21',
# '+/-Button11', '3D View 1336022080', 'AfxWnd10066',
# '3D View 1336022080AfxWnd100', '#3277014', '+/-#3277012', '+/-12',
# 'Button22', '+/-Button12', 'Video View 1336332000AfxWnd100', 'AfxWnd10067',
# 'Video View 1336332000'])'




time.sleep(20)



sarin_path = r"C:\Program Files\Sarin Technologies\Advisor5.3\Advisor.exe"

# Start Sarin Advisor 5.3 application




app2 = Application().connect(path=sarin_path)

# app1 = app2[u'Advisor 5.3 Professional']

# app1 = app

# window =app
ctrl = app['AfxWnd10061']  #   suggesion 00
ctrl.DoubleClick()
time.sleep(3)

ctrl = app['AfxWnd10050']  #   suggesion 01
ctrl.DoubleClick()
time.sleep(3)
ctrl = app['AfxWnd10049']  #   suggesion 02
ctrl.DoubleClick()
time.sleep(3)

ctrl = app['AfxWnd10040']  #suggesion 0.3
ctrl.DoubleClick()
time.sleep(3)

ctrl = app['AfxWnd10034']  #suggesion 04
ctrl.DoubleClick()
time.sleep(3)


ctrl = app['AfxWnd10028']    #suggesion 05
ctrl.DoubleClickInput()






#
#
#
#
# ctrl = app['AfxWnd10061']  #   suggesion 00
# ctrl.DoubleClick()
# time.sleep(3)
#
#
#
#
#
#
# ctrl = app['AfxWnd10028']    #   suggesion 05
# ctrl.DoubleClickInput()
#
#
# time.sleep(3)
# ctrl = app['AfxWnd100'] #   suggesion 09
# ctrl.DoubleClick()
#



# app.menu_select("Planning -> SawlessPlanning")



# app.menu_select("Planning -> Best Pair")

# app.menu_select("Planning -> Sawless Planning").Select()
# app.menu_select("Planning -> Makeable")
#
# app.menu_select(u'P&lanning ->&Makeable')

# app.print_control_identifiers()



# app.menu_select(u'P&lanning ->Sawless Planning')


# app.menu_select("Planning -> Sawless Planning")
# window.MenuItem(u'P&lanning->Sawless Planning').Select()
#

# app.menu_select("Stone -> Opne")


# app = app[u'Advisor 5.3 Professional']
#
# # app.menu_select("Stone -> Opne")
# app.MenuItem(u'lanning->Makeable').Select()
# #
# app.menu_select("lanning -> Makeable")


#
# P&lanning



# app.menu_select("Stone -> Opne")
#
#
#
# app.print_control_identifiers()

# Access names : []
# Class : Button
# ClientRects : [<RECT L0, T0, R38, B31>]
# ContextHelpID : 0
# ControlCount : 0
# ControlID : 1056
# ExStyle : 0
# Fonts : [<LOGFONTW 'MS Shell Dlg' -11>]
# FriendlyClassName : Button
# handle : 1638534
# IsEnabled : True
# IsUnicode : False
# IsVisible : False
# MenuItems : []
# pwa_type : <class 'pywinauto.controls.win32_controls.ButtonWrapper'>
# Rectangle : (L-31299, T-31017, R-31261, B-30986)
# Style : 1342177291
# Texts : ['']
# UserData : 0


#
# Access names : [u'AfxWnd10030', u'3D View 1347282880', u'3D View 1347282880AfxWnd100']
# Class : AfxWnd100
# ClientRects : [<RECT L0, T0, R294, B248>]
# ContextHelpID : 0
# ControlCount : 1
# ControlID : 1997
# ExStyle : 0
# Fonts : [<LOGFONTW 'MS Shell Dlg' -11>]
# FriendlyClassName : AfxWnd100
# handle : 983786
# IsEnabled : True
# IsUnicode : False
# IsVisible : True
# MenuItems : []
# pwa_type : <class 'pywinauto.controls.HwndWrapper.HwndWrapper'>
# Rectangle : (L1567, T430, R1861, B678)
# Style : 1442840576
# Texts : [u'3D View 1347282880']
# UserData : 0
