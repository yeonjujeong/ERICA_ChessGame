import tkinter

window = tkinter.Tk()
window.title("koreanchess")
window.geometry("360*360)
window. resizable(True, True)

image=tkinter.PhotoImage(file="wall.png")

label = tkinter.Label(window, image = image)
label.pack()

window.mainloop()
