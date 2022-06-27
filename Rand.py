
from tkinter import*

window = Tk()
# add widgets here

txtfld=Entry(window, text="Enter your text here", bd=5)
txtfld.place(x=80, y=150)
window.title('Convert your text to Signal')
window.geometry("300x200+10+20")
window.mainloop()