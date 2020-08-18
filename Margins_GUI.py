# Program modified from original Margins.py to include a gui
import tkinter as tk


def total_price():
    while True:
        try:
            margin = float(entry_margin.get())
            margin = margin / 100
            margin = margin + 1
            price = float(entry_price.get())
            total = margin * price
            tk.Label(main, text="Total Price: " + str(total)).grid(row=4)
            break
        except (TypeError, ValueError):
            pass


# Creating main window
main = tk.Tk()

# Creating label for window
main.title('Margin Calculator')

# Creating entry labels
tk.Label(main, text="Margin").grid(row=0)
tk.Label(main, text="Price:").grid(row=1)

# Creating entry fields
entry_margin = tk.Entry(main)
entry_price = tk.Entry(main)

# Setting fields to zero (Empty values can hold program)
entry_margin.insert(0, "0")
entry_price.insert(0, "0")

# Attaching entry fields to a grid
entry_margin.grid(row=0, column=1)
entry_price.grid(row=1, column=1)

# Creating a button to get the info and run the function
tk.Button(main, text="Calculate", command=total_price).grid(row=3, column=1, sticky=tk.W, pady=4)


main.mainloop()