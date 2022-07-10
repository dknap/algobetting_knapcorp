import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from tkinter import Menu

# ========= CONFIG =========

algo = tk.Tk()
algo.title('AlgoBetting KnapCorp / 1.0')
algo.geometry('900x450')
algo.resizable(0, 0)


# Tab Control
tabControl = ttk.Notebook(algo)

# Menu

def _quit():
    algo.quit()
    algo.destroy()
    exit()

def aboutUs():
    mBox.showinfo('About us', 'Software created by KnapCorp\nVisit www.KnapCorp.com for more informations.')

menuBar = Menu(algo)
algo.config(menu=menuBar)

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


algo.iconbitmap(r'C:\Programowanie\Python\learnPy\simple_projects\AlgoBetting KnapCorp 1.0\icon.ico')
algo.mainloop()