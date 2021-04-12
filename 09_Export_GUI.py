from tkinter import *
from functools import partial

import random


class Converter:
    def __init__(self):

        # Formatting variable...
        background_color = "light blue"

        # In actual program this is blank and is populated with user calculations
        self.all_calc_list = ['0 degrees F is -17.8 degrees C',
                              '0 degrees C is 32 degrees F',
                              '40 degrees C is 104 degrees F',
                              '40 degrees F is 4.4 degrees C',
                              '24 degrees C is 75.2 degrees F',
                              '100 degrees F is 37.8 degrees F']
        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
