from tkinter import *
from tkinter.ttk import *
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
from datetime import datetime
import projeto

dia = None
listaDeVisitantes = ['NENHUM']

def pegarDia(*args):
    print(dia.get())

def insirirNomeVisitantes(NumeroV):

    if(NumeroV != '0'):
        janelaVisitantes = Toplevel()
        janelaVisitantes.title('')
        janelaVisitantes.geometry('930x500')
        janelaVisitantes.configure(background='#feffff')
        janelaVisitantes.resizable(width=TRUE, height=TRUE)

        framePrincipalV = Frame(janelaVisitantes, width=300, height=40, relief='flat')
        framePrincipalV.grid(row=0, column=0, padx=0, pady=1, sticky=NSEW)

        my_entrys = []
        n = int(NumeroV) / 3
        extras = 0
        if (n > int(n)):
            extras = (n - int(n)) * 10
            extras = int(int(extras) / 3)
        m = 0
        l = 1
        contador = 1
        numerosLinhas = 0
        if(int(n) != 0):
            for i in range(int(n)):
                for j in range(3):
                    numerosLinhas = i + m
                    l_visitante = Label(framePrincipalV, text=f'Nome visitante {contador}:', font='Ivy 10').grid(row=i + m, column=j, padx=10, pady=1, sticky=NSEW)
                    e_visitante = Entry(framePrincipalV, width=25, justify='left', font=('', 15))  
                    e_visitante.insert(END, '')
                    e_visitante.grid(row=i + l, column=j, padx=14, pady=1, sticky=NSEW)
                    my_entrys.append(e_visitante)
                    contador += 1
                m += 1 
                l += 1
        if(extras != 0):
            for i in range(1):
                for j in range(extras):
                    l_visitante = Label(framePrincipalV, text=f'Nome visitante {contador}:', font='Ivy 10').grid(row=numerosLinhas+2, column=j, padx=10, pady=1, sticky=NSEW)
                    e_visitante = Entry(framePrincipalV, width=25, justify='left', font=('', 15))
                    e_visitante.insert(END, '')
                    e_visitante.grid(row=numerosLinhas+3, column=j, padx=14, pady=1, sticky=NSEW)    
                    my_entrys.append(e_visitante)
                    contador += 1
            bnt_enviarV = Button(framePrincipalV, text ="Enviar visitantes", command=lambda: enviarVisitantes(my_entrys, janelaVisitantes)).grid(row=numerosLinhas+4, column=1, padx=14, pady=1, sticky=NSEW)
        else:
            bnt_enviarV = Button(framePrincipalV, text ="Enviar visitantes", command=lambda: enviarVisitantes(my_entrys, janelaVisitantes)).grid(row=numerosLinhas+2, column=1, padx=14, pady=1, sticky=NSEW)
        janelaVisitantes.mainloop()
    else:
        messagebox.showerror("Erro", "Insira uma quantidade de visitantes para colocar seus nomes")

def enviarVisitantes(listaVisitantes, root):
    global listaDeVisitantes 
    listaDeVisitantes = []
    for i in range(len(listaVisitantes)):
        listaDeVisitantes.append(listaVisitantes[i].get().upper())
    root.destroy()

def cadastrarReserva(janela):
    nome = e_nome.get().upper()
    area_selecionada = area.get().upper()
    visitantes = listaDeVisitantes
    data = dia.get()
    horaE = e_horaEntrada.get()
    horaS = e_horaSaida.get()
    valor = valor_area_reservada(area_selecionada, horaE, horaS)
    if(nome != ''):
        if(area_selecionada != ''):
            if(formatoHoraEntradaSaida(horaE, horaS)):
                projeto.cadastrarReserva(nome, visitantes, data, horaE, horaS, area_selecionada, valor)
                janela.destroy()
                messagebox.showinfo(title='Sucesso', message='Cadastro feito com sucesso')
        else:
            messagebox.showerror("Erro", "Selecione uma area")
    else:
        messagebox.showerror("Erro", "Espaço de nome está vazio")

def valor_area_reservada(area, horaE, horaS):
    hora1 = datetime.strptime(horaE, '%H:%M')
    hora2 = datetime.strptime(horaS, '%H:%M')
    delta = hora2 - hora1
    
    horaMin = str(delta).split(':')
    hora = int(horaMin[0])
    minutos = int(horaMin[1])
    valor_total = 0
    if area == 'PISCINA':
        valor_total = 40 * hora + (minutos / 60) * 40
    elif area == 'SALA DE JOGOS':
        valor_total = 25 * hora + (minutos / 60) * 25
    elif area == 'SAUNA':
        valor_total = 50 * hora + (minutos / 60) * 50
    elif area == 'QUADRA DE FUTEBOL':
        valor_total = 15 * hora + (minutos / 60) * 15
    elif area == 'SALÃO DE FESTA':
        valor_total = 90 * hora + (minutos / 60) * 90
    return (f'R${valor_total:.2f}')

def formatoHoraEntradaSaida(horaE, horaS):
    horaVEntrada = FALSE
    horaVSaida = FALSE

    partesEntrada = horaE.split(":")
    if len(partesEntrada) != 2:
        messagebox.showerror("Erro", "Formato HH:MM inválido para o campo HORA DE ENTRADA")
    else:
        try:
            horaE = int(partesEntrada[0])
            minutoE = int(partesEntrada[1])
            if horaE < 0 or horaE > 23:
                messagebox.showerror("Erro", "HORA inválida para HORA DE ENTRADA")
            elif minutoE < 0 or minutoE > 59:
                messagebox.showerror("Erro", "MINUTO inválido para HORA DE ENTRADA")
            else:
                horaVEntrada = TRUE
        except ValueError:
            messagebox.showerror("Erro", "informe apenas digitos no campo HORA DE ENTRADA")

    partesSaida = horaS.split(":")
    if len(partesSaida) != 2:
        messagebox.showerror("Erro", "Formato HH:MM inválido para o campo HORA DE ENTRADA")
    else:
        try:
            horaS = int(partesSaida[0])
            minutoS = int(partesSaida[1])
            if horaS < 0 or horaS> 23:
                messagebox.showerror("Erro", "HORA inválida para HORA DE ENTRADA")
            elif minutoS < 0 or minutoS > 59:
                messagebox.showerror("Erro", "MINUTO inválido para HORA DE ENTRADA")
            else:
                horaVSaida = TRUE
        except ValueError:
            messagebox.showerror("Erro", "informe apenas digitos no campo HORA DE ENTRADA")
    if(horaS == 0):
        messagebox.showerror("Erro", "Informe um periodo dentro do mesmo dia (hora de saida 00:00 invalida)")
        return False
    if((horaS - horaE)< 1):
        messagebox.showerror("Erro", "Periodo fora de horario minimo de 1 hora de reserva")
        return False
    elif(horaVSaida and horaVEntrada):
        return True
    else:
        return True

cont = 0
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

def janelaCadastroReserva():
    global dia
    global e_nome, area, e_horaEntrada, e_horaSaida, numVisitantes, listaDeVisitantes 

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
    l_cadastro = Label(frame_cima, text='CADASTRO RESERVA', anchor=NE, font='Ivy 15').place(x=5, y=5)
    #Parte de baixo
    l_nome = Label(frame_baixo, text='Nome: *', anchor=NW, font='Ivy 10').grid(row=0, column=0, padx=10, pady=1, sticky=NSEW)
    e_nome = Entry(frame_baixo, width=25, justify='left', font=('', 15))
    e_nome.insert(END, '')
    e_nome.grid(row=1, column=0, padx=14, pady=1, sticky=NSEW)


    l_visitantes = Label(frame_baixo, text='Visitantes: ', anchor=NW, font='Ivy 10').grid(row=2, column=0, padx=10, pady=1, sticky=NSEW)
    numVisitantes = StringVar(frame_baixo)
    e_visitantes = Entry(frame_baixo, width=25, justify='left', font=('', 15), textvariable=numVisitantes)
    e_visitantes.insert(END, '0')
    e_visitantes.grid(row=3, column=0, padx=14, pady=1, sticky=NSEW)

    bnt_cadastroV = Button(frame_baixo, text ="Insirir visitantes", command=lambda: insirirNomeVisitantes(e_visitantes.get())).grid(row=4, column=0, padx=14, pady=1, sticky=NSEW)


    l_area = Label(frame_baixo, text='Area: *', anchor=NW, font='Ivy 10').grid(row=5, column=0, padx=10, pady=1, sticky=NSEW)
    areas = ['', 'Piscina', 'Sala de Jogos', 'Quadra de futebol', 'Sauna', 'Salão de festa']
    area = StringVar(frame_baixo)
    area.set(areas[0])
    e_area = OptionMenu(frame_baixo, area, *areas)
    e_area.grid(row=6, column=0, padx=14, pady=1, sticky=NSEW)

    l_data = Label(frame_baixo, text='Dia da reserva: *', anchor=NW, font='Ivy 10').grid(row=7, column=0, padx=10, pady=1, sticky=NSEW)
    dia = StringVar(frame_baixo)
    cal = DateEntry(frame_baixo, selectmode='day', textvariable=dia, locale='pt_BR')
    dia.trace('w', pegarDia)
    cal.grid(row=8, column=0, padx=10, pady=1, sticky=NSEW)

    l_horaEntrada = Label(frame_baixo, text='Hora de entrada: *', anchor=NW, font='Ivy 10').grid(row=9, column=0, padx=10, pady=1, sticky=NSEW)
    e_horaEntrada = Entry(frame_baixo, width=25, justify='left', font=('', 15))
    e_horaEntrada.insert(END, '')
    e_horaEntrada.grid(row=10, column=0, padx=14, pady=1, sticky=NSEW)

    l_horaSaida = Label(frame_baixo, text='Hora de saida: *', anchor=NW, font='Ivy 10').grid(row=11, column=0, padx=10, pady=1, sticky=NSEW)
    e_horaSaida = Entry(frame_baixo, width=25, justify='left', font=('', 15))
    e_horaSaida.insert(END, '')
    e_horaSaida.grid(row=12, column=0, padx=14, pady=1, sticky=NSEW)


    bnt_cadastrarReserva = Button(frame_baixo, text ="CADASTRAR RESERVA", command=lambda: cadastrarReserva(janela)).grid(row=13, column=0, padx=14, pady=1, sticky=NSEW)
    janela.mainloop()