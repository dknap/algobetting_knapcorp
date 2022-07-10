import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from tkinter import Menu

# ========= CONFIG =========

window = tk.Tk()
window.title('AlgoBetting KnapCorp')
window.geometry('900x450')
window.resizable(0, 0)


# Tab Control
tabControl = ttk.Notebook(window)

# Menu

def _quit():
    window.quit()
    window.destroy()
    exit()

def aboutUs():
    mBox.showinfo('About us', 'Software created by KnapCorp\nVisit www.KnapCorp.com for more informations.')

menuBar = Menu(window)
window.config(menu=menuBar)

programMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Program', menu=programMenu)
programMenu.add_command(label='Restart')
programMenu.add_command(label='Exit', command=_quit)

helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label='Tutorial')
helpMenu.add_separator()
helpMenu.add_command(label='About us', command=aboutUs)


# ========= ALGO BETTING =========

# tab1: NORWAY - ELITESERIEN
norwayEliteserien = ttk.Frame(tabControl)
tabControl.add(norwayEliteserien, text='NORWAY Eliteserien')
tabControl.pack(expand=1, fill='both', padx=10, pady=10)

# tab2: SLOVAKIA - FORTUNA LIGA
slovakiaFortunaLiga = ttk.Frame(tabControl)
tabControl.add(slovakiaFortunaLiga, text='SLOVAKIA Fortuna Liga')
tabControl.pack(expand=1, fill='both', padx=10, pady=10)


window.iconbitmap(r'icon.ico')
window.mainloop()