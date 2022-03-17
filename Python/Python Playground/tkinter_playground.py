import tkinter

window = tkinter.Tk()
window.title("Tkinter Graphical User Interface")
window.minsize(width=600, height=300)

label = tkinter.Label(font=("Arial", 10, "bold"), text="New Label")
label.pack()


def click_me():
    label["text"] = "Button clicked"
    label["text"] = my_input.get()


button = tkinter.Button(text="Click Me", command=click_me)
button.pack()

my_input = tkinter.Entry()
my_input.pack()

window.mainloop()
