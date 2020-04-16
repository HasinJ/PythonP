from tkinter import *
from tkinter.ttk import Entry,Button,OptionMenu
from PIL import Image,ImageTk
import random
from tkinter import filedialog as tkFileDialog
import os

class Main():
    def __init__(self,parent):
        self.parent=parent
        self.image=StringVar()
        self.grid=IntVar()
        self.createWidgets()

    def createWidgets(self):
        self.mainFrame = Frame(self.parent)
        Label(self.mainFrame,text = 'Sliding Puzzle',font = ('',50)).pack(padx =10,pady=10)
        frame = Frame(self.mainFrame)
        Label(frame,text = 'Image').grid(sticky=W)
        Entry(frame,textvariable = self.image,width=50).grid(row=0,column=1,padx=10,pady=10)
        Button(frame,text='Browse',command=self.browse).grid(row=0,column=2,pady=10,padx=10)
        Label(frame,text = 'Grid').grid(sticky=W)
        OptionMenu(frame,self.grid,*[3,4,5,6,7,8,9,10]).grid(row=1,column=1,padx=10,pady=10)
        frame.pack(padx=10,pady=10)
        Button(self.mainFrame,text='Start',command=self.start).pack(padx=10,pady=10)
        self.mainFrame.pack()
        self.board = Frame(self.parent)
        self.winframe = Frame(self.parent)

    def start(self):
        image = self.image.get()
        grid = self.grid.get()
        if os.path.exists(image):
            self.board=Board()

    def browse(self):
        self.image.set(tkFileDialog.askopenfilename(title='Select Image',filetype = ( ('png File','*.png'),('jpg File','*.jpg') )) )


if __name__=="__main__":
    root = Tk()
    Main(root)
    print('test1')
    root.mainloop()
