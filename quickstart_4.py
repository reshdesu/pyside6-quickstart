"""
This tutorial was all around using the PySide API to import and use the .ui files which we created using the QTDesigner
Video: 
https://youtu.be/xKIPPZMP9y4?si=gIed0kMJkpXMEuZS
"""

# get the class the tutorial has on github
"""
This code has a YouTube video associated with it
https://www.youtube.com/watch?v=xKIPPZMP9y4&list=PLuvCsqbtUSFAEmez6Tuyi2KitVcS4fLWX&index=5
"""
"""
This code has a YouTube video associated with it
https://www.youtube.com/watch?v=xKIPPZMP9y4&list=PLuvCsqbtUSFAEmez6Tuyi2KitVcS4fLWX&index=5
"""
import subprocess
import xml.etree.ElementTree as xml


class PySide6Ui:
    """
    class to load .ui files to memory or
    convert them to .py files

    based on:
    http://stackoverflow.com/a/14195313/3781327

    usage:
    PySide6Ui('myUi.ui').toPy('myUi.py')
    PySide6Ui('myUi.ui').toPy()

    PySide6Ui('myUi.ui').load()
    """

    def __init__(self, ui_file):
        self.__ui_file = ui_file

    def __getUi(self):
        return subprocess.check_output(["pyside6-uic", self.__ui_file])

    def toPy(self, py_file=None):
        py_file = py_file or self.__ui_file.replace(".ui", ".py")
        uipy = self.__getUi()
        try:
            # Write the file
            with open(py_file, "w") as f:
                f.write(uipy.decode("utf-8"))
            return True
        except:
            return False

    def load(self):
        uipy = self.__getUi()
        parsed = xml.parse(self.__ui_file)
        widget_class = parsed.find("widget").get("class")
        form_class = parsed.find("class").text
        pyc = compile(uipy, "<string>", "exec")
        frame = {}
        exec(pyc, frame)
        form_class = frame["Ui_%s" % form_class]
        base_class = eval("%s" % widget_class)  # 'QMainWindow' or 'QWidget'
        return form_class, base_class


# import base classes for pyside6 API
from PySide6.QtWidgets import QApplication, QMainWindow

# initialize the app
app = QApplication([])

# import the UI file into the individual classes
form_class, base_class = PySide6Ui("my_first_qtdesigner_UI.ui").load()

# create main window
win = base_class()
# create form
form = form_class()
form.setupUi(win)
# accessing the existing elements and printing the text within the button
print(form.pushButton.text())
# show the window
win.show()

# execute app
app.exec()
