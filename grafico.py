from info_personagem import InfoPersonagem as ip
from funcoes import ler_arquivo
import matplotlib.pyplot as plt

class Grafico:
    # Este é o construtor da classe Grafico, mas atualmente não faz nada, pois está vazio (contém apenas pass).
    def __init__(self):
        pass

    # Este método aceita o nome de um personagem e um DataFrame filtro_personagem como argumentos. 
    # Ele calcula o número de aparições do personagem selecionado em relação ao número total de aparições de todos os personagens. 
    # Em seguida, cria um gráfico de barras que compara esses valores.
    def grafico_aparicoes_1_para_muitos(nome_personagem, filtro_personagem):
        df = ler_arquivo()

        num_aparicoes_pers = ip.info_df(filtro_personagem, 'Aparições')
        num_aparicoes_todos = sum(df['Aparições'].values)

        print(f"{nome_personagem} apareceu em {num_aparicoes_pers} HQs dos Vingadores")

        x = [nome_personagem, "Todos"]
        y = [num_aparicoes_pers, num_aparicoes_todos]

        plt.bar(x, y)

        plt.xlabel('Personagem(ns)')
        plt.ylabel('Número de aparições nas HQs')

        plt.title(f'Aparições nas HQs de {nome_personagem}\n(em comparação ao total de aparições de todos os membros)')
        plt.show()

    # Esta função funciona um pouco diferente, ela calcula o número de aparições do personagem selecionado e solicita ao usuário que digite o nome de outro personagem para comparação.
    def grafico_aparicoes_1_para_1(nome_personagem, filtro_personagem):
        df = ler_arquivo()

        num_aparicoes_pers = ip.info_df(filtro_personagem, 'Aparições')

        print(f"{nome_personagem} apareceu em {num_aparicoes_pers} HQs dos Vingadores")

        pers_comp = input("Digite o nome do personagem que você deseja comparar: ")
        pers_comp_filtrado = df[df['Nome/Herói'] == pers_comp]

        num_aparicoes_outro = ip.info_df(pers_comp_filtrado, 'Aparições')

        print(f"{pers_comp} apareceu em {num_aparicoes_outro} HQs dos Vingadores")

        x = [nome_personagem, pers_comp]
        y = [num_aparicoes_pers, num_aparicoes_outro]

        plt.bar(x, y)

        plt.xlabel('Personagem(ns)')
        plt.ylabel('Número de aparições nas HQs')

        plt.title(f'Aparições nas HQs de {nome_personagem} comparado com {pers_comp}')
        plt.show()

    # Este método aceita o nome de um personagem e um DataFrame filtro_personagem como argumentos. 
    # Ele calcula o ano de entrada do personagem selecionado no grupo Vingadores e compara esse ano com o ano de entrada do membro mais antigo e do membro mais novo dos Vingadores. 
    # Em seguida, cria um gráfico de barras horizontais que compara esses anos.
    def grafico_ano_entrada_1_para_muitos(nome_personagem, filtro_personagem):
        df = ler_arquivo()

        ano_entrada_pers = ip.info_df(filtro_personagem, 'Ano')
        print(f'{nome_personagem} entrou no grupo Vingadores no ano {ano_entrada_pers} nas HQs')

        df_entrada_todos = df[df['Ano'] > 0]
        
        ano_entrada_antigo = min(df_entrada_todos['Ano'].values)
        ano_entrada_novo = max(df_entrada_todos['Ano'].values)
        
        x = [ano_entrada_antigo, ano_entrada_pers, ano_entrada_novo]
        y = ["Mais Antigo", nome_personagem, "Mais Novo"]

        plt.barh(y, x)

        plt.xlim(ano_entrada_antigo-10, ano_entrada_novo+10)

        plt.xlabel('Ano de Entrada')
        plt.ylabel('Comparação com o Personagem')

        plt.title(f'Ano da entrada nas HQs de {nome_personagem} no grupo dos Vingadores\n(comparado com os membros mais antigo e mais novo)')

        plt.show()

    # Funcionando de forma parecida com o anterior, mas aqui ele faz a comparação entre 1 e 1
    def grafico_ano_entrada_1_para_1(nome_personagem, filtro_personagem):
        df = ler_arquivo()

        ano_entrada_pers = ip.info_df(filtro_personagem, 'Ano')
        print(f"{nome_personagem} entrou para os Vingadores no ano {ano_entrada_pers}")
        
        pers_comp = input("Qual herói deseja comparar?: ")
        pers_comp_filtrado = df[df['Nome/Herói'] == pers_comp]
        
        ano_entrada_outro = ip.info_df(pers_comp_filtrado, 'Ano')
        
        print(f"{pers_comp} entrou para os Vingadores no ano {ano_entrada_outro}")
        
        x = [nome_personagem, pers_comp]
        y = [ano_entrada_pers, ano_entrada_outro]

        plt.bar(x, y)

        plt.ylim(ano_entrada_pers-10, ano_entrada_outro+10)
        
        plt.xlabel("Ano de Entrada")
        plt.ylabel("Comparação 1 com 1")
        
        plt.title(f"Ano de entrada de {nome_personagem} comparado com {pers_comp}")
        plt.show()

    # Este método aceita o nome de um personagem e um DataFrame filtro_personagem como argumentos. 
    # Ele calcula o número de anos em que o personagem selecionado participou ativamente dos Vingadores e compara esse valor com os anos de participação do membro mais antigo e do membro mais novo dos Vingadores. 
    # Em seguida, cria um gráfico de barras horizontais que compara esses anos.
    def grafico_ingresso_1_para_muitos(nome_personagem, filtro_personagem):
        df = ler_arquivo()

        anos_ingresso_pers = ip.info_df(filtro_personagem, 'Anos Ingresso')
        print(f'{nome_personagem} tem {anos_ingresso_pers} anos participando ativamente dos Vingadores')

        df_anos_ingresso_todos = df[df['Anos Ingresso'] >= 0]

        pers_mais_anos_ingresso = max(df_anos_ingresso_todos['Anos Ingresso'].values)
        pers_menos_anos_ingresso = min(df_anos_ingresso_todos['Anos Ingresso'].values)

        x=[pers_mais_anos_ingresso, anos_ingresso_pers, pers_menos_anos_ingresso]
        y=["+ Antigo", nome_personagem, "+ Novo"]

        plt.barh(y, x)

        plt.xlim(pers_menos_anos_ingresso-10, pers_mais_anos_ingresso+10)

        plt.xlabel('Anos Ingresso')
        plt.ylabel('Comparação com o Personagem')

        plt.title(f'Ano(s) de Ingresso nas HQs de {nome_personagem} no grupo dos Vingadores\n(comparado com os membros mais antigo e mais novo)')

        plt.show()

    # Também funcionado de forma parecida com o anterior, mas aqui usamos novamente a comparação 1 e 1
    def grafico_ingresso_1_para_1(nome_personagem, filtro_personagem):
        df = ler_arquivo()

        anos_ingresso_pers = ip.info_df(filtro_personagem, 'Anos Ingresso')
        print(f"{nome_personagem} tem {anos_ingresso_pers} anos participando ativamente dos Vingadores")
        
        pers_comp = input("Qual herói você deseja comparar?: ")
        pers_comp_filtrado = df[df['Nome/Herói'] == pers_comp]
        
        anos_ingresso_outro = ip.info_df(pers_comp_filtrado, 'Anos Ingresso')
        
        print(f"{pers_comp} tem {anos_ingresso_outro} anos participando ativamente dos Vingadores")
        
        x = [nome_personagem, pers_comp]
        y = [anos_ingresso_pers, anos_ingresso_outro]

        plt.bar(x, y)
        
        plt.xlabel("Anos de Ingresso")
        plt.ylabel("Comparação 1 a 1")
        
        plt.title(f"Anos de ingresso de {nome_personagem} comparado com {pers_comp}")
        plt.show()