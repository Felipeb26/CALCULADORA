from math import radians, sin, tan,cos
from tkinter import *

from PySimpleGUI.PySimpleGUI import Btn

janela =Tk()
janela.title("titulo da janela")
janela.geometry("400x300")

Label(janela, text='Qual o ângulo?').grid(row=0, column=0)
texto_pergunta = Entry(janela).grid(row=0, column=1,)
Btn = Button(janela, text="calcular").grid(column=1,row=3)

 


janela.mainloop()