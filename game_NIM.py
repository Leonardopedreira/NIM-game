def computador_escolhe_jogada(n,m):
    computador = 1

    while computador!=m:
        if (n-computador)%(m+1)==0:
            return computador
        else:
            computador+=1
    
    print ("O computador tirou", computador, "peça(s).")
    restantePC = n - computador
    print ("Agora restam apenas", restantePC, "peça(s) no tabuleiro.")
    return computador

def usuario_escolhe_jogada(n,m):
    jogador = int(input("Quantas peças você vai tirar? "))
    if jogador >= m:
        print("Oops! Jogada inválida! Tente de novo.")
        usuario_escolhe_jogada(n,m)
    
    print ("Você tirou", jogador, "peça(s).")
    restanteJ = n - jogador
    print ("Agora restam apenas", restanteJ, "peça(s) no tabuleiro.")
    return jogador


def chamada_peças():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while m >= n:
        print("O limite de peças deve ser menor que a quantidade delas")
        print("Escolha novamente")
        chamada_peças()
    return (n,m)

def metodo_jogadas(n,m):
        if (n%(m+1))==0:
            print("Você começa!")
            usuario_escolhe_jogada(n,m)
            restante = n - jogador
        else:
            print("Computador começa!")
            computador_escolhe_jogada(n,m)
            restante = n - computador
            
        while restante!=0:
            if restante == n - jogador:
                computador_escolhe_jogada(n,m)
            if restante == n - computador:
                usuario_escolhe_jogada(n,m)
        anuncio = print("Fim de jogo! Computador venceu!")
        return anuncio

def campeonato(n,m):
    print("Você escolheu um campeonato")
    print("**** Rodada 1 ****")

    n,m = chamada_peças()

    anuncio = metodo_jogadas(n,m)

    print("**** Rodada 2 ****")

    n,m = chamada_peças()

    anuncio = metodo_jogadas(n,m)

    print("**** Rodada 3 ****")

    n,m = chamada_peças()

    anuncio = metodo_jogadas(n,m)

    print("**** Fim do campeonato! ****")
    print("Placar: Você 0 x 3 Computador")

def partida():
    print("Bem-vindo ao jogo do NIM! Escolha:")

    print("1 - para jogar uma partida isolada: ")
    print("2 - para jogar um campeonato: ")

    a = int(input("Sua opção: "))
    if a == 1:
        print("Você escolheu uma partida isolada")

        print("**** Rodada única ****")

        n,m = chamada_peças()

        anuncio = metodo_jogadas(n,m)
                                
    if a == 2:
        campeonato(n,m)

    if a!=1 and a!=2:
        print("Você escolheu uma opção inválida, por favor, tente novamente")

        partida()
            

    return ()

partida()