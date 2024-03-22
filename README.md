# Sarin_Advisor53application
Sarin Technologies\Advisor5.3    pywinauto



# Easy Way for Beginners to Automate Desktop GUI Applications || Swapy Tool || Python|| pywinauto
# https://www.youtube.com/watch?v=QtJXqF7rf54

from pywinauto import Application
from pywinauto.findwindows import find_elements
import time

# Path to Sarin Advisor 5.3 executable
sarin_path = r"C:\Program Files\Sarin Technologies\Advisor5.3\Advisor.exe"

# Start Sarin Advisor 5.3 application
# app = Application().start(sarin_path)   or

app = Application().start(sarin_path)

time.sleep(10)  # Wait for 5 seconds to ensure application is fully loaded


# Select Advisor window  [u'Advisor 5.3 Professional                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ']
app = app[u'Advisor 5.3 Professional']

app.menu_select("Stone -> Opne")

app.print_control_identifiers()
