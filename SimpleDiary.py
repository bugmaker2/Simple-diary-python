# -*- coding: UTF-8 -*-
# Name: Simple diary
# Version: 1.0.0 2020-3-13
# Autuor: ColourfulWhite
# QQ: 2742622317

from PyQt5.QtWidgets import QMainWindow,QApplication,\
    QPushButton,QDesktopWidget,QAction,QLineEdit,QTextEdit,\
    QFileDialog,QMessageBox
from PyQt5.QtGui import QIcon
from sys import argv,exit
from time import strftime
from time import localtime
from time import time

class Main_Function(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.buildMenu()
        self.buildWindow()
        self.buildText()
        self.buildButton()
        self.show()


    def buildMenu(self):
        menubar = self.menuBar()

        # File Menu
        fileMenu = menubar.addMenu('File')
        # # open
        openAction = QAction('open',self)
        openAction.triggered.connect(self.open)
        fileMenu.addAction(openAction)
        # # choose path
        chooseAction = QAction('choose path',self)
        chooseAction.triggered.connect(self.choose_path)
        fileMenu.addAction(chooseAction)

        # Help Menu
        helpMenu = menubar.addMenu('Help')
        # # contact author
        # contactAction = QAction('contact author',self)
        # contactAction.triggered.connect(self.contact)
        # helpMenu.addAction(contactAction)
        # # help
        helpAction = QAction('help',self)
        helpAction.triggered.connect(self.help)
        helpMenu.addAction(helpAction)

    # def contact(self):
    #     QMessageBox.about(self,'Contact author',"QQ: 2742622317\nBlog: https://blog.csdn.net/weixin_44226870")

    def help(self):
        QMessageBox.about(self,'Help','open：打开已往日记\nchoose path：永久更改存储文件夹')

    def buildWindow(self):

        self.resize(500,500)
        # get the structure of the main window
        qr = self.frameGeometry()
        # get the resolution
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.setWindowTitle('Simple Diary v1.0.0')
        self.setWindowIcon(QIcon('notes.ico'))


    def buildText(self):
        self.title = QLineEdit(self)
        self.title.setGeometry(100,60,300,30)
        self.content = QTextEdit(self)
        self.content.setGeometry(49,110,400,290)


    def buildButton(self):

        self.btn_clear = QPushButton('Clear',self)
        self.btn_clear.setToolTip('Clear all content.')
        self.btn_clear.resize(self.btn_clear.sizeHint())
        self.btn_clear.move(130,420)
        self.btn_clear.clicked.connect(self.clear)

        self.btn_save = QPushButton('Finish',self)
        self.btn_save.setToolTip('Save all content and close.')
        self.btn_save.resize(self.btn_clear.sizeHint())
        self.btn_save.move(270,420)
        self.btn_save.clicked.connect(self.finish)

        self.show()


    def open(self):
        path, ok1 = QFileDialog.getOpenFileName(self,"选取文件","./","All Files (*);;Text Files (*.txt)")
        self.title.clear()
        self.content.clear()
        f = open(path)
        filename = path.split('/')[-1]   # fine the basename of the file
        filename = filename.split('.')[0]
        self.title.setText(filename)
        self.content.setPlainText(f.read())
        f.close()

    def choose_path(self):
        '''
        open the log and rewrite the path
        '''
        f = open('log.txt','w')
        path = QFileDialog.getExistingDirectory(self, "选择文件夹", "./")
        f.write(path+'/')
        f.close()

    def clear(self):
        '''
        clear all the content of the title and content
        '''
        self.title.clear()
        self.content.clear()

    def finish(self):
        '''
        get title (default is Untitled)
        get content
        read log to get path
        write to the path
        '''
        save_title = self.title.text()
        if save_title == '':
            save_title = 'Untitled'
        save_content = self.content.toPlainText()
        path = open('log.txt','r').read()
        now = strftime("%Y-%m-%d",localtime(time()))
        save_path = path+save_title+" "+now+".txt"
        save_file = open(save_path,'w')
        save_file.write(save_content)
        save_file.close()
        exit()


if __name__ == '__main__':
    app = QApplication(argv)
    GUI = Main_Function()
    exit(app.exec_())
