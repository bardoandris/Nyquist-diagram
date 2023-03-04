import cmath as cm
import tkinter as tk
from scipy import signal
import sys
import tkinter as tk

def input_coeff(counter_array, denominator_array):
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
    rootwindow = tk.Tk()
    counter_label = tk.Label(text="Transfer function counter coefficients")
    counter_label.pack()
    denominator_label = tk.Label(text="Transfer function denominator coefficients")
    denominator_label.pack()
    counter_textbox = tk.Entry()
    counter_textbox.pack()
    denominator_textbox = tk.Entry()
    denominator_textbox.pack()
    compute_button = tk.Button(command=lambda: input_coeff(counter_textbox.get(),denominator_textbox.get()))
    rootwindow.mainloop()
    pass



if __name__ == "__main__":
    main()


