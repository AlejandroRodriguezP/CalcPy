from tkinter import *

app = Tk()
app.title("CalcPy")


user_input = Entry(app, width =50)
user_input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def numeric_button():
    print("you pressed a numeric button")

# Numeric Buttons
button_0 = Button(app, text=" 0 ", padx=40, pady=20, command=numeric_button).grid(row=4, column=1, columnspan=1)
button_1 = Button(app, text=" 1 ", padx=40, pady=20, command=numeric_button).grid(row=3, column=0, columnspan=1)
button_2 = Button(app, text=" 2 ", padx=40, pady=20, command=numeric_button).grid(row=3, column=1, columnspan=1)
button_3 = Button(app, text=" 3 ", padx=40, pady=20, command=numeric_button).grid(row=3, column=2, columnspan=1)
button_4 = Button(app, text=" 4 ", padx=40, pady=20, command=numeric_button).grid(row=2, column=0, columnspan=1)
button_5 = Button(app, text=" 5 ", padx=40, pady=20, command=numeric_button).grid(row=2, column=1, columnspan=1)
button_6 = Button(app, text=" 6 ", padx=40, pady=20, command=numeric_button).grid(row=2, column=2, columnspan=1)
button_7 = Button(app, text=" 7 ", padx=40, pady=20, command=numeric_button).grid(row=1, column=0, columnspan=1)
button_8 = Button(app, text=" 8 ", padx=40, pady=20, command=numeric_button).grid(row=1, column=1, columnspan=1)
button_9 = Button(app, text=" 9 ", padx=40, pady=20, command=numeric_button).grid(row=1, column=2, columnspan=1)


app.mainloop()