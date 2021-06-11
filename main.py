import tkinter
from tkinter import *
from tkinter import font
import random
import threading
import time
import requests

user_entry = None
pts = 0
playagain = None
playagainb = None

import urllib.request

word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
r = long_txt.splitlines()

print(r, response)

tmp = r[random.randint(0, len(r) - 1)]

root = Tk()

root.geometry('700x400')

timer = Canvas(root)


word1 = Canvas(root)
L = Label(word1, text=tmp, font=('default, 40'))
L.pack()

user_input = Canvas(root, highlightthickness=0, relief='ridge')

user_entry = Entry(user_input, font=('default, 20'))
user_input.create_window(200, 140, window=user_entry)

def reset():
    global pts
    global L
    global playagain
    global user_entry
    global playagainb
    global L
    global tmp
    playagain.destroy()
    playagainb.destroy()
    tmp = r[random.randint(0, len(r) - 1)]
    L = Label(word1, text=tmp, font=('default, 40'))
    L.pack()
    pts = 0
    user_entry.focus_set()

def showCanvases():
    global timer
    global word1
    global user_input
    global playButton
    playButton.destroy()
    timer.pack()
    word1.pack()
    user_input.pack()
    user_entry.focus_set()
    threading.Thread(target=countdown).start()

playButton = Button(root, text='play', command=showCanvases, font=('default, 45'))
playButton.pack(pady=50)



def change_word(event=None):
    global L
    global word1
    global r
    global tmp
    global user_entry
    global pts
    print(user_entry.get(), tmp)
    try:
        if user_entry.get() == tmp:
            pts += 1
            tmp = r[random.randint(0, len(r) - 1)]
            L.destroy()
            user_entry.delete(0, END)
            user_entry.insert(0, "")
            L = Label(word1, text=tmp, font=('default, 40'))
            L.pack()
    except:
        user_entry.delete(0, END)
        user_entry.insert(0, "")


root.bind('<Return>', change_word)

def countdown():
    y = 60
    for x in range(y):
        F = Label(timer, text=y)
        F.pack()
        time.sleep(1)
        F.destroy()
        y -= 1
    endGame()
    
def endGame():
    global user_input
    global user_entry
    global L
    global pts
    global playagain
    global playagainb
    
    word1.forget()
    user_input.forget()
    L.destroy()
    pts = str(pts)
    tmp = 'you got ' + pts + ' wpm'

    playagain = Label(root, text = tmp, font=('default, 30'))
    playagain.pack()

    playagainb = Button(root, text='Play again', command=lambda:[reset(), showCanvases()])
    playagainb.pack()






root.mainloop()

