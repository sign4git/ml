import tkinter

window = tkinter.Tk()
window.title("Tkinter Grid System")
window.minsize(width=600, height=300)

label = tkinter.Label(text="Label")
label.grid(row=0, column=0)

button = tkinter.Button(text="Button")
button.grid(row=1, column=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(row=0, column=2)

entry = tkinter.Entry(text="Entry")
entry.grid(row=2, column=3)

window.mainloop()