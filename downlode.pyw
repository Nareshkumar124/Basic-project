from customtkinter import *
from tkinter import filedialog,messagebox,Tk
import requests

class Downloader:
    def __init__(self,name) -> None:
        self.saveTo=''
        self.win=CTk()
        self.win.title(name)
        self.url_label=CTkLabel(self.win,text="Enter URL",font=("Arial",30))
        self.url_label.pack(pady=(50,10))
        self.url_entry=CTkEntry(self.win,width=400,height=35,font=("Arial",18),placeholder_text='Enter URL')
        self.url_entry.pack(pady=(10,0))
        self.save_label=CTkLabel(self.win,text=f"",font=("Arial",15))
        self.save_label.pack()
        self.button_frame=CTkFrame(self.win,fg_color="transparent")
        # self.browse_button=CTkButton(self.button_frame,text="Browse",command=self.browse,height=40)
        # self.browse_button.pack(pady=10,padx=(0,55),side='left')
        self.download_button=CTkButton(self.button_frame,text="Download",command=self.download,height=40,width=300,font=("Arial",15))  #threading.Thread(target=self.download).start
        self.download_button.pack(pady=(0,10))
        self.button_frame.pack(padx=10)
        self.win.geometry('800x300')
        
        self.bar=CTkProgressBar(self.win,width=400)
        self.bar.pack(pady=10)
        self.bar.set(0)
        self.win.mainloop()
    
    def browse(self):
        fileName="newfile"
        if self.url_entry.get()!="":
            fileName=self.url_entry.get().split('/')[-1].split('.')[0]
        fileName=filedialog.asksaveasfilename(initialfile=fileName)
        self.saveTo=fileName
        self.save_label.configure(text=self.saveTo)
        print(self.saveTo)
        
    def download(self):
        self.browse()
        url=self.url_entry.get()
        try:
            response=requests.get(url,stream=True)
        except Exception as e:
            messagebox.showerror("Error",e)
            return
        total_size_in_bytes=int(response.headers.get("content-length"))
        print(total_size_in_bytes)
        block_size=10000

        extension=url.split('?')[0].split('.')[-1]
        print(extension)
        total_download=0
        with open(f"{self.saveTo}.{extension}",'wb') as f:
            for data in response.iter_content(block_size):
                f.write(data)
                total_download+=block_size
                self.bar.set(total_download/total_size_in_bytes)
                # print(self.bar.get())
                self.win.update()
        messagebox.showinfo("Save","Download Complete.")
        self.bar.set(0)
        self.url_entry.delete(0,END)
        self.save_label.configure(text='')
        self.saveTo=""

# https://chromedriver.storage.googleapis.com/114.0.5735.16/chromedriver_win32.zip 
# https://player.vimeo.com/progressive_redirect/playback/778956556/rendition/1080p/file.mp4?loc=external&oauth2_token_id=57447761&signature=01b90b35e5825b6b80c6d3400025611500141bba39ac7b2b059f62d42fe4432d
# https://download.pexels.com/vimeo/816742459/pexels-jorge-zald%C3%ADvar-marroqu%C3%ADn-16343098.mp4?fps=59.9401&width=1920

from threading import Thread
Thread(target=Downloader,args=("Python 4",)).start()
Downloader("pyhton3")