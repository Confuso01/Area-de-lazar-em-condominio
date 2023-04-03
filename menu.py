# pip install xlrd xlsxwriter openpyxl pandas IPython tkcalendar
from tkinter import *
from tkinter.ttk import *
import pandas as pd

import buscarMorador
import cadastroReserva
import buscarReserva
import buscarArea
import cadastroMorador
import buscarTodasReservas
import buscarTodosCaixas
import buscarTodosMoradores

def abrir_janelaBuscarMorador():
    buscarMorador.janelaBuscarMorador()

def abrir_janelaCadastroReserva():
    cadastroReserva.janelaCadastroReserva()

def abrir_janelaBuscarReserva():
    buscarReserva.janelaBuscarReserva()

def abrir_janelaBuscarArea():
    buscarArea.janelaBuscarArea()

def abrir_janelaCadastroMorador():
    cadastroMorador.janelaCadastroMorador()

def abrir_janelaMostrarTodasReservas():
    buscarTodasReservas.janelaBuscarTodasReservas()

def abrir_janelaCaixa():
    buscarTodosCaixas.janelaCaixa()

def abrir_janelaMoradores():
    buscarTodosMoradores.janelaMoradores()

def menuPrincipal():
    co0 = "#f0f3f5"  # Preta / black
    co1 = "#feffff"  # branca / white
    co2 = "#3fb5a3"  # verde / green
    co3 = "#38576b"  # valor / value
    co4 = "#403d3d"   # letra / letters

    janela = Tk()
    janela.title('')
    janela.geometry('300x500')
    janela.configure(background='#feffff')
    janela.resizable(width=TRUE, height=FALSE)
    janelaEstilo = Style()
    janelaEstilo.configure('my.TButton', font=('Helvetica', 12), width=30)


    frame_cima = Frame(janela, width=300, height=40, relief='flat')
    frame_cima.grid(row=0, column=0, padx=0, pady=1, sticky=NSEW)

    frame_baixo = Frame(janela, width=300, height=460, relief='flat')
    frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)
    frame_baixo.grid_propagate(False)

    #Titulo
    l_cadastro = Label(frame_cima, text='SISTEMA DE CONDOMINIO', anchor=NE, font='Ivy 15').place(x=5, y=5)

    botao1 = Button(frame_baixo, text="Cadastro de morador", style='my.TButton', command=abrir_janelaCadastroMorador)
    botao1.grid(row=0, column=0, padx=14, pady=3, ipady=10, sticky=NSEW)

    botao2 = Button(frame_baixo, text="Cadastro de reserva", style='my.TButton', command=abrir_janelaCadastroReserva)
    botao2.grid(row=1, column=0, padx=14, ipady=10, sticky=NSEW)

    botao3 = Button(frame_baixo, text="Buscar por morador", style='my.TButton',command=abrir_janelaBuscarMorador)
    botao3.grid(row=2, column=0, padx=14, ipady=10, sticky=NSEW)

    botao4 = Button(frame_baixo, text="Buscar por reserva",style='my.TButton', command=abrir_janelaBuscarReserva)
    botao4.grid(row=3, column=0, padx=14, ipady=10, sticky=NSEW)

    botao5 = Button(frame_baixo, text="Buscar por área",style='my.TButton', command=abrir_janelaBuscarArea)
    botao5.grid(row=4, column=0, padx=14, ipady=10, sticky=NSEW)

    botao5 = Button(frame_baixo, text="Mostrar todas as reservas",style='my.TButton', command=abrir_janelaMostrarTodasReservas)
    botao5.grid(row=5, column=0, padx=14, ipady=10, sticky=NSEW)

    botao6 = Button(frame_baixo, text="Mostrar caixa de todas reservas",style='my.TButton', command=abrir_janelaCaixa)
    botao6.grid(row=6, column=0, padx=14, ipady=10, sticky=NSEW)

    botao7 = Button(frame_baixo, text="Mostrar todos moradores cadastrados",style='my.TButton', command=abrir_janelaMoradores)
    botao7.grid(row=7, column=0, padx=14, ipady=10, sticky=NSEW)

    janela.mainloop()
menuPrincipal()