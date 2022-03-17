import tkinter

MILES = "Miles"
KM = "Km"
EQUAL = "is equal to"
FONT = ("Arial", 10, "bold")


def calculate_miles_to_km():
    kms = float(entry.get()) * 1.609
    km_value.config(text=kms)


window = tkinter.Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

entry = tkinter.Entry()
entry.grid(row=0, column=1)
entry.config(width=10)

miles_label = tkinter.Label(text=MILES, font=FONT)
miles_label.grid(row=0, column=2)

equals_label = tkinter.Label(text=EQUAL, font=FONT)
equals_label.grid(row=1, column=0)

km_value = tkinter.Label(text="", font=FONT)
km_value.grid(row=1, column=1)

km_label = tkinter.Label(text=KM, font=FONT)
km_label.grid(row=1, column=2)

calculate_button = tkinter.Button(text="Calculate", command=calculate_miles_to_km, font=FONT)
calculate_button.grid(row=2, column=1)

window.mainloop()
