# Esta função imprime um menu de opções na tela para o usuário.
def menu():
    print('''Menu de Gráficos:
    1- Comparação 1 com todos (numero de aparições)
    2- Comparação 1 com 1 (numero de aparições)
    3- Comparação 1 com todos (ano de entrada)
    4- Comparação 1 com 1 (ano de entrada)
    5- Comparação 1 com todos (anos desde o ingresso)
    6- Comparação 1 com 1 (anos de ingresso nos Vingadores)
    ''')

# Esta função lida com a leitura de um arquivo CSV chamado 'avengers.csv' usando a biblioteca pandas. 
# O arquivo é lido com codificação 'latin1', e o DataFrame resultante é retornado.
def ler_arquivo():
    import pandas as pd

    df = pd.read_csv('avengers.csv', encoding='latin1')
    return df

# Esta função aceita uma mensagem msg como entrada, que é uma mensagem solicitando ao usuário que digite um nome.
def nome_input(msg):
    # A função converte o nome em formato capitalizado (a primeira letra de cada palavra em maiúscula) e retorna o resultado. 
    # Isso é útil para garantir que os nomes estejam em um formato consistente.
    return msg.capitalize()
        