import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

entrada = None
tabela = None 

def buscar_registro():
    tabela.delete(*tabela.get_children()) # Limpa a tabela
    df = pd.read_excel('CadastroMoradores.xlsx')
    nome = entrada.get()
    coluna = df["nome"]
    listanomes = coluna.tolist()
    if(nome.upper() in listanomes):
        resultados = df[df['nome'] == nome.upper()]
        for i, row in resultados.iterrows():
            tabela.insert("", "end", values=(row['apartamento'],row['nome'], row['email'], row['telefone']))
    else:
        messagebox.showerror("Erro", "Nome informado não está presente na lista de moradores. Cadastre o novo morador ou digite o nome corretamente")

def janelaBuscarMorador():
    global entrada, tabela

    janela = tk.Tk()
    janela.title("Busca de Registros")

    instrucoes = tk.Label(janela, font='Ivy 10', text="Insira o NOME do registro que você deseja buscar:")
    instrucoes.pack()

    entrada = tk.Entry(janela)
    entrada.pack()

    botao = tk.Button(janela, text="Buscar", command=buscar_registro)
    botao.pack()

    tabela = ttk.Treeview(janela, columns=("Apartamento","Nome", "Email", "Telefone"), show='headings')
    tabela.pack()
    tabela.heading("Apartamento", text="Apartamento")
    tabela.heading("Nome", text="Nome")
    tabela.heading("Email", text="Email")
    tabela.heading("Telefone", text="Telefone")

    janela.mainloop()
