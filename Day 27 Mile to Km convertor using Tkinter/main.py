from tkinter import *


def mile_to_km():
    miles = float(input_data.get())
    km = miles * 1.609
    rounded_km = round(km, 2)
    output_label.config(text=f"{rounded_km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=200)
window.config(padx=30, pady=30)

is_equal_label = Label(text="is equal to", font=("Arial", 14, "normal"))
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10, pady=10)

input_data = Entry(width=10, font=("Arial", 14, "normal"))
input_data.grid(column=1, row=0)

output_label = Label(text="0", font=("Arial", 14, "normal"))
output_label.grid(column=1, row=1)

button = Button(text="Calculate", font=("Arial", 14, "normal"), command=mile_to_km)
button.grid(column=1, row=2)

mile_label = Label(text="Miles", font=("Arial", 14, "normal"))
mile_label.grid(column=2, row=0)
mile_label.config(padx=10, pady=10)

km_label = Label(text="Km", font=("Arial", 14, "normal"))
km_label.grid(column=2, row=1)

window.mainloop()
