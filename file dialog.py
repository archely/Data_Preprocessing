from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    print(file)
    file.close()

window = Tk()
button = Button(text="open",command=openFile)
button.pack()
window.mainloop()