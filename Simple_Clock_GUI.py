#import modules
from tkinter import *
from tkinter.ttk import *
#import strftime functions to receive system's time
from time import strftime

#create tkinter  window
root = Tk()
root.title('Clock by Sean Talbot')

#this function is used to display time on the label.
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

#Styling the label widget
lbl = Label(root, font = ('lucidia', 40, 'bold'),
            background = 'silver',
            foreground = 'black')

#placing clock in the center of window
lbl.pack(anchor = 'center')
time()
mainloop()
