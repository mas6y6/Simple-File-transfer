import tkinter, tkinter.messagebox, tkinter.filedialog
import websockets

fileselected = ""

def selectfiles():
    fileselected = tkinter.filedialog.askopenfilenames()

window = tkinter.Tk()
window.title("Simple File Transfer")
window.geometry("600x500")

window.mainloop()