import tkinter as tk
from tkinter import END
import os
import threading
import logging
from pynput.mouse import Listener
import threading
import pyautogui as pg


root = tk.Tk()
root.geometry('300x300')


def stoplog():
    logging.shutdown()
    kill = threading.Event()
    pg.hotkey('alt', 'F4')
    
        

def getclicks(event=None):
    with open('MOUSECLICK_log.txt', 'r') as inputfile:
        data = inputfile.read()
        occurrences = data.count('mouse clicks')
        e1 = tk.Entry(root)
        e1.grid(row=0, column=0)
        e1.delete(0, END)
        e1.insert(0, occurrences)



def loggin():
    count = 0

    t1 = threading.Thread(target=loggin, args=[])
    
    desktop = os.path.expanduser('~/Desktop')

    logging.basicConfig(filename = '{0}/MOUSECLICK_log.txt'.format(desktop), level=logging.DEBUG)

    #def on_move(x, y):
    #        logging.info('pyautogui.moveTo(' + str(x) + ', ' + str(y) + ')')

       

    def on_click(x, y, button, pressed):
        nonlocal count
        count=0
        count += 1
        if pressed:
            logging.info('mouse clicks' + str(count) + '\n')
            
        else:
            '======'


    with Listener(on_click=on_click ) as listener:
        listener.join()





##t1.raise_exception() 


btn1 = tk.Button(root, text='get clicks', command=getclicks)
btn1.grid(row=6, column=1)
##t1.join()
btn2 = tk.Button(root, text='start thread', command=threading.Thread(target=loggin).start())
btn2.grid(row=6, column=2)

btn3 = tk.Button(root, text='stop thread', command=stoplog)
btn3.grid(row=6, column=3)

root.bind('<Motion>', getclicks)


root.mainloop()









