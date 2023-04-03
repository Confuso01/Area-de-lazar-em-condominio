import pandas as pd
from tkinter import *
from tkinter.ttk import *

entrada = None
tabela = None 

def buscar_registro():
    tabela.delete(*tabela.get_children()) # Limpa a tabela
    df = pd.read_excel('CadastroReservas.xlsx')
    resultados = df[df['Area'] == area.get().upper()]
    resultados = resultados.groupby(["DiaR", "HoraEntrada"]).first().reset_index()
    for i, row in resultados.iterrows():
        tabela.insert("", "end", values=(row['Morador'], row['DiaR'], row['HoraEntrada'], row['HoraSaida']))

def janelaBuscarArea():
    global area, tabela

    janela = Tk()
    janela.title("Busca de Reservas")

    instrucoes = Label(janela, font='Ivy 10', text="Selecione o nome da AREA que você deseja verificar suas reservas:")
    instrucoes.pack()

    areas = ['Piscina', 'Piscina', 'Sala de Jogos', 'Quadra de futebol', 'Sauna', 'Salão de festa']
    area = StringVar(janela)
    area.set(areas[0])
    e_area = OptionMenu(janela, area, *areas)
    e_area.pack()

    botao = Button(janela, text="Buscar", command=buscar_registro)
    botao.pack()

    tabela = Treeview(janela, columns=("Morador", "Dia", "Hora Entrada", "Hora Saida"), show='headings')
    tabela.pack()
    tabela.heading("Morador", text="Morador")
    tabela.heading("Dia", text="Dia")
    tabela.heading("Hora Entrada", text="Hora Entrada")
    tabela.heading("Hora Saida", text="Hora Saida")


    janela.mainloop()