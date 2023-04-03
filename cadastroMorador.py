from tkinter import *
from tkinter.ttk import *
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import pandas as pd
import projeto
import re


def cadastrarMorador(janela):
    cpf = e_CPF.get()
    nome = e_nome.get().upper()
    email = e_email.get()
    apartamento = e_apartamento.get()
    numero = e_telefone.get()
    telefone = validarTelefone(numero)
    if(not apartamento.isnumeric()):
        messagebox.showerror("Erro","Informe apenas digitos em apartamento")
    if(validarCPF(cpf) and validarEmail(email)):
        projeto.cadastrarMorador(cpf, nome, apartamento, email, telefone)
        janela.destroy()
        messagebox.showinfo(title='Sucesso', message='Cadastro feito com sucesso')

def validarTelefone(numero):
    n = str(numero)
    if n.isnumeric():
        if len(n) == 10:
            return("({}{}) {}{}{}{}-{}{}{}{}" .format(numero[0],numero[1],numero[2],numero[3],numero[4],numero[5],numero[6],numero[7],numero[8],numero[9]))          
        elif len(n) ==11:
            return("({}{}) {} {}{}{}{}-{}{}{}{}" .format(numero[0],numero[1],numero[2],numero[3],numero[4],numero[5],numero[6],numero[7],numero[8],numero[9],numero[10]))
        else:
            messagebox.showerror("Erro", "Informe um telefone válido (DDD 9 ou 8 DIGITOS SEM ESPAÇO OU TRAÇO)!!!")
    else:
        messagebox.showerror("Erro", "Informe apenas digitos para o telefone e um formato válido (DDD 9 ou 8 DIGITOS SEM ESPAÇO OU TRAÇO)!!!") 
            

def validarEmail(email):
    regex = '^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):
        return True
    else:
        messagebox.showerror("Erro","Email Inválido insira-o corretamente")
        return False


def validarCPF(cpf):
    ok = False
    n = str(cpf)
    if n.isnumeric():
        if len(n)==11:
            df = pd.read_excel("CadastroMoradores.xlsx")
            coluna = df["CPF"]
            listadocpf = coluna.tolist()
            cpfFormato = "{}{}{}.{}{}{}.{}{}{}-{}{}".format(cpf[0],cpf[1],cpf[2],cpf[3],cpf[4],cpf[5],cpf[6],cpf[7],cpf[8],cpf[9],cpf[10])
            if(cpfFormato in listadocpf):
                messagebox.showerror("Erro", "O CPF já está registrado")
                return False
            else:
                ok = True
        else:
            messagebox.showerror("Erro", "O CPF não tem 11 digitos")
            return False    
    else:
        messagebox.showerror("Erro", "Informe o CPF em um formato válido (Sem traço e ponto)!!!") 
        return False
        
    if ok:
        return True
            
cont = 0
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

def janelaCadastroMorador():
    global e_CPF, e_nome, e_email, e_apartamento, e_telefone

    janela = Tk()
    janela.title('')
    janela.geometry('300x500')
    janela.configure(background='#feffff')
    janela.resizable(width=FALSE, height=FALSE)

    frame_cima = Frame(janela, width=300, height=40, relief='flat')
    frame_cima.grid(row=0, column=0, padx=0, pady=1, sticky=NSEW)

    frame_baixo = Frame(janela, width=300, height=460, relief='flat')
    frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

    #Titulo
    l_cadastro = Label(frame_cima, text='CADASTRO MORADOR', anchor=NE, font='Ivy 15').place(x=5, y=5)
    #Parte de baixo
    l_CPF = Label(frame_baixo, text='CPF: *', anchor=NW, font='Ivy 10').grid(row=0, column=0, padx=10, pady=1, sticky=NSEW)
    e_CPF = Entry(frame_baixo, width=25, justify='left', font=('', 15))
    e_CPF.insert(END, '')
    e_CPF.grid(row=1, column=0, padx=14, pady=1, sticky=NSEW)

    l_nome = Label(frame_baixo, text='Nome: *', anchor=NW, font='Ivy 10').grid(row=2, column=0, padx=10, pady=1, sticky=NSEW)
    e_nome = Entry(frame_baixo, width=25, justify='left', font=('', 15))
    e_nome.insert(END, '')
    e_nome.grid(row=3, column=0, padx=14, pady=1, sticky=NSEW)

    l_apartamento = Label(frame_baixo, text='Apartamento: *', anchor=NW, font='Ivy 10').grid(row=4, column=0, padx=10, pady=1, sticky=NSEW)
    e_apartamento = Entry(frame_baixo, width=25, justify='left', font=('', 15))
    e_apartamento.insert(END, '0')
    e_apartamento.grid(row=5, column=0, padx=14, pady=1, sticky=NSEW)

    l_email = Label(frame_baixo, text='Email: *', anchor=NW, font='Ivy 10').grid(row=6, column=0, padx=10, pady=1, sticky=NSEW)
    e_email = Entry(frame_baixo, width=25, justify='left', font=('', 15))
    e_email.insert(END, '')
    e_email.grid(row=7, column=0, padx=14, pady=1, sticky=NSEW)

    l_telefone = Label(frame_baixo, text='telefone: *', anchor=NW, font='Ivy 10').grid(row=8, column=0, padx=10, pady=1, sticky=NSEW)
    e_telefone= Entry(frame_baixo, width=25, justify='left', font=('', 15))
    e_telefone.insert(END, '0')
    e_telefone.grid(row=9, column=0, padx=14, pady=1, sticky=NSEW)


    bnt_cadastrarMorador = Button(frame_baixo, text ="CADASTRAR MORADOR", command=lambda: cadastrarMorador(janela)).grid(row=10, column=0, padx=14, pady=1, sticky=NSEW)

    janela.mainloop()