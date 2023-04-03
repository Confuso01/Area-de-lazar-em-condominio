from IPython.display import display
import pandas as pd


def cadastrarMorador(cpf, nome, apartamento, email, telefone):
    moradores_df = pd.read_excel('CadastroMoradores.xlsx')


    cadastro = {'CPF': cpf, 'nome':nome, 'apartamento': apartamento, 'email':email, 'telefone': telefone}

    cadastro_df = pd.DataFrame(cadastro, index=[0])
    display(cadastro_df)
    moradores_df = moradores_df.append(cadastro_df, ignore_index=True)
    moradores_df.to_excel("CadastroMoradores.xlsx", index=False)
    return

def cadastrarReserva(nome, visitantes, data, horaE, horaS, area_selecionada, valor):
    reservas_df = pd.read_excel('CadastroReservas.xlsx')

    cadastro = {'Morador': nome, 'Visitantes': visitantes}
    cadastro['Area'] = area_selecionada
    cadastro['DiaR'] = data
    cadastro['HoraEntrada'] = horaE
    cadastro['HoraSaida'] = horaS
    cadastro['Valor'] = valor
    print(cadastro)

    cadastro_df = pd.DataFrame(cadastro)
    display(cadastro_df)
    reservas_df = reservas_df.append(cadastro_df, ignore_index=True)
    reservas_df.to_excel("CadastroReservas.xlsx", index=False)
    return 
