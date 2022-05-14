"""
This file is for the altered assignment no. 7 in the UNO Comp Sci II class with Dr. Owora (completed by Bailey Frank)
"""

import tkinter
from GUI import *


def main():
    window = tkinter.Tk()
    window.geometry('500x300')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
