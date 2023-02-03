from tkinter import *
from tkinter.ttk import *

__version__ = '1.8-pre-release'

class init_gui:
    def __init__(self,root) -> None:
        self.root = root
        self.root = root
        self.width = 1024
        self.height = 512
        self.left = (self.root.winfo_screenwidth() - self.width) / 2
        self.top = (self.root.winfo_screenheight() - self.height) / 2

    def guiset(self):
        self.root.resizable(False,False)
        self.root.title("FTPReader - v{}".format(__version__))
        self.root.geometry("{}x{}+{}+{}".format(int(self.width),int(self.height),int(self.left),int(self.top)))

def init_start()->...:
    '''
    start this main gui
    '''
    root = Tk()
    obj = init_gui(root)
    obj.guiset()
    root.mainloop()

if __name__ == '__main__':
    init_start()