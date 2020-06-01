# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

playerX = 0
playerO = 0
turn = 0


class Ui_MainWindow(object):

    def restart(self):
        global turn
        self.P1.setEnabled(True)
        self.P1.setText("")
        self.P2.setEnabled(True)
        self.P2.setText("")
        self.P3.setEnabled(True)
        self.P3.setText("")
        self.P4.setEnabled(True)
        self.P4.setText("")
        self.P5.setEnabled(True)
        self.P5.setText("")
        self.P6.setEnabled(True)
        self.P6.setText("")
        self.P7.setEnabled(True)
        self.P7.setText("")
        self.P8.setEnabled(True)
        self.P8.setText("")
        self.P9.setEnabled(True)
        self.P9.setText("")
        self.spielerAnzeige.setText("Turn: X")

        turn = 0

    def win(self, winner):
        print(f"{winner} gewinnt!")
        global playerX, playerO
        if winner == "X":
            playerX += 1
        else:
            playerO += 1
        self.SpielerO.setText(f"Spieler O: {playerO}")
        self.SpielerX.setText(f"Spieler X: {playerX}")
        self.restart()

        


    def check_winner(self):
        
        if self.P1.text() == self.P2.text() and self.P2.text() == self.P3.text() and self.P1.text() != "":
            self.win(self.P1.text())
        elif self.P4.text() == self.P5.text() and self.P5.text() == self.P6.text() and self.P4.text() != "":
            self.win(self.P4.text())
        elif self.P7.text() == self.P8.text() and self.P8.text() == self.P9.text() and self.P7.text() != "":
            self.win(self.P7.text())
        elif self.P1.text() == self.P4.text() and self.P4.text() == self.P7.text() and self.P1.text() != "":
            self.win(self.P1.text()) 
        elif self.P2.text() == self.P5.text() and self.P5.text() == self.P8.text() and self.P2.text() != "":
            self.win(self.P2.text())
        elif self.P3.text() == self.P6.text() and self.P6.text() == self.P9.text() and self.P3.text() != "":
            self.win(self.P3.text())
        elif self.P1.text() == self.P5.text() and self.P5.text() == self.P9.text() and self.P1.text() != "":
            self.win(self.P1.text())
        elif self.P3.text() == self.P5.text() and self.P5.text() == self.P7.text() and self.P3.text() != "":
            self.win(self.P3.text())
        
            
    def Click(self, button):
        global turn
        if turn % 2 == 0:
            button.setText("X") 
            self.spielerAnzeige.setText("Turn: O")
            button.setEnabled(False)
        else:
            button.setText("O")
            button.setEnabled(False)
            self.spielerAnzeige.setText("Turn: X")
        
        turn += 1
        self.check_winner()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 624)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 40, 401, 419))
        self.gridLayoutWidget.setMinimumSize(QtCore.QSize(120, 135))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.P8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.P8.setMinimumSize(QtCore.QSize(120, 135))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.P8.setFont(font)
        self.P8.setText("")
        self.P8.setObjectName("P8")
        self.gridLayout.addWidget(self.P8, 2, 1, 1, 1)
        self.P8.clicked.connect(lambda: self.Click(self.P8))


        self.P4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.P4.setEnabled(True)
        self.P4.setMinimumSize(QtCore.QSize(120, 135))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.P4.setFont(font)
        self.P4.setText("")
        self.P4.setObjectName("P4")
        self.gridLayout.addWidget(self.P4, 1, 0, 1, 1)
        self.P4.clicked.connect(lambda: self.Click(self.P4))


        self.P1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.P1.setMinimumSize(QtCore.QSize(120, 135))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.P1.setFont(font)
        self.P1.setText("")
        self.P1.setObjectName("P1")
        self.gridLayout.addWidget(self.P1, 0, 0, 1, 1)
        self.P1.clicked.connect(lambda: self.Click(self.P1))


        self.P7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.P7.setMinimumSize(QtCore.QSize(120, 135))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.P7.setFont(font)
        self.P7.setText("")
        self.P7.setObjectName("P7")
        self.gridLayout.addWidget(self.P7, 2, 0, 1, 1)
        self.P7.clicked.connect(lambda: self.Click(self.P7))


        self.P5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.P5.setMinimumSize(QtCore.QSize(120, 135))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.P5.setFont(font)
        self.P5.setText("")
        self.P5.setObjectName("P5")
        self.gridLayout.addWidget(self.P5, 1, 1, 1, 1)
        self.P5.clicked.connect(lambda: self.Click(self.P5))


        self.P2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.P2.setMinimumSize(QtCore.QSize(120, 135))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.P2.setFont(font)
        self.P2.setText("")
        self.P2.setObjectName("P2")
        self.gridLayout.addWidget(self.P2, 0, 1, 1, 1)
        self.P2.clicked.connect(lambda: self.Click(self.P2))


        self.P3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.P3.setMinimumSize(QtCore.QSize(120, 135))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.P3.setFont(font)
        self.P3.setText("")
        self.P3.setObjectName("P3")
        self.gridLayout.addWidget(self.P3, 0, 2, 1, 1)
        self.P3.clicked.connect(lambda: self.Click(self.P3))


        self.P6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.P6.setMinimumSize(QtCore.QSize(120, 135))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.P6.setFont(font)
        self.P6.setText("")
        self.P6.setObjectName("P6")
        self.gridLayout.addWidget(self.P6, 1, 2, 1, 1)
        self.P6.clicked.connect(lambda: self.Click(self.P6))


        self.P9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.P9.setMinimumSize(QtCore.QSize(120, 135))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.P9.setFont(font)
        self.P9.setStyleSheet("")
        self.P9.setText("")
        self.P9.setObjectName("P9")
        self.gridLayout.addWidget(self.P9, 2, 2, 1, 1)
        self.P9.clicked.connect(lambda: self.Click(self.P9))


        self.Titel = QtWidgets.QLabel(self.centralwidget)
        self.Titel.setGeometry(QtCore.QRect(150, 0, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Titel.setFont(font)
        self.Titel.setStyleSheet("color: \"black\";\n""")
        self.Titel.setObjectName("Titel")
       
        self.spielerAnzeige = QtWidgets.QLabel(self.centralwidget)
        self.spielerAnzeige.setGeometry(QtCore.QRect(175, 565, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.spielerAnzeige.setFont(font)
       
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(180, 470, 91, 71))
        self.pushButton_10.clicked.connect(lambda: self.restart())
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 70, 73);\n"
"color: \"white\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.SpielerX = QtWidgets.QLabel(self.centralwidget)
        self.SpielerX.setGeometry(QtCore.QRect(30, 470, 111, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SpielerX.setFont(font)
        self.SpielerX.setObjectName("SpielerX")
        self.SpielerO = QtWidgets.QLabel(self.centralwidget)
        self.SpielerO.setGeometry(QtCore.QRect(310, 470, 111, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SpielerO.setFont(font)
        self.SpielerO.setObjectName("SpielerO")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe"))
        self.Titel.setText(_translate("MainWindow", "Tic Tac Toe "))
        self.spielerAnzeige.setText(_translate("MainWindow", "Turn: X"))
        self.pushButton_10.setText(_translate("MainWindow", "Restart"))
        self.SpielerX.setText(_translate("MainWindow", "Player X: 0"))
        self.SpielerO.setText(_translate("MainWindow", "Player O: 0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

