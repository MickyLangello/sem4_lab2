from tkinter import *

def show(*args):
    fio.place(x = 160, y = 35)
    
def hide(*args):
    fio.place_forget()

def SMALL():
    fio['font'] = "Verdana 6"
        
def small():
    fio['font'] = "Verdana 8"

def normal():
    fio['font'] = "Verdana 10"

def big():
    fio['font'] = "Verdana 12"

def BIG():
    fio['font'] = "Verdana 16"

root = Tk()
root.resizable(0, 0)
root.geometry('540x100')
root['bg'] = 'pink'
root.title('Лабораторная работа №2')
img1 = 0
img2 = 0

mainMenu = Menu( root )
root.config(menu = mainMenu)

fio = Text(root, width = 25, height = 1)
fio.insert(0.0,'Богданов Максим 19-ИЭ-1')
fio['state'] = 'disabled'

img1 = PhotoImage(file = '1.gif')
img2 = PhotoImage(file = '2.gif')
        
tip = Menu(mainMenu,tearoff = 0)
guitars = Menu(tip, tearoff = 0)
best = Menu(guitars, tearoff = 0)
size = Menu(mainMenu, tearoff = 0)
bad = Menu(best,tearoff = 0)
gryzDOWN = Menu(best,tearoff = 0)
tmn = IntVar()
opt = Menu(mainMenu, tearoff = 0)

tip.add_cascade(label = 'Электромузыкальные', menu = guitars)
tip.add_command(label = 'Клавишные', command = hide)
tip.add_command(label = 'Ударные')
tip.add_command(label = 'Духовые')

guitars.add_command(label = 'FENDER SQUIER MM')
guitars.add_command(label = 'IBANEZ GRX70QA-TRB')
guitars.add_command(label = 'FENDER SQUIER BULLET STRAT HT HSS BLK')
guitars.add_command(label = 'FENDER SQUIER BULLET TREM')
guitars.add_command(label = 'FENDER SQUIER AFFINITY TELECASTER')
guitars.add_cascade(label = 'Лучшие', menu = best)

bad.add_command(label = 'SCHECTER BANSHEE GT FR S.TR')
bad.add_command(label = 'SCHECTER HELLRAISER C-7 BCH')
gryzDOWN.add_command(label = 'ARIA STG-003SPL 3TS')
gryzDOWN.add_command(label = 'CORT G110-2T')

size.add_checkbutton(label = "Очень маленький", variable = tmn, onvalue  = 2, offvalue=0,command = SMALL)
size.add_checkbutton(label = "Маленький", variable = tmn, onvalue  = 1, offvalue = 0,command = small)
size.add_checkbutton(label = "Обычный", variable = tmn, onvalue  = 0, offvalue = 0,command = normal)
size.add_checkbutton(label = "Большой", variable = tmn, onvalue  = 3, offvalue = 0,command = big)
size.add_checkbutton(label = "Очень большой", variable = tmn, onvalue  = 4, offvalue = 0,command = BIG)
fio.bind("<Button-3>", lambda event: size.post(event.x_root, event.y_root))

opt.add_command(label = "Показать надпись",image = img1, compound = 'left', command = show, accelerator = 'Cntr+Q')
opt.add_command(label = 'Скрыть надпись',image = img2, compound = 'left', command = hide, accelerator = 'Cntr+W')

mainMenu.add_cascade(label = "Муз. инструменты", menu = tip)
mainMenu.add_cascade(label = "Размер надписи", menu = size)
mainMenu.add_command(label = "Машины ")
root.bind('<Control-q>', show)
mainMenu.add_command(label = "Самолеты")
root.bind('<Control-w>',hide)
mainMenu.add_cascade(label = "Помощь", menu = opt)

best.add_cascade(label = 'Дорогие', menu = bad)
best.add_cascade(label = 'Дешевые', menu = gryzDOWN)

root.mainloop()

