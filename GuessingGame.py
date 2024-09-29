import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from random import *

class GuessingGame(QWidget):
    def __init__(self, parent=None):
        
        QWidget.__init__(self, parent)
        self.setGeometry(250, 250, 500, 450)
        self.setWindowTitle('Guessing Game')
        
        self.rand_num = randint(1,10)
        
        self.combo_char = QComboBox()
        self.combo_char.addItem('mickey')
        self.combo_char.addItem('pluto')
        
        self.combo_color = QComboBox()
        self.combo_color.addItem('red')
        self.combo_color.addItem('blue')
        
        self.combo_color.activated.connect(self.color_display)
        self.combo_char.activated.connect(self.picture_display)
        
        self.pixmap_m = QPixmap('mickey.gif')
        self.pic_label_m = QLabel()
        self.pic_label_m.setPixmap(self.pixmap_m)
        
        self.pixmap_p = QPixmap('pluto.gif')
        self.pic_label_p = QLabel()
        self.pic_label_p.setPixmap(self.pixmap_p)
    
        self.guess_label1 = QLabel('Guess 1:')
        self.pic_label = QLabel('Picture:')
        self.colour_label = QLabel('Colour:')
        
        self.primary_label = QLabel('Guesses:')
        self.primary_label.setFont(QFont('Courier',20,1))
        
        self.secondary_label = QLabel('Interface:')
        self.secondary_label.setFont(QFont('Courier',20,1))
        
        self.guess_num = QLineEdit()
        
        self.empty_label = QLabel('')
        
        self.guess_btn = QPushButton('Guess')
        self.guess_btn.setFont(QFont('Courier',11,2))
        self.guess_btn.clicked.connect(self.check_guess)
        
        self.newgame_btn = QPushButton('New Game')
        self.newgame_btn.setFont(QFont('Courier',11,2))
        self.newgame_btn.clicked.connect(self.new_game)
        
        self.change_btn = QPushButton('Change')
        self.change_btn.setFont(QFont('Courier',11,2))
        self.change_btn.clicked.connect(self.color_display)
        
        self.close_btn = QPushButton('Close')
        self.close_btn.setFont(QFont('Courier',11,2))
        self.close_btn.clicked.connect(self.close_game)
        
        self.grid = QGridLayout() 
        self.grid.addWidget(self.primary_label,0,2)
        self.grid.addWidget(self.secondary_label,15,2)
        #self.grid.addWidget(self.guess_label1,1,2)
        self.grid.addWidget(self.guess_num,13,3)
        self.grid.addWidget(self.combo_char,16,3)
        self.grid.addWidget(self.pic_label,16,2)
        self.grid.addWidget(self.combo_color,17,3)
        self.grid.addWidget(self.colour_label,17,2)
        self.grid.addWidget(self.pic_label_m,1,0)
        #self.grid.addWidget(self.pic_label_p,1,0)
        self.grid.addWidget(self.guess_btn,13,4)
        self.grid.addWidget(self.newgame_btn,18,3)
        self.grid.addWidget(self.change_btn,17,4)
        self.grid.addWidget(self.close_btn,18,2)
        self.setLayout(self.grid)        
        
    def new_game(self):
        a.label(' ')    
    
    def close_game(self):
        sys.exit()
        
    def color_display(self): 
        color = str(self.combo_color.currentText())
        bg_color = QPalette()
        bg_color.setColor(QPalette.Window, QColor(color))
        #bg_color.setAutoFillBackground(True)
        app.setPalette(color)
        
    def picture_display(self):
        pixmap = QPixmap(str(self.combo_char.currentText())+'.gif')
        char_pic = QLabel()
        char_pic.setPixmap(pixmap)
        
    def check_guess(self):   
        guess = int(self.guess_num.text())
        if guess_label1 == self.rand_num:
            self.statusLabel.setText('Correct!')
        elif guess_label1 < self.rand_num:
            self.statusLabel.setText('Too small')
        elif guess_label1 > self.rand_num:
            self.statusLabel.setText('Too big')
        
        if guess_label2 == self.rand_num:
            self.statusLabel.setText('Correct!')
        elif guess_label2 < self.rand_num:
            self.statusLabel.setText('Too small')
        elif guess_label2 > self.rand_num:
            self.statusLabel.setText('Too big')

        if guess_label3 == rand_num:
            self.statusLabel.setText('Correct!')
        elif guess_label3 < self.rand_num:
            self.statusLabel.setText('Too small')
        elif guess_label3 > self.rand_num:
            self.statusLabel.setText('Too big')
            
def main():
    app = QApplication(sys.argv)
    
    my_widget = GuessingGame()
    my_widget.show()
    sys.exit(app.exec_())        
    
main()