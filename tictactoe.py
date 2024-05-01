from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton
from PyQt5 import uic

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("UIs/Tic.ui",self)

        self.b1 = self.findChild(QPushButton,"pushButton_1")
        self.b2 = self.findChild(QPushButton,"pushButton_2")
        self.b3 = self.findChild(QPushButton,"pushButton_3")
        self.b4 = self.findChild(QPushButton,"pushButton_4")
        self.b5 = self.findChild(QPushButton,"pushButton_5")
        self.b6 = self.findChild(QPushButton,"pushButton_6")
        self.b7 = self.findChild(QPushButton,"pushButton_7")
        self.b8 = self.findChild(QPushButton,"pushButton_8")
        self.b9 = self.findChild(QPushButton,"pushButton_9")
        self.b10 = self.findChild(QPushButton,"pushButton_10")

        self.b1.clicked.connect(lambda: self.set(self.b1))
        self.b2.clicked.connect(lambda: self.set(self.b2))
        self.b3.clicked.connect(lambda: self.set(self.b3))
        self.b4.clicked.connect(lambda: self.set(self.b4))
        self.b5.clicked.connect(lambda: self.set(self.b5))
        self.b6.clicked.connect(lambda: self.set(self.b6))
        self.b7.clicked.connect(lambda: self.set(self.b7))
        self.b8.clicked.connect(lambda: self.set(self.b8))
        self.b9.clicked.connect(lambda: self.set(self.b9))


        self.b10.clicked.connect(lambda: self.reset())
        self.count = 0

        self.label= self.findChild(QLabel,"label")

        self.show()

    def win(self,a,b,c):
        a.setStyleSheet("QPushButton {color:red}")
        b.setStyleSheet("QPushButton {color:red}")
        c.setStyleSheet("QPushButton {color:red}")
        self.but2 = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]
        for i in self.but2:
            i.setEnabled(False)
        self.label.setText(f"{a.text()} wins!")

    def check(self):
        if self.b1.text() !="" and self.b1.text() == self.b2.text() and self.b1.text() == self.b3.text():
            self.win(self.b1,self.b2,self.b3)

        if self.b4.text() !="" and self.b4.text() == self.b5.text() and self.b4.text() == self.b6.text():
            self.win(self.b4,self.b5,self.b6)
        if self.b7.text() !="" and self.b7.text() == self.b8.text() and self.b7.text() == self.b9.text():
            self.win(self.b7,self.b8,self.b9)

        if self.b1.text() !="" and self.b1.text() == self.b4.text() and self.b1.text() == self.b7.text():
            self.win(self.b1,self.b4,self.b7)
        if self.b2.text() !="" and self.b2.text() == self.b5.text() and self.b2.text() == self.b8.text():
            self.win(self.b2,self.b5,self.b8)
        if self.b3.text() !="" and self.b3.text() == self.b6.text() and self.b3.text() == self.b9.text():
            self.win(self.b3,self.b6,self.b9)

        if self.b1.text() !="" and self.b1.text() == self.b5.text() and self.b1.text() == self.b9.text():
            self.win(self.b1,self.b5,self.b9)
        if self.b3.text() !="" and self.b3.text() == self.b5.text() and self.b3.text() == self.b7.text():
            self.win(self.b3,self.b5,self.b7)
    def set(self,b):
        if self.count %2 == 0:
            b.setText("X")
            self.label.setText("O's Turn")
        else:
            b.setText("O")
            self.label.setText("X's Turn")
        b.setEnabled(False)
        self.count += 1
        self.check()

    def reset(self):
        self.but = [self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8,self.b9]
        for i in self.but:
            i.setEnabled(True)
            i.setText("")
            i.setStyleSheet("QPushButton{color:#797979}")

        self.count = 0
        self.label.setText("X is first!")

if __name__ == "__main__":
    app = QApplication([])
    win = window()
    app.exec_()