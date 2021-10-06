from random import randint
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        loader=QUiLoader()
        self.ui=loader.load('TicTacToe_game.ui',None)
        self.ui.show()

        self.game=[[None for i in range(3)] for j in range(3)]
        self.game[0][0]=self.ui.btn1
        self.game[0][1]=self.ui.btn2
        self.game[0][2]=self.ui.btn3
        self.game[1][0]=self.ui.btn4
        self.game[1][1]=self.ui.btn5
        self.game[1][2]=self.ui.btn6
        self.game[2][0]=self.ui.btn7
        self.game[2][1]=self.ui.btn8
        self.game[2][2]=self.ui.btn9
        for i in range(3):
            for j in range(3):
                self.game[i][j].clicked.connect(partial(self.show,i,j))
        self.ui.btn_newgame.clicked.connect(self.new_game)
        self.ui.btn_about.clicked.connect(lambda :self.ui.message_game.setText('TicTacToe game made by Amir Hossein Sharifnejad'))
        self.ui.radio_pvc.setChecked(True)
        self.count=0
        self.score_x=0
        self.score_o=0
        self.win=False
        self.equal=0
    def show(self,i,j):

        if self.game[i][j].text()=='':
            if self.ui.radio_pvc.isChecked():
                self.one_player(i,j)
            else: self.two_player(i,j)

        else:
            self.ui.message_game.setText('The place is full')
    def one_player(self,i,j):
        self.game[i][j].setText('X')
        self.game[i][j].setStyleSheet('color:#000; ')
        self.var = 'X'
        self.checked(self.var)
        if self.count!=0:
            while True:
                x = randint(0, 2)
                y = randint(0, 2)
                if self.game[x][y].text() == '':
                    self.game[x][y].setText('O')
                    self.game[x][y].setStyleSheet('color:#c8d6e5; ')
                    self.var='O'
                    break
        self.count+=1
        self.checked(self.var)
    def two_player(self,i,j):
        if self.count % 2 == 0:
            self.game[i][j].setText('X')
            self.game[i][j].setStyleSheet('color:#000; ')
            self.var = 'X'
        else:
            self.game[i][j].setText('O')
            self.game[i][j].setStyleSheet('color:#c8d6e5; ')
            self.var = 'O'
        self.count += 1
        self.checked(self.var)
    def checked(self,var):
        count=0
        for i in range(3):
            for j in range(3):
                if self.game[i][j].text()==var:
                    count+=1
            if count==3:
                self.winner(var)
                count = 0
                break
            count = 0
        for i in range(3):
            for j in range(3):
                if self.game[j][i].text() == var:
                    count += 1
            if count == 3:
                count = 0
                self.winner(var)
            count = 0


        for i in range(3):
            if self.game[i][i].text() == var:
                count+=1
        if count==3:
            self.winner(var)
        count=0

        for i in range(3):
            for j in range(2,-1,-1):
                if self.game[i][j].text()==var:
                    count+=1
                i+=1
            break
        if count==3:
            self.winner(var)
        num=0
        for i in range(3):
            for j in range(3):
                if self.game[i][j].text()!='':
                    num+=1
        if num==9:
            self.ui.message_game.setText('The game equalised')
            self.ui.text_eq.setText(str(self.equal))
            self.reset()
    def winner(self,var):
        if var=='X':
            self.score_x+=1
            self.ui.text_x.setText(str(self.score_x))
        else:
            self.score_o+=1
            self.ui.text_o.setText(str(self.score_o))
        return self.reset()
    def reset(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
        self.count = 0
    def new_game(self):
        self.score_x = 0
        self.score_o = 0
        self.equal=0
        self.ui.text_x.setText('--')
        self.ui.text_o.setText('--')
        self.ui.text_eq.setText('--')
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
        self.count = 0



app=QApplication([])
window=TicTacToe()
app.exec()