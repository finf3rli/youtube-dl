import tkinter as tk
from tkinter import *
import code
import threading
from functools import partial

class YoutubeDlGUI():
    def __init__(self):
        self.cmd = code.YoutubeDownloader()
        self.m = tk.Tk()
        Label(self.m, text='URL').grid(row=0)
        self.e1 = Entry(self.m)
        self.e1.grid(row=0, column=1)
        self.button = tk.Button(self.m, text='Fetch', width=25, command=self.buttonClick)
        self.button.grid()
        self.m.mainloop()


    def buttonClick(self):
        self.m = tk.Tk()
        video_title = self.cmd.get_video_name(self.e1.get())
        formats = self.cmd.list_formats(self.e1.get())
        format = formats.split('\n')
        l = Label(self.m, text = video_title.split('\n')[1], font=('Helvetica', 18, 'bold'))
        for item in format[3:]:
            value = item.split()
            try:
                action = partial(self.download, value[0], self.e1.get())
                self.button = tk.Button(self.m, text=value, width=100, command=action)
                l.pack()
                self.button.pack()
            except(IndexError):
                print("")
        self.m.update()
        self.m.mainloop()

    def download(self, index, url):
        thread = threading.Thread(target=self.cmd.download, args=(index, url), daemon=True)
        thread.start()

app = YoutubeDlGUI()