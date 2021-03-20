from tkinter import *

# OKNO
win = Tk()
win.title('Beležka')
win.config(bg="green")
win.geometry("300x415")


# FUNKCIONALNOST
def save():
    file = open('podatki.txt', 'w')
    pridobi = str(text.get(1.0, END))
    file.write(pridobi)
    file.close()
    win.quit()


def show():
    odpri = open('podatki.txt', 'r')
    beri = odpri.read()
    text.insert(END, beri)
    odpri.close()


# OBMOČJE BESEDILA
pozdrav = Label(win, bg='lightblue', text='Vnesi zapiske:')
pozdrav.pack(fill=X)

text = Text(win, font=("Arial", 9))
text.pack()
# GUMBI
zapri = Button(win, text='Zapri', command=save)
zapri.pack(side=BOTTOM)

# ZAGON PROGRAMA
show()
win.mainloop()
