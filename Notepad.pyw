from customtkinter import *
from tkinter import messagebox,filedialog
from datetime import datetime
import os

class NotePad:
    def __init__(self,winName='Untitled') -> None:
        self.file=None
        self.win=CTk(fg_color='#000000')
        self.win.geometry('1000x600+330+150')
        self.win.title(winName)
        self.buttonFrame=CTkFrame(self.win,fg_color='transparent')

        self.saveButton=CTkButton(self.buttonFrame,command=self.save,text='Save',fg_color='transparent',border_color='#1d1e1e',border_width=2)
        self.saveButton.grid(row=0,column=0,padx=(10,5),pady=5)

        self.openButton=CTkButton(self.buttonFrame,command=self.open,text='Open File',fg_color='transparent',border_color='#1d1e1e',border_width=2)
        self.openButton.grid(row=0,column=1,padx=5,pady=5)


        self.pythonButton=CTkButton(self.buttonFrame,command=self.runPython,text='Python',fg_color='transparent',border_color='#1d1e1e',border_width=2)
        self.pythonButton.grid(row=0,column=2,padx=5,pady=5)

        self.textSize=CTkSlider(self.buttonFrame, from_=10, to=50, command=self.ChangeTextSize)
        self.textSize.grid(row=0,column=3,padx=5,pady=5)
        
        
        self.buttonFrame.pack(padx=2,pady=2,fill=X)
        self.text=CTkTextbox(self.win,font=('Arial',20),fg_color='#222327')
        self.text.pack(padx=10,pady=10,fill='both',expan=True,ipadx=10,ipady=10)
        self.win.mainloop()

    def save(self):
        self.file=filedialog.asksaveasfilename(initialfile='Untitled',defaultextension='txt')
        if self.file:
            data=self.text.get('0.0',END)
            with open(self.file,'w') as f:
                f.write(data)
            self.saveButton.configure(command=self.save2)
            self.win.title(self.file)

    def save2(self):
        data=self.text.get('0.0',END)
        with open(self.file,'w') as f:
                f.write(data)
        
    def open(self):
        self.file=filedialog.askopenfilename(defaultextension='txt')
        if self.file:
            with open(self.file,'r') as f:
                data= f.read()
            self.text.delete('0.0',END)
            self.text.insert('0.0',data)
        self.saveButton.configure(command=self.save2)
        self.win.title(self.file)

    def runPython(self):
        if self.file is not None:
            os.system(f'python {self.file}')

    def ChangeTextSize(self,val):
        self.text.configure(font=('Arial',val))
        
a=NotePad()



