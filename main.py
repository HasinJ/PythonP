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
        Label(frame,text = 'Grid').grid(sticky=W)
        OptionMenu(frame,self.grid,*[3,4,5,6,7,8,9,10]).grid(row=1,column=1,padx=10,pady=10)
        frame.pack()
        self.mainFrame.pack()
        self.board = Frame(self.parent)
        self.winframe = Frame(self.parent)


if __name__=="__main__":
    root = Tk()
    Main(root)
    root.mainloop()
