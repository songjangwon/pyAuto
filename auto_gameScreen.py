import pyautogui as pag
import random, time, subprocess
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
# form_class = uic.loadUiType("test0124.ui")[0]
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(575, 246)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(280, 20, 75, 23))
        self.startButton.setObjectName("startButton")
        self.endButton = QtWidgets.QPushButton(self.centralwidget)
        self.endButton.setGeometry(QtCore.QRect(280, 60, 75, 23))
        self.endButton.setObjectName("endButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 61))
        self.label.setObjectName("label")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(60, 10, 141, 61))
        self.status.setObjectName("status")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "시작"))
        self.endButton.setText(_translate("MainWindow", "중단"))
        self.label.setText(_translate("MainWindow", "상태"))
        self.status.setText(_translate("MainWindow", "정지"))
        self.startButton.clicked.connect(self.btn_clicked1)
        self.endButton.clicked.connect(self.btn_clicked2)


    def btn_clicked1(self):
        # QMessageBox.about(self, "message", "start")
        # self.status.setText('진행중,,')
        a = ['./image/allPlayButton.png','./image/autoPlayButton.png','./image/checkButton.png','./image/nextButton.png','./image/screenTouchButton.png','./image/startButton.png','./image/closeButton.png']

        while True:
            for pngName in a:
                i = pag.locateOnScreen(pngName, confidence=0.9)
                if i is not None:
                    time.sleep(random.uniform(1.31242, 5.5487))
                    pag.click(i)





    def btn_clicked2(self):
        # QMessageBox.about(self, "message", "end")
        self.status.setText('중지상태,,')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# while True:
#     x, y = pag.position()
#     print('x: %s, y: %s,' % (x,y))

# def countdown(t):
#     while t:
#         mins,secs = divmod(t, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins,decs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         t-=1
# countdown(63)
# exit()

# def bring_window():
#     time.sleep(0.5)
#     apple="""
#     tell application "BlueStacks"
#         activate
#     end tell
#     """
#     apple = apple.encode()
#     p = subprocess.Popen('osascript', stdin=subprocess.PIPE, stdout=subprocess.PIPE,
#     stderr=subprocess.STDOUT)
#     p.communicate(appe)[0]
#
# bring_window()
# exit()


# start_button = {
#     'top_left' : {
#         'x':1250,
#         'y':920,
#     },
#     'bottom_right': {
#         'x': 1500,
#         'y': 990,
#     }
# }
#
#
# allPlay_button = {
#     'top_left' : {
#         'x':630,
#         'y':840,
#     },
#     'bottom_right': {
#         'x': 1000,
#         'y': 915,
#     }
# }
#
#
# skip_button = {
#     'top_left' : {
#         'x':960,
#         'y':500,
#     },
#     'bottom_right': {
#         'x': 1060,
#         'y': 670,
#     }
# }
#
#
# auto_button = {
#     'top_left' : {
#         'x':1310,
#         'y':65,
#     },
#     'bottom_right': {
#         'x': 1350,
#         'y': 90,
#     }
# }
#
# x_button = {
#     'top_left' : {
#         'x':1480,
#         'y':200,
#     },
#     'bottom_right': {
#         'x': 1514,
#         'y': 230,
#     }
# }
#
#
# next_button = {
#     'top_left' : {
#         'x':1360,
#         'y':850,
#     },
#     'bottom_right': {
#         'x': 1560,
#         'y': 920,
#     }
# }
#
# oneclick_button = {
#     'top_left' : {
#         'x':1130,
#         'y':330,
#     },
#     'bottom_right': {
#         'x': 1280,
#         'y': 500,
#     }
# }
#
# def moveClick(buttom):
#     duration = random.uniform(0.5, 1.5)
#     pag.moveTo(
#         x=random.uniform(buttom['top_left']['x'], buttom['bottom_right']['x']),
#         y=random.uniform(buttom['top_left']['y'], buttom['bottom_right']['y']),
#         duration=duration
#     )
#
#     pag.mouseDown()
#     time.sleep(random.uniform(0.15001, 0.29987))
#     pag.mouseUp()
#     time.sleep(random.uniform(0.31242, 1.5487))
#
#
# count = 1

# while True:
#     print(count)
#     # duration = random.uniform(0.5, 1.5)
#     # pag.moteTo(
#     #     x=random.uniform(combat_button['top_left']['x'],combat_button['bottom_right']['x'] ),
#     #     y=random.uniform(combat_button['top_left']['y'],combat_button['bottom_right']['y'] ),
#     #     duration=duration
#     # )
#     #
#     # pag.mouseDown()
#     # time.sleep(random.uniform(0.15001,0.29987))
#     # pag.mouseUP()
#     # time.sleep(random.uniform(0.31242, 1.5487))
#
#     moveClick(start_button)
#     time.sleep(random.uniform(3.31242, 5.5487))
#     moveClick(start_button)
#     time.sleep(random.uniform(60.31242, 62.5487))
#
#     moveClick(allPlay_button)
#     time.sleep(random.uniform(3.31242, 5.5487))
#
#     moveClick(skip_button)
#     time.sleep(random.uniform(2.31242, 3.5487))
#     moveClick(skip_button)
#     time.sleep(random.uniform(2.31242, 3.5487))
#     moveClick(skip_button)
#     time.sleep(random.uniform(2.31242, 3.5487))
#     moveClick(skip_button)
#     time.sleep(random.uniform(2.31242, 3.5487))
#
#     moveClick(auto_button)
#     time.sleep(random.uniform(3512.31242, 3600.5487))
#
#     moveClick(skip_button)
#     time.sleep(random.uniform(2.31242, 3.5487))
#
#     moveClick(x_button)
#     time.sleep(random.uniform(2.31242, 3.5487))
#
#     moveClick(next_button)
#     time.sleep(random.uniform(2.31242, 3.5487))
#
#     moveClick(oneclick_button)
#     time.sleep(random.uniform(2.31242, 3.5487))
#
#     moveClick(next_button)
#     time.sleep(random.uniform(10.31242, 20.5487))
#
#     count += 1