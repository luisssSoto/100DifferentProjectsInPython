"""Mile to Kilometers Project"""

import tkinter
FONT = ("Arial", 12)

# Window
my_window = tkinter.Tk()
my_window.title("Mile to Km Converter")
my_window.config(padx=50, pady=50)


# Entry
miles_entry = tkinter.Entry(width=7)
miles_entry.grid(column=1, row=0)

# Label miles
miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

# Label equal to
equal_label = tkinter.Label(text="is equal to: ", font=FONT)
equal_label.grid(column=0, row=1)

# Label amount km
amount_km_label = tkinter.Label(text="0", font=FONT)
amount_km_label.grid(column=1, row=1)

# Label km
km_label = tkinter.Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

def ml_to_km():
    miles = round(float(miles_entry.get()) * 1.60934, 2)
    amount_km_label.config(text=miles)


# Button calculate
calculate_button = tkinter.Button(text="Calculate", command=ml_to_km)
calculate_button.grid(column=1, row=2)



my_window.mainloop()