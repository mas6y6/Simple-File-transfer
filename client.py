import tkinter, tkinter.messagebox, tkinter.filedialog
import tkinter.ttk as ttk
import websockets

window = tkinter.Tk()
window.title("Simple File Transfer")
window.geometry("600x500")
fsvar = tkinter.StringVar(value="None")
fileselected = ""

def selectfiles():
    global fileselected
    fileselected = tkinter.filedialog.askopenfilenames()
    if fileselected == "":
        fsvar.set("None")
    else:
        fsvar.set("")
        for i in fileselected:
            fsvar.set(fsvar.get()+f"\"{i}\"\n")

mainframe = ttk.Frame(window)
def intro():
    global mainframe
    mainframe.destroy()
    mainframe = ttk.Frame(window)
    
    l1 = ttk.Label(mainframe,text="Simple File Transfer")
    l1.pack()
    
    fileselectionframe = ttk.Frame(mainframe)
    l3 = ttk.Label(fileselectionframe,text="File selection:")
    l3.pack(side="left")
    b1 = ttk.Button(fileselectionframe,command=selectfiles,text="Select")
    b1.pack(side="left", padx=5)
    l2 = ttk.Label(fileselectionframe,textvariable=fsvar)
    l2.pack(side="right",padx=5)
    fileselectionframe.pack()
    
    mainframe.pack()

intro()
window.mainloop()