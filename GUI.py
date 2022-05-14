from tkinter import *
from tkinterwidgets import *


class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_entries = Frame(self.window)
        self.var1= Entry(self.frame_entries, )
        self.var2 = Entry(self.frame_entries)
        self.var1.pack(pady=10)
        self.var2.pack(pady=10)
        self.frame_entries.pack(pady=10)

        self.frame_radios = Frame(self.window)
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_addition = Radiobutton(self.frame_entries, text="Add Up To", variable=self.radio_1, value=0)
        self.radio_exponents = Radiobutton(self.frame_entries, text="Exponentiate", variable=self.radio_1, value=1)
        self.radio_listing = Radiobutton(self.frame_entries, text="List of Numbers To", variable=self.radio_1, value=2)
        self.radio_addition.pack(side='left', padx=10)
        self.radio_exponents.pack(side='left', padx=10)
        self.radio_listing.pack(side='left', padx=10)
        self.frame_radios.pack(padx=10, pady=10)

        self.label = Label(self.window, text='Answer will appear here')
        self.label.pack(pady=10)

        self.frame_button = Frame(self.window)
        self.button_calculate = Button(self.frame_button, text='Calculate', command=self.clicked)
        self.button_calculate.pack(side='bottom', pady=10)
        self.frame_button.pack(side='bottom', padx=10, pady=10)


    def clicked(self):
        """

        This function stores the values entered in the entries and which radio button was selected

        :return: None
        """


        variable1 = int(self.var1.get())
        selection = self.radio_1.get()

        error = "Please use whole numbers greater than 0"

        if variable1 != type(int):
            self.label.config(text=error)

        if selection == 0:
            self.adding(variable1)
        elif selection == 1:
            if self.var2.get() != '':
                try:
                    variable2 = int(self.var2.get())
                    self.exponents(variable1, variable2)
                except:
                    self.label.config(text=error)
        elif selection == 2:
            self.listing(variable1)

        self.var1.delete(0, END)
        self.var2.delete(0, END)


    def adding (self, var1):
        """

        This function accepts any positive whole number and returns the sum of all whole numbers up to and including the variable

        :param var1: the number provided by the user

        :return: None
        """
        total = 0

        while var1 >= 0:
            total += var1
            var1 -= 1
        self.label.config(text=total)


    def exponents(self, var1, var2):
        """

        This function raises a number to a power

        :param var1: the number to be raised to a power
        :param var2: the exponent

        :return: None
        """

        if var1 == 0 and var2 == 0:
            self.label.config(text='1')
        else:
            answer = var1 ** var2
            self.label.config(text=answer)



    def listing(self, var1):
        """

        This function prints out all of the positive whole numbers leading up to that number
        :param var1:

        :return: None
        """

        if var1 == 1:
            self.label.config(text='1')
        else:
            nums = []
            while var1 != 0:
                nums.append(var1)
                var1 -= 1
            self.label.config(text=nums)
