# Program Designed to estimate labour costs (Included GUI)
import tkinter as tk
from tkinter import messagebox


# Function to calculate total labour cost
def lab_total():
    try:
        total_cost = float(hour_cost.get()) * float(hour_amount.get())
        tk.Label(main, text="Total Price: " + str(total_cost)).grid(row=4)
    except (OSError, ValueError, TypeError):
        tk.messagebox.showinfo('Error', 'Please Enter A Number!')


# Creating main window
main = tk.Tk()

# Creating label for window
main.title('Labour Estimator')

# Creating entry labels
tk.Label(main, text="Cost Per Hour:").grid(row=0)
tk.Label(main, text="Number Of Hours:").grid(row=1)

# Creating entry fields
hour_cost = tk.Entry(main)
hour_amount = tk.Entry(main)

# Setting fields to zero (Empty values can hold program)
hour_cost.insert(0, "0")
hour_amount.insert(0, "0")

# Attaching entry fields to a grid
hour_cost.grid(row=0, column=1)
hour_amount.grid(row=1, column=1)

# Creating a button to get the info and run the function
tk.Button(main, text="Calculate", command=lab_total).grid(row=3, column=1, sticky=tk.W, pady=4)


main.mainloop()
