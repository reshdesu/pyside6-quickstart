from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# initialize the app
app = QApplication([])
# create main window
win = QMainWindow()
# add a button
button = QPushButton("quickstart push button")


# callback function for button
def called_button(a):
    print(a)


# connect button to the callback
button.clicked.connect(called_button)

# add the button to the window
win.setCentralWidget(button)

# show the window
win.show()

# execute app
app.exec()
