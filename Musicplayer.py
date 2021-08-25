import tkinter as tk
import pygame
import os
from tkinter.filedialog import askdirectory

musicplayer = tk.Tk()                          #creating window
musicplayer.title("Mp3 Music Player")          #set title for window
musicplayer.geometry("450x450")                #set geometry for window


directory = askdirectory()                     #asking for music directory
os.chdir(directory)                            #setting music directory to current working directory

songlist = os.listdir()                        #creating songlist using os.listdir() which returns list containing the names of entries in the directory
playlist = tk.Listbox(musicplayer,font = "Cambria 14 bold",bg="cyan2",selectmode=tk.SINGLE)  #adding songs to playlist
for song in songlist :
    pos=0
    playlist.insert(pos,song)
    pos = pos+1

#initializing pygame modules
pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()

def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

Button_stop = tk.Button(musicplayer,height=3,width=5,text="Play Music",font="Cambria 14 bold",command=play,bg="green",fg="black")
Button_stop.pack(fill="x")

Button_stop = tk.Button(musicplayer,height=3,width=5,text="Exit Music Player",font="Cambria 14 bold",command=ExitMusicPlayer,bg="red",fg="black")
Button_stop.pack(fill="x")

Button_pause = tk.Button(musicplayer,height=3,width=5,text="Pause Music",font="Cambria 14 bold",command=pause,bg="yellow",fg="black")
Button_pause.pack(fill="x")

Button_resume = tk.Button(musicplayer,height=3,width=5,text="Resume Music",font="Cambria 14 bold",command=resume,bg="blue",fg="black")
Button_resume.pack(fill="x")

playlist.pack(fill="both",expand="yes")

var = tk.StringVar()
songtitle = tk.Label(musicplayer,font="Cambria 14 bold",textvariable=var)
songtitle.pack()

musicplayer.mainloop()