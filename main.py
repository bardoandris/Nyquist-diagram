import cmath as cm
import tkinter as tk
from scipy import signal
import sys
import tkinter as tk

TK_widgets = {}


def input_coeff():
    results = []
    while True:

            matrix_counter = input('Please enter the coefficients of the counter:').strip().split(' ')
            matrix_denominator = input('please enter the coefficients of the denominator ').strip().split(' ')
            break
    for i in range(len(matrix_counter)):
        matrix_counter[i] = float(matrix_counter[i])
    for i in range(len(matrix_denominator)):
         matrix_denominator[i] = float(matrix_denominator[i])
         transfer_func = signal.TransferFunction(matrix_counter, matrix_denominator)
    print(transfer_func)
    return (transfer_func)
    return

def main():
    TK_widgets["rootwindow"] = tk.Tk()
    TK_widgets["counter_label"]  = tk.Label(text="Transfer function counter coefficients")
    TK_widgets["counter_label"].pack()
    TK_widgets["denominator_label"] = tk.Label(text="Transfer function denominator coefficients")
    TK_widgets["denominator_label"].pack()
    TK_widgets["counter_textbox"] = tk.Entry()
    TK_widgets["counter_textbox"].pack()
    TK_widgets["denominator_textbox"] = tk.Entry()
    TK_widgets["denominator_label"].pack()
    TK_widgets["go_button"] = tk.Button(command=input_coeff)
    TK_widgets["rootwindow"].mainloop()
    pass



if __name__ == "__main__":
    main()


