import tkinter.messagebox, tkinter, sys
import tkinter.ttk as ttk
window = tkinter.Tk()
window.title("Simple File Transfer Setup - Intro")
window.geometry("500x400")
mainframe = ttk.Frame(master=window)

def exit():
    if tkinter.messagebox.askyesno("Stop installion?","Do you want to close the installtion?"):
        #!Insert cleanup script here
        sys.exit(0)
    else:
        pass
        
def intro():
    global mainframe
    mainframe.destroy()
    mainframe = ttk.Frame(master=window)
    mainframe.pack(fill="both",expand=True)


intro()
window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", exit)
window.mainloop()