import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class main_gui(QWidget):

    def __init__(self):
        super().__init__()

        self.guiset()


    def guiset(self):
        self.setGeometry(300, 300, 1000, 500)
        self.setWindowTitle('FTPReader')
        self.button_quitbutton()
        self.center()
        self.show()

    def button_quitbutton(self):
        self.qbutton_quitbutton = QPushButton('退出',self)
        #self.qbutton_quitbutton.clicked.connect(QApplication.instance().quit)
        self.qbutton_quitbutton.clicked.connect(self.button_quit_commamd)
        self.qbutton_quitbutton.resize(self.qbutton_quitbutton.sizeHint())
        self.qbutton_quitbutton.setToolTip('这是一个 <b>退出</b> 按钮')
        self.qbutton_quitbutton.move(10,10)

    def button_quit_commamd(self,):

        reply = QMessageBox.question(self, 'Message',
                    "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                    QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)

        if reply == QMessageBox.StandardButton.Yes:
            sys.exit(QApplication(sys.argv))
            #self.qbutton_quitbutton.clicked.connect(QApplication.instance().quit)
        else: ...
            

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():

    app = QApplication(sys.argv)
    ex = main_gui()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()