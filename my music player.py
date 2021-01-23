from tkinter import *
from tkinter import filedialog,messagebox
from pygame import mixer
import datetime
from mutagen import mp3
from tkinter.ttk import Progressbar
from PIL import Image,ImageTk

#---------------------------------------------------Geometry part-----------------------------------------------------------------------------------------------------------------------------------
root=Tk()
root.title("Music Player")
root.geometry("800x420+40+40")
root.resizable(False,False)




#--------------------------------------------------Image section---------------------------------------------------------------------------------------------------------------------------------------------
#Play=Button(text="Play").pack()

#Pause=Button(text="Pause").pack()

#Next=Button(text="Next").pack()

#Prev=Button(text="Prev").pack()

#img1=Image.open("D:\Python Practice\login.jpeg")
#ph1=ImageTk.PhotoImage(img1)






#---------------------------------------------------Function Section-----------------------------------------------------------------------------------------------------------------------------------------
def searchmusic():
    try:
        sm=filedialog.askopenfilename(intialdir='D:/',title="Select Audio File",filetype=(("MP3","*.mp3"),("WAV","*.wav")))

    except:
        sm=sm=filedialog.askopenfilename(title="Select Audio File",filetype=(("MP3","*.mp3"),("WAV","*.wav")))

    
    e1.set(sm)

def playmusic():
    lb4.grid()
    lb3.grid()
    root.btn8.grid()
    mixer.music.set_volume(0.4)
    progressvol['value']=40
    progressvol1['text']='40%'
    pm=e1.get()
    mixer.music.load(pm)
    mixer.music.play()
    lb2.configure(text="Playing.......")

    
    song=MP3(pm)
    totalsonglenth=int(song.info.length)
    music['maximum']=totalsonglenth
    end.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglenth))))
    def musiclength():
        currentmusic=mixer.music.get_pos()//1000
        music['value']=currentmusic
        start.configure(text='{}'.format(str(datetime.timedelta(seconds=currentmusic))))
        music.after(2,musiclength)
    musiclength()


def pausemusic():
    mixer.music.pause()
    root.btn3.grid_remove()
    root.btn7.grid()
    lb2.configure(text="Pause......")


def volumup():
    global vol 
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol+0.01)
    progressvol1.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    progressvol['value']=mixer.music.get_volume()*100


def volumdown():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol-0.01)
    progressvol1.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    progressvol['value']=mixer.music.get_volume()*100


def stopmusic():
    mixer.music.stop()
    lb2.configure(text="Stop.......")

def resumemusic():
    mixer.music.unpause()
    root.btn7.grid_remove()
    root.btn3.grid()
    lb2.configure(text="Playing.......")

def mutemusic():
    global currentvolume
    currentvolume=mixer.music.get_volume()
    mixer.music.set_volume(0)
    root.btn8.grid_remove()
    root.btn9.grid()


def immutemusic():
    global currentvolume
    mixer.music.set_volume(currentvolume)
    root.btn9.grid_remove()
    root.btn8.grid()


#---------------------------------------------------Baground----------------------------------------------------------------------------------------------------------------------------------------------
#bg=LabelFrame(root,text="Devloper:-Karamveer Rajput",font=("times new roman",14,"italic bold"),fg="red")
#bg.pack(fill="both",expand="yes",padx=10,pady=10)
#bg.configure(bg="yellow")
root.configure(bg="lightskyblue")

#------------------------------------------------
playbutton=Button(root,text="Play",border=2,command=playmusic,bd=3,width=8,height=2)
playbutton.grid(row=5,column=4)

#----------------------------------------------------End-------------------------------------------------------------------------------------------------------------------------------------------------------
root.mainloop()

#========================================------------+++++++++++++++++++++++++++++++++++++-------------------------============================================================================================