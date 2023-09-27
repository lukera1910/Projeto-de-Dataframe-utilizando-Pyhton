import pandas as pd

class InfoPersonagem:
    def __init__(self):
        pass

    # Este método aceita um DataFrame df_filtrado e o nome de uma coluna como argumentos. 
    # Ele retorna o valor da primeira linha da coluna especificada no DataFrame.
    def info_df(df_filtrado, nome_coluna):
        return df_filtrado[nome_coluna].values[0]
    
    # Este método aceita informações pessoais de um personagem, como nome, gênero, nível de membro e status, como argumentos e imprime essas informações em um formato específico.
    def info_pessoal(nome, genero, n_membro, status):
        print(f"""Dados:
    Nome: {nome}
    Gênero: {genero}
    Nível Membro: {n_membro}
    Continua? {status}\n """)
        
   # Este método aceita um nome de coluna e um valor como argumentos e imprime o nome da coluna seguido pelo valor.
    def info_mortes_retornos(nome_col, valor):
        print(f'{nome_col}: {valor}')

    # Este método aceita o nome de um personagem e um DataFrame filtro_personagem como argumentos. 
    # Ele cria um dicionário info_ficha que contém informações específicas do personagem, como nome, gênero, nível de membro e status, usando o método info_df para extrair essas informações do DataFrame. 
    # Em seguida, chama o método info_pessoal para imprimir informações pessoais do personagem.
    # Além disso, este método itera por uma lista de colunas relacionadas a mortes e retornos (colunas_mortes_retornos_notas) e, se houver um valor não nulo para uma coluna no DataFrame filtro_personagem, chama o método info_mortes_retornos para exibir essa informação.
    def ficha_completa(nome_personagem, filtro_personagem):

        info_ficha = {'Nome': InfoPersonagem.info_df(filtro_personagem, 'Nome/Herói'), 'Genero': InfoPersonagem.info_df(filtro_personagem, 'Gênero'), 'Nivel': InfoPersonagem.info_df(filtro_personagem, 'Honorário/Titular'), 'Status': InfoPersonagem.info_df(filtro_personagem, 'Continuou?')}

        InfoPersonagem.info_pessoal(info_ficha['Nome'], info_ficha['Genero'], info_ficha['Nivel'], info_ficha['Status'])

        print(f"Mortes e retornos de {nome_personagem}:")
        
        colunas_mortes_retornos_notas = ['Primeira Morte?', 'Primeiro Retorno?', 'Segunda Morte?', 'Segundo Retorno?', 'Terceira Morte?', 
                            'Terceiro Retorno?', 'Quarta Morte?', 'Quarto Retorno?', 'Quinta Morte?', 'Quinto Retorno?', 'Notas']

        for coluna in colunas_mortes_retornos_notas:
            if pd.notna(InfoPersonagem.info_df(filtro_personagem, coluna)):
                InfoPersonagem.info_mortes_retornos(coluna, InfoPersonagem.info_df(filtro_personagem,coluna))