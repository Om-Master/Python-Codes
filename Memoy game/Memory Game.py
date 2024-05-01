'''
10. Memory Game:
Description: Implement a memory game where users match pairs of cards.
Features:
Generate a grid of cards.
Flip cards to find matching pairs.
Keep track of the number of moves and time.
'''
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import random
from PyQt5.QtCore import Qt,QTimer
from victory import *
from context import *
from PyQt5.QtGui import QCursor

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.active = True
        self.win = 0

        self.list1 = ["card/burger.jpg", "card/cake.jpg", "card/chips.jpg", "card/donut.jpg", "card/drink.jpg",
                      "card/fries.jpg", "card/ice-cream.jpg", "card/pastry.jpg", "card/pizza.jpg", "card/sandwich.jpg",
                      "card/hi (7).jpg", "card/hi (8).jpg", "card/hi (9).jpg", "card/hi (10).jpg", "card/hi (1).jpg",
                      "card/hi (2).jpg", "card/hi (3).jpg", "card/hi (4).jpg", "card/hi (5).jpg", "card/hi (6).jpg",
                      ]
        self.copy = ["card/burger.jpg", "card/cake.jpg", "card/chips.jpg", "card/donut.jpg", "card/drink.jpg",
                     "card/fries.jpg", "card/ice-cream.jpg", "card/pastry.jpg", "card/pizza.jpg", "card/sandwich.jpg",
                     "card/hi (7).jpg", "card/hi (8).jpg", "card/hi (9).jpg", "card/hi (10).jpg", "card/hi (1).jpg",
                     "card/hi (2).jpg", "card/hi (3).jpg", "card/hi (4).jpg", "card/hi (5).jpg", "card/hi (6).jpg",]
        uic.loadUi("UIs/memory.ui", self)

        self.label = self.findChild(QLabel, "label")
        self.label2 = self.findChild(QLabel, "label2")
        self.label3 = self.findChild(QLabel, "label3")
        self.label4 = self.findChild(QLabel, "label4")
        self.label5 = self.findChild(QLabel, "label5")
        self.label6 = self.findChild(QLabel, "label6")
        self.label7 = self.findChild(QLabel, "label7")
        self.label8 = self.findChild(QLabel, "label8")
        self.label9 = self.findChild(QLabel, "label9")
        self.label10 = self.findChild(QLabel, "label10")
        self.label11 = self.findChild(QLabel, "label11")
        self.label12 = self.findChild(QLabel, "label12")
        self.label13 = self.findChild(QLabel, "label13")
        self.label14 = self.findChild(QLabel, "label14")
        self.label15 = self.findChild(QLabel, "label15")
        self.label16 = self.findChild(QLabel, "label16")
        self.label17 = self.findChild(QLabel, "label17")
        self.label18 = self.findChild(QLabel, "label18")
        self.label19 = self.findChild(QLabel, "label19")
        self.label20 = self.findChild(QLabel, "label20")
        self.button = self.findChild(QPushButton, "restart")

        self.label.setPixmap(QPixmap("cards/back.jpg"))
        self.label2.setPixmap(QPixmap("cards/back.jpg"))
        self.label3.setPixmap(QPixmap("cards/back.jpg"))
        self.label4.setPixmap(QPixmap("cards/back.jpg"))
        self.label5.setPixmap(QPixmap("cards/back.jpg"))
        self.label6.setPixmap(QPixmap("cards/back.jpg"))
        self.label7.setPixmap(QPixmap("cards/back.jpg"))
        self.label8.setPixmap(QPixmap("cards/back.jpg"))
        self.label9.setPixmap(QPixmap("cards/back.jpg"))
        self.label10.setPixmap(QPixmap("cards/back.jpg"))
        self.label11.setPixmap(QPixmap("cards/back.jpg"))
        self.label12.setPixmap(QPixmap("cards/back.jpg"))
        self.label13.setPixmap(QPixmap("cards/back.jpg"))
        self.label14.setPixmap(QPixmap("cards/back.jpg"))
        self.label15.setPixmap(QPixmap("cards/back.jpg"))
        self.label16.setPixmap(QPixmap("cards/back.jpg"))
        self.label17.setPixmap(QPixmap("cards/back.jpg"))
        self.label18.setPixmap(QPixmap("cards/back.jpg"))
        self.label19.setPixmap(QPixmap("cards/back.jpg"))
        self.label20.setPixmap(QPixmap("cards/back.jpg"))

        self.list_label = [self.label, self.label2, self.label3, self.label4, self.label5,
                           self.label6, self.label7, self.label8, self.label9, self.label10,
                           self.label11, self.label12, self.label13, self.label14, self.label15,
                           self.label16, self.label17, self.label18, self.label19, self.label20]
        for i in self.list_label:
            i.mouseDoubleClickEvent = None

        self.label.mousePressEvent = lambda event: self.reveal(self.label, event)
        self.label2.mousePressEvent = lambda event: self.reveal(self.label2, event)
        self.label3.mousePressEvent = lambda event: self.reveal(self.label3, event)
        self.label4.mousePressEvent = lambda event:self.reveal(self.label4, event)
        self.label5.mousePressEvent = lambda event:self.reveal(self.label5, event)
        self.label6.mousePressEvent = lambda event:self.reveal(self.label6, event)
        self.label7.mousePressEvent = lambda event:self.reveal(self.label7, event)
        self.label8.mousePressEvent = lambda event:self.reveal(self.label8, event)
        self.label9.mousePressEvent = lambda event:self.reveal(self.label9, event)
        self.label10.mousePressEvent = lambda event:self.reveal(self.label10, event)
        self.label11.mousePressEvent = lambda event:self.reveal(self.label11, event)
        self.label12.mousePressEvent = lambda event:self.reveal(self.label12, event)
        self.label13.mousePressEvent = lambda event:self.reveal(self.label13, event)
        self.label14.mousePressEvent = lambda event:self.reveal(self.label14, event)
        self.label15.mousePressEvent = lambda event:self.reveal(self.label15, event)
        self.label16.mousePressEvent = lambda event:self.reveal(self.label16, event)
        self.label17.mousePressEvent = lambda event:self.reveal(self.label17, event)
        self.label18.mousePressEvent = lambda event:self.reveal(self.label18, event)
        self.label19.mousePressEvent = lambda event:self.reveal(self.label19, event)
        self.label20.mousePressEvent = lambda event:self.reveal(self.label20, event)
        self.button.clicked.connect(lambda: self.restart1())
        self.mousePressEvent = lambda event: self.context(event)

        self.list2 = []
        self.card_act = True
        self.track = 0

        self.image_dict = {}

        for i in range(len(self.list_label)):
            image1 = random.choice(self.list1)
            self.image_dict[self.list_label[i]] = image1

            self.list1.remove(image1)
        self.show()

    def reveal(self, name, event):
        if event.button() == Qt.LeftButton and self.active:
            name.setPixmap(QPixmap(self.image_dict[name]))
            self.list2.append(self.copy.index(self.image_dict[name]))
            self.list2.append(name)
            self.check(name)

    def check(self,name):
        if len(self.list2) == 4:
            self.active = False
            self.track += 1
            int1 = int(self.list2[0])
            int2 = int(self.list2[2])
            if int1 > int2:
                if int1-int2 == 10:
                    self.delay_true()
                else:
                    self.delay()
            elif int2 > int1:
                if int2-int1 == 10:
                    self.delay_true()
                else:
                    self.delay()

    def delay(self):
        timer = QTimer(self)
        timer.singleShot(1000, lambda: self.back())

    def back(self):
        self.list2[1].setPixmap(QPixmap("cards/back.jpg"))
        self.list2[3].setPixmap(QPixmap("cards/back.jpg"))
        self.list2.clear()
        self.active = True

    def delay_true(self):
        timer = QTimer(self)
        timer.singleShot(1000,lambda :self.clear1())

    def clear1(self):
        self.list2[1].clear()
        self.list2[3].clear()
        self.win += 1
        self.active = True
        self.list2[1].hide()
        self.list2[3].hide()
        self.list2.clear()
        self.victory_screen()

    def restart1(self):
        try:
            self.win = 0
            self.track = 0
            self.list1 = ["card/burger.jpg", "card/cake.jpg", "card/chips.jpg", "card/donut.jpg", "card/drink.jpg",
                      "card/fries.jpg", "card/ice-cream.jpg", "card/pastry.jpg", "card/pizza.jpg", "card/sandwich.jpg",
                      "card/hi (7).jpg", "card/hi (8).jpg", "card/hi (9).jpg", "card/hi (10).jpg", "card/hi (1).jpg",
                      "card/hi (2).jpg", "card/hi (3).jpg", "card/hi (4).jpg", "card/hi (5).jpg", "card/hi (6).jpg",
                      ]
            for i in self.list_label:
                i.show()
                i.setPixmap(QPixmap("cards/back.jpg"))
            self.image_dict = {}

            for i in range(len(self.list_label)):
                image1 = random.choice(self.list1)
                self.image_dict[self.list_label[i]] = image1
                self.list1.remove(image1)
        except Exception as e:
            print(e)
    def victory_screen(self):
        try:
            if self.win == 10:
                with open("score.txt", "r") as f:
                    best = int(f.read())
                if self.track < best:
                    with open("score.txt", "w") as g:
                        g.write(str(self.track))
                        best = self.track
                self.sec = QMainWindow()
                self.second = Ui_secWindow()
                self.second.setupUi(self.sec,self,self.restart1,self.track,best)
                self.sec.show()
                self.hide()
        except Exception as e:
            print(e)

    def context(self,event):
        try:
            if event.button() == Qt.RightButton:
                self.cursor = QCursor()
                cursor_pos = self.cursor.pos()
                self.con_win = QMainWindow()
                self.con = Ui_conWindow()
                self.con.setupUi(self.con)
                self.con_win.setGeometry(cursor_pos.x(),cursor_pos.y(),270,310)
                self.con_win.show()
        except Exception as e:
            print(e)
if __name__ == "__main__":
    app = QApplication([])
    win = window()
    app.exec_()