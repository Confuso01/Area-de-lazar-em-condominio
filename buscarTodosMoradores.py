import pandas as pd
import tkinter as tk
from tkinter import ttk

entrada = None
tabela = None 

    
def janelaMoradores():
    global entrada, tabela

    janela = tk.Tk()
    janela.title("Busca por moradores")

    instrucoes = tk.Label(janela, font='Ivy 10', text="TODAS OS MORADORES CADASTRADOS:")
    instrucoes.pack()

    tabela = ttk.Treeview(janela, columns=("Nome", "Email", "Telefone"), show='headings')
    tabela.pack()
    tabela.heading("Nome", text="Nome")
    tabela.heading("Email", text="Email")
    tabela.heading("Telefone", text="Telefone")

    tabela.delete(*tabela.get_children()) # Limpa a tabela
    df = pd.read_excel('CadastroMoradores.xlsx')
    resultados = df
    resultados = resultados.groupby(["CPF"]).first().reset_index()
    for i, row in resultados.iterrows():
        tabela.insert("", "end", values=(row['nome'], row['email'], row['telefone']))


    janela.mainloop()