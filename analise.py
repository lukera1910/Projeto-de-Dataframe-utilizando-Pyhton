# Isso importa a classe Grafico do módulo grafico e a apelida como grf. 
# Isso permite que você acesse a classe usando o alias grf.
from grafico import Grafico as grf
# Isso importa a classe InfoPersonagem do módulo info_personagem e a apelida como ip. 
# Isso permite que você acesse a classe usando o alias ip.
from info_personagem import InfoPersonagem as ip
# Isso importa o módulo funcoes e o apelida como fct. 
# Isso permite que você acesse funções definidas nesse módulo usando o alias fct.
import funcoes as fct

# Isso chama a função ler_arquivo() do módulo funcoes e atribui o resultado a df.
df = fct.ler_arquivo()
#Um loop para iniciar o programa e escolher seu personagem
while True:
    # Isso solicita ao usuário que digite o nome de um personagem desejado e armazena a entrada na variável personagem_desejado.
    personagem_desejado = input("Digite o nome do personagem que deseja pesquisar (Ou Sair para acabar): ")
    #Condição para sair do programa
    if personagem_desejado == 'sair':
        break
    # Isso cria um novo DataFrame personagem_filtrado que contém apenas as linhas onde a coluna 'Nome/Herói' é igual ao nome do personagem desejado.
    personagem_filtrado = df[df['Nome/Herói'] == personagem_desejado]

    # Isso chama a função ficha_completa() da classe InfoPersonagem com o nome do personagem e o DataFrame filtrado como argumentos.
    ip.ficha_completa(personagem_desejado, personagem_filtrado)

    # Há um loop while que continua até que o usuário escolha a opção 0 (provavelmente para sair do programa). 
    # Dentro do loop, o código verifica a escolha do usuário e chama funções relacionadas a gráficos com base na opção selecionada. 
    while True:
        # Isso chama a função menu() do módulo funcoes.
        fct.menu()
        # Isso solicita ao usuário que escolha uma opção de gráfico e armazena a escolha como um número inteiro na variável opc.
        opc = int(input("Qual opção de gráficos você deseja ver: "))
        if not personagem_filtrado.empty:
            if opc == 1:
                #opção 1 mostrará o grafico de comparação do numero de aparições do personagem escolhido com o total de aparições de todos os personagens
                grf.grafico_aparicoes_1_para_muitos(personagem_desejado, personagem_filtrado)
            elif opc == 2:
                #opção 2 mostrará o grafico de comparação do numero de aparições de dois personagens especificos
                grf.grafico_aparicoes_1_para_1(personagem_desejado, personagem_filtrado)
            elif opc == 3:
                #opção 3 mostrará o grafico de comparação do ano de entrada do personagem com o mais antigo e o mais novo
                grf.grafico_ano_entrada_1_para_muitos(personagem_desejado, personagem_filtrado)
            elif opc == 4:
                #opção 4 mostra o ano de entrada de dois determinados heróis
                grf.grafico_ano_entrada_1_para_1(personagem_desejado, personagem_filtrado)
            elif opc == 5:
                #opção 5 mostrará o grafico de comparação do ano de ingresso do personagem com o mais anos e o com menos anos
                grf.grafico_ingresso_1_para_muitos(personagem_desejado, personagem_filtrado)
            elif opc == 6:
                #opção 6 mostra um gráfico comparando os anos de ingresso de dois determinados heróis
                grf.grafico_ingresso_1_para_1(personagem_desejado, personagem_filtrado)
            else:
                break
    else:
        print(f"{personagem_desejado} não foi encontrado")
print('Obrigado por utilizar!!')
