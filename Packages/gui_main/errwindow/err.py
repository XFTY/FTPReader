from tkinter import *



class err:
    def __init__(self) -> None:
        self.__err = Tk()
        self.width = 1024
        self.height = 512
        self.x_way = 10
        self.left = (self.__err.winfo_screenwidth() - self.width) / 2
        self.top = (self.__err.winfo_screenheight() - self.height) / 2
    
    def guiset(self,err):
        self.__err.title(f'ERR : {err}')
        self.__err.geometry("{}x{}+{}+{}".format(int(self.width),int(self.height),int(self.left),int(self.top)))
        self.__err.resizable(False,False)
        self.__err.configure(bg='#272727')
        self.text(err)
        self.__err.mainloop()

    def text(self,err):

        self.err_title = Label(self.__err,text='An error occurred while the FTPReader software was running                                                                                 ',bg='red',fg='white',font=('Arial',17)).place(x=0,y=0)

        self.none_title = Label(self.__err,text='An error occurred while the software was running and need to restart.',bg='#272727',fg='white',font=('Arial',13)).place(x=0,y=42)
        self.none2_title = Label(self.__err,text='If this is the first time you see this message, try restarting the software.',bg='#272727',fg='white',font=('Arial',13)).place(x=0,y=64)
        self.none3_title = Label(self.__err,text='If you see this message again, try to do like this:',bg='#272727',fg='white',font=('Arial',13)).place(x=0,y=86)
        self.none4_title = Label(self.__err,text='Check that the software is installed correctly on your computer, and if not, try reinstalling the software.',bg='#272727',fg='white',font=('Arial',13)).place(x=0,y=140)
        self.none5_title = Label(self.__err,text='Check that the configuration information for this software is set correctly.',bg='#272727',fg='white',font=('Arial',13)).place(x=0,y=162)
        self.none6_title = Label(self.__err,text='Check that the program is compatible with this operating system.',bg='#272727',fg='white',font=('Arial',13)).place(x=0,y=184)
        self.stop_title = Label(self.__err,text='Termination code:',bg='red',fg='white',font=('Arial',13)).place(x=0,y=240)
        self.stop_code = Label(self.__err,text=f'*** STOP : {err}',bg='#272727',fg='white',font=('Arial',13)).place(x=0,y=280)
        self.exit = Label(self.__err,text="Click 'X' to close this window",bg='#272727',fg='white',font=('Arial',13)).place(x=0,y=490)
        #self.text = Button(self.__err,text='twxt').pack(side='top')



def init_start(errs='N/A')->...:
    '''
    start this main gui
    '''
    obj = err()
    obj.guiset(errs)


if __name__ == '__main__':
    init_start('This software has reached End of Service and Support \n To avoid performance and reliability issues, we recommend that you move to a newer version of FTPReader.')
    #init_start()