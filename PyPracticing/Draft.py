from tkinter import *
from PIL import ImageTk, Image

window = Tk()

name = Label(window, text='Rapaz Desaparecido!!!', bg='white', fg='blue', font=('Serif', 20))
img = Image.open('ram.png')
logo = ImageTk.PhotoImage(img)
image = Label(window, image=logo)
button = Button(window, text='AJUDAR')
username = Label(window, text='Username', font=('Serif', 12))
inputBox = Entry(window)

name.pack()
image.pack()
button.place(x=130, y=350)
username.pack(side=LEFT)
inputBox.pack(side=RIGHT)
window.mainloop()
