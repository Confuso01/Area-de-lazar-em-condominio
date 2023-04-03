import pandas as pd
import tkinter as tk
from tkinter import ttk

entrada = None
tabela = None 

    
def janelaCaixa():
    global entrada, tabela

    janela = tk.Tk()
    janela.title("Busca de caixa")

    instrucoes = tk.Label(janela, font='Ivy 10', text="TODOS OS CAIXAS FEITOS NAS RESERVAS:")
    instrucoes.pack()

    tabela = ttk.Treeview(janela, columns=("Morador", "Dia", "Hora Entrada", "Hora Saida", "Area", "Valor"), show='headings')
    tabela.pack()
    tabela.heading("Morador", text="Morador")
    tabela.heading("Dia", text="Dia")
    tabela.heading("Hora Entrada", text="Hora Entrada")
    tabela.heading("Hora Saida", text="Hora Saida")
    tabela.heading("Area", text="Area")
    tabela.heading("Valor", text="Valor")
    

    tabela.delete(*tabela.get_children()) # Limpa a tabela
    df = pd.read_excel('CadastroReservas.xlsx')
    resultados = df
    resultados = resultados.groupby(["DiaR", "HoraEntrada"]).first().reset_index()
    for i, row in resultados.iterrows():
        tabela.insert("", "end", values=(row['Morador'], row['DiaR'], row['HoraEntrada'], row['HoraSaida'], row['Area'], row['Valor']))


    janela.mainloop()