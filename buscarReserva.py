import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

entrada = None
tabela = None 

def buscar_registro():
    tabela.delete(*tabela.get_children()) # Limpa a tabela
    df = pd.read_excel('CadastroReservas.xlsx')
    nome = entrada.get()
    nome = entrada.get()
    coluna = df["Morador"]
    listanomes = coluna.tolist()
    if(nome.upper() in listanomes):
        resultados = df[df['Morador'] == nome.upper()]
        for i, row in resultados.iterrows():
            tabela.insert("", "end", values=(row['Visitantes'], row['DiaR'], row['HoraEntrada'], row['HoraSaida'], row['Area']))
    else:
        messagebox.showerror("Erro", "O nome do morador informado não está presente na lista de reservas. Faça uma reserva com esse morador ou digite o nome corretamente")

def janelaBuscarReserva():
    global entrada, tabela

    janela = tk.Tk()
    janela.title("Busca de Reservas")

    instrucoes = tk.Label(janela, font='Ivy 10', text="Insira o NOME DO MORADOR que você deseja buscar a reserva:")
    instrucoes.pack()

    entrada = tk.Entry(janela)
    entrada.pack()

    botao = tk.Button(janela, text="Buscar", command=buscar_registro)
    botao.pack()

    tabela = ttk.Treeview(janela, columns=("Visitantes", "Dia", "Hora Entrada", "Hora Saida", "Area"), show='headings')
    tabela.pack()
    tabela.heading("Visitantes", text="Visitantes")
    tabela.heading("Dia", text="Dia")
    tabela.heading("Hora Entrada", text="Hora Entrada")
    tabela.heading("Hora Saida", text="Hora Saida")
    tabela.heading("Area", text="Area")


    janela.mainloop()