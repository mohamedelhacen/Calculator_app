import tkinter as tk
from tkinter import font
from functools import partial

def get_input(entry, arg):
    entry.insert(tk.END, arg)

def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)

def clear(entry):
    entry.delete(0, tk.END)

def calc(entry):
    input_info = entry.get()
    try:
        output = str(eval(input_info.strip()))
    except ZeroDivisionError:
        popupmsg("Cannot divide by 0!")
        output = ""
    except SyntaxError:
        popupmsg("Invalid syntax")
        output = ""
    clear(entry)
    entry.insert(tk.END, output)

def popupmsg(show):
    popup = tk.Tk()
    popup.resizable(0, 0)
    popup.geometry("150x80")
    popup.title("Alert")
    label = tk.Label(popup, text=show)
    label.pack(side="top", fill="x", pady=5, padx=5)
    p1 = tk.Button(popup, text="OK", bg="#DDDDDD", command=popup.destroy)
    p1.pack()

def calculator():
    root = tk.Tk()
    root.title("Calculator App")
    root.resizable(0, 0)

    entry_font = font.Font(size=20)
    entry = tk.Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=4,
               sticky=tk.N + tk.W + tk.S + tk.E, padx=5, pady=5)
    cal_button_bg = 'red'
    num_button_bg = '#ffffff'
    other_button_bg = '#fff000'
    text_fg = 'black'
    button_active_bg = '#C0C0C0'

    num_button = partial(tk.Button, root, fg=text_fg, bg=num_button_bg, padx=10, pady=3,
                         activebackground=button_active_bg)
    cal_button = partial(tk.Button, root, fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                         activebackground=button_active_bg)

    # Numbers
    button0 = num_button(text='0', command=lambda: get_input(entry, '0'))
    button0.grid(row=5, column=0)

    button1 = num_button(text='1', command=lambda: get_input(entry, '1'))
    button1.grid(row=4, column=0)

    button2 = num_button(text='2', command=lambda: get_input(entry, '2'))
    button2.grid(row=4, column=1)

    button3 = num_button(text='3', command=lambda: get_input(entry, '3'))
    button3.grid(row=4, column=2)

    button4 = num_button(text='4', command=lambda: get_input(entry, '4'))
    button4.grid(row=3, column=0)

    button5 = num_button(text='5', command=lambda: get_input(entry, '5'))
    button5.grid(row=3, column=1)

    button6 = num_button(text='6', command=lambda: get_input(entry, '6'))
    button6.grid(row=3, column=2)

    button7 = num_button(text='7', command=lambda: get_input(entry, '7'))
    button7.grid(row=2, column=0)

    button8 = num_button(text='8', command=lambda: get_input(entry, '8'))
    button8.grid(row=2, column=1)

    button9 = num_button(text='9', command=lambda: get_input(entry, '9'))
    button9.grid(row=2, column=2)

    button10 = num_button(text='.', command=lambda: get_input(entry, '.'))
    button10.grid(row=5, column=1)

    # Calculation Symbols
    button11 = cal_button(text='-', command=lambda: get_input(entry, '-'))
    button11.grid(row=3, column=3)

    button12 = cal_button(text='*', command=lambda: get_input(entry, '*'))
    button12.grid(row=2, column=3)

    button13 = cal_button(text='+', command=lambda: get_input(entry, '+'))
    button13.grid(row=4, column=3)

    button14 = cal_button(text='/', command=lambda: get_input(entry, '/'))
    button14.grid(row=1, column=3)

    button18 = cal_button(text='^', command=lambda: get_input(entry, '**'))
    button18.grid(row=5, column=2)

    # Other symbols
    button15 = tk.Button(root, text='<-', bg=other_button_bg, padx=10, pady=3,
                         command=lambda: backspace(entry), activebackground=button_active_bg)
    button15.grid(row=1, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E +tk.W)

    button16 = tk.Button(root, text='C', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                         command=lambda: clear(entry), activebackground=button_active_bg)
    button16.grid(row=1, column=2)

    button17 = tk.Button(root, text='=', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                         command=lambda: calc(entry), activebackground=button_active_bg)
    button17.grid(row=5, column=3)

    root.mainloop()

if __name__ == '__main__':
    calculator()