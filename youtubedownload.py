import tkinter as tk
from tkinter import ttk
from tkinter import *
from pytube import YouTube
windows = Tk()

windows.geometry("600x400")
windows.title("Youtube Download")

youtube_entry = Entry(windows, font=("Ariel 20"),bd= 5)
youtube_entry.place(x=50,y=100, height=50, width=500)
def get_youtube():
    youtube_link = youtube_entry.get()
    YouTube(youtube_link).streams.get_audio_only().download()
    caption = YouTube(youtube_link).title.capitalize()
    print(caption)
button = tk.Button(font="Ariel 15",text="İndir",fg="black",command=get_youtube)
button.place(height=50,width=100,x=250,y=200)


windows.mainloop()






























