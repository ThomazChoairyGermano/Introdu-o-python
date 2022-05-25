import random


def menu():
    opcao = 0
    primeiro = 1
    segundo = 2
    terceiro = 3
    quarto = 4
    quinto = 5

# MENU_PRINCIPAL---------------------------------------------------
    print("")
    print(" -----------Jogo da Forca---------------\n")

    while opcao != 3:
        print('''    
            [ 1 ] Tema
            [ 2 ] Créditos
            [ 3 ] Fechar jogo\n''')

        opcao = int(input("Escolha uma opção: "))
        print("\n")

# TEMAS------------------------------------------------------------
        if opcao == 1:

            while opcao != 6:
                print('''            
                  [ 1 ] Filmes
                  [ 2 ] Profissões
                  [ 3 ] Objetos
                  [ 4 ] Países
                  [ 5 ] Estados do Brasil\n
                  [ 6 ] Voltar ao Menu Principal\n''')

                opcao = int(input("Escolha uma opção: "))
                print("\n")

                if opcao == 1:
                    print("TEMA: FILMES")
                    jogo("1")

                if opcao == 2:
                    print("TEMA: PROFISSÕES")
                    jogo("2")
                if opcao == 3:
                    print("TEMA: OBJETOS")
                    jogo("3")
                if opcao == 4:
                    print("TEMA: PAÍSES")
                    jogo("4")
                if opcao == 5:
                    print("TEMA: ESTADOS DO BRASIL")
                    jogo("5")
                if opcao == 6:
                    print("Voltar para o menu principal")
                    menu()

            else:
                print("Opção inválida!")

                int(input())

            print("-------------------------------------\n")


# CREDITOS---------------------------------------------------------
        elif opcao == 2:
            print("-------------Créditos---------------\n")
            print("-----Equipe de Desenvolvimento------\n")

            print("- Jorge Miguel Choairy - 2022111510030@iesp.edu.br")
            print("- Thomaz Choairy Germano - 2022111510037@iesp.edu.br")
            print("- Josilene Marques de Santana - 2022111510014@iesp.edu.br")
            print("- Duwarleu Almeida da Silva - 2022111510015@iesp.edu.br")
            print("- Silvio Claudio Custódio - 2022111510057@iesp.edu.br")
            print("- Cícero de Sousa Lacerda -  2022111510056@iesp.edu.br\n")

            print("------------Colaboradores------------\n")
            print("- Thiago Vasconcelos Costa Freire")
            print("- UNIESP - João Pessoa\n")

            print("-------------------------------------\n")

# FECHAR_PROGRAMA--------------------------------------------------
        elif opcao == 3:
            print("Programa finalizado")

        else:
            print("Opção inválida!")


def jogo(tema):
    alfabeto = list("abcdefghijklmnopqrstuvwxyzáéíóúãõâêôçABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÃÂÊÔÇ")
    jogarNovamente = " "

    forca = """
      _______
            !
            !"""

    nada = """

      """
    cabeça = """
            O


      ❤ ❤ ❤ ❤ ❤ ❤"""
    torço = """
            O
            I


      ❤ ❤ ❤ ❤ ❤"""
    braço_esquerdo = """
            O
           /I


      ❤ ❤ ❤ ❤"""
    braço_direito = """
            O
           /I\\


      ❤ ❤ ❤"""
    perna_esquerda = """
            O
           /I\\
           /


      ❤ ❤"""
    perna_direita = """
            O
           /I\    
           / \\


      ❤"""

    forca_partes = [nada, cabeça, torço, braço_esquerdo, braço_direito, perna_esquerda, perna_direita]

    palavra = random.choice(pegarTema(tema)).upper()

    tentativas = 0

    letras_erradas = " "
    letras_certas = " "
    letra_oculta = "_ " * len(palavra)

    acertos = 0
    erros = 0

    print("")
    print("TEMA ESCOLHIDO:" + tema)
    print("Você tem 7 tentativas")
    print("Boa Sorte!\n")

# print(palavra) #----------------------------------------------------------------------

    while tentativas != len(palavra) and erros < 7:
        letra_oculta = " "

        for letra in palavra:
            if letra in letras_certas:
                letra_oculta += letra
            else:
                letra_oculta += "_ "

        print(forca + forca_partes[erros])
        print(letra_oculta)
        print("LETRAS CERTAS:" + letras_certas)
        print("LETRAS ERRADAS:" + letras_erradas)

        print("")

        letra = input("Escolha uma letra ou digite [MENU] para voltar ao menu principal: ").upper()
        if letra == "MENU":
            print("")
            print("Voltando ao menu principal")
            menu()
            break
        if letra in letras_certas + letras_erradas:
            print("")
            print("Essa letra já foi digitada, tente outra!")
            continue
        if letra not in alfabeto:
            print("Você não digitou uma letra, tente novamente!")
            continue
        if letra in palavra:
            print("A letra (" + letra + ") esta certa!\n")
            letras_certas += letra + " "
            acertos += palavra.count(letra)
            acertou = True

            for letra in palavra:
                if letra not in letras_certas:
                    acertou = False
            if acertou:
                print("Parabéns você ACERTOU a palavra, a palavra era: ", palavra)
                while jogarNovamente != "n":
                    opcao = input(
                        "\nDeseja jogar novamente ? Digite [S] para Sim e [N] para voltar ao menu principal: ").upper()
                    if opcao == "S":
                        letras_erradas = " "
                        letras_certas = " "
                        letra_oculta = "_ " * len(palavra)
                        palavra = pegarTema(tema)
                        break
                    if opcao == "N":
                        print("Voltando ao menu principal")
                        menu()
                        break
        else:
            print("A letra (" + letra + ") não faz parte da palavra escolhida!\n")
            tentativas += 1
            letras_erradas += letra + ""
            erros += 1

    else:
        print("Você errou a palavra, a palavra era: " + palavra)
        while jogarNovamente != "n":
            opcao = input("\nDeseja jogar novamente ? Digite [S] para Sim e [N] para voltar ao menu principal: ").upper()
            if opcao == "S":
                letras_erradas = " "
                letras_certas = " "
                letra_oculta = "_ " * len(palavra)
                palavra = random.choice(pegarTema(tema))
                break
            if opcao == "N":
                print("Voltando ao menu principal")
                menu()
                break


def pegarTema(tema):
    if tema == "1":
        filmes = ["Orgulho e Preconceito", "De volta para o futuro", "Jurassic park", "Toy Story", " Star Wars", "Curtindo a vida adoidado", "O iluminado", "Clube da luta", "Harry Potter", "Senhor dos Aneis", "Matrix", "Perdido em Marte", " Mortal Kombat", "Os Vingadores", "Os Incriveis", "Meu malvado favorito", "Velozes e Furiosos", "Interestelar"]
        return filmes
    if tema == "2":
        profissoes = ["advogado", "açougueiro", "arquiteto", "agente", "agricultor", "analista", "vigilante", "garçom",
                      "tradutor", "vendedor", "ilustrador", "gerente", "historiador", "inspetor", "zelador",
                      "zootecnista", "marinheiro", "soldado", "carpinteiro", "mensageiro", "barman", "laqueador",
                      "marceneiro", "modelo", "motorista"]
        return profissoes
    if tema == "3":
        objetos = ["borracha", "caderno", "caneta", "cadeira", "celular", "apagador", "almofada", "bandeira", "boneca",
                   "caneca", "capacete", "disquete", "dobradiça", "escova", "etiqueta", "extintor"]
        return objetos
    if tema == "4":
        paises = ["Brasil", "Argentina", "Venezuela", "Alemanha", "Estados Unidos", "Barbados", "Chipre", "Equador",
                  "Costa Rica", "Espanha", "Filipinas", "Guatemala", "Iraque", "Irlanda", "Israel", "Jamaica",
                  "Marrocos", "Montenegro", "Portugal", "Inglaterra", "Turquia", "Viatname", "Suriname",
                  "Coreia do Sul", "Coreia do Norte"]
        return paises
    if tema == "5":
        estados = ["Minas Gerais", "Rio Grande do Sul", "Santa Catarina", "Rio de Janeiro", "Pernambuco", "Mato Grosso",
                   "Amazonas", "Sergipe", "Rio Grande do Norte", "Alagoas", "Mato Grosso do Sul", "Roraima",
                   "Tocantins"]
        return estados


menu()
