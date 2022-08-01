from cProfile import label
from cgitb import text
from tkinter import *
import webbrowser


def open_Finoana_Git():
    webbrowser.open_new("https://github.com/FinoanaRandria")

root = Tk()

root.title("Premier test interface PY")

root.geometry("1280x720")

root.minsize(480,360)

root.config(background='orange')
#boite frame

frame =Frame(root, bg="orange",bd=1 ,)

#Partie texte

texto = Label(frame,text ="Mon Git", font=("courrier",40),bg="Orange",fg="white")

texto.pack()

texto2 = Label(frame,text ="Tout chose a forcement un debut?", font=("courrier",40),bg="Orange",fg="white")

texto2.pack()

#ajouter  bouton

boutono= Button(frame, text="Ouvrir" ,font=("courrier",25),bg="white",fg="orange",command=open_Finoana_Git)

boutono.pack(pady=25,fill=X)





frame.pack(expand=YES)


root.mainloop()