from PIL import Image
from customtkinter import *
import tkinter.filedialog as fd
from tkinter import messagebox
import threading

class Image2PDF:
    def __init__(self, imagePaths=None) -> None:
        self.images = []
        if imagePaths==None:
            return
        if type(imagePaths) == list:
            self.images.extend(imagePaths)
        else:
            self.images.append(imagePaths)

    def appendImage(self, path):
        if type(path) == list:
            self.images.extend(path)
        else:
            self.images.append(path)


    def data(self):
        return self.images

    def save(self, pdf_path="temp.pdf"):
        bar.start()
        print(self.images)
        self.imagesObjects = [
            Image.open(f)
            for f in self.images
        ]
        self.imagesObjects[0].save(
            pdf_path, "pdf", resolution=100.0,
            save_all=True, append_images=self.imagesObjects[1:]
        )
        bar.stop()
        bar.set(0)
        messagebox.showinfo("PDF",f"Pdf Created\nPath = {pdf_path}")

win = CTk()
# Set the geometry of tkinter frame
win.minsize(700,350)
win.maxsize(700,350)
win.title("Image2PDf")
def showfile(a):
    check=False
    for widget in frame.winfo_children(): #destroy old widget--
            check=True
            widget.destroy()
    for i in a.data():
        l=CTkLabel(master=frame,text=i)
        l.pack(pady=2,padx=2)
    saveButton=CTkButton(master=win,text="Save as Pdf",command=threading.Thread(target=a.save).start)
    print(check)
    if not check:
        saveButton.pack(padx=5,pady=5,fill='both',side="bottom")
    frame.pack(padx=5,pady=5,expand=True,fill="both")

def open_file():
   file = fd.askopenfilenames(parent=win, title='Choose a File')
   a = Image2PDF(list(file))
   showfile(a)

# Add a Label widget
label = CTkLabel(win, text="Select the Button to Open the File")
label.pack(pady=10)

# Add a Button Widget
CTkButton(win, text="Select a File", command=open_file).pack()
frame=CTkScrollableFrame(win)
bar=CTkProgressBar(win)
bar.pack(side='bottom',fill=X,padx=1,pady=1)
bar.set(0)
win.mainloop()