import tkinter
m = tkinter.Tk()
m.title("Hello World")
label = tkinter.Label(m, text="Hello, World!")
label.pack()
m.geometry("200x100")
m.button = tkinter.Button(m, text="Close", command=m.destroy)
m.button.pack()
m.mainloop()
