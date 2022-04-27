import random
import defs

rep = True

while rep:
    computador = random.randint(1,3)
    defs.linha()
    print('Olá jogador, seja bem vindo ao jogo da velha')
    defs.linha()
    escolha = int(input('Faça sua escolha\n1 - Pedra\n2 - Papel\n3 - Tesoura\nEscolha: '))
    
    if computador == escolha:
        defs.linha()
        print('Resultado do jogo')
        print(f'Computador: {computador}\nVocê: {escolha}\nEMPATE')
    
    else:
        #Vitórias do jogador
        if escolha == 1 and computador == 3:
            defs.linha()
            escolha = 'Pedra'
            computador = 'Tesoura'
            print('Resultado do jogo')
            print(f'Computador: {computador}\nVocê: {escolha}\nVocê venceu!!')
            
        elif escolha == 2 and computador == 1:
            defs.linha()
            print('Resultado do jogo')
            print(f'Computador: {computador}\nVocê: {escolha}\nVocê venceu!!')
        elif escolha == 3 and computador == 2:
            defs.linha()
            print('Resultado do jogo')
            print(f'Computador: {computador}\nVocê: {escolha}\nVocê venceu!!')

        #Vitórias do computador
        elif computador == 1 and escolha == 3:
            defs.linha()
            print('Resultado do jogo')
            print(f'Computador: {computador}\nVocê: {escolha}\nO cumputador venceu!!')
        elif computador == 2 and escolha == 1:
            defs.linha()
            print('Resultado do jogo')
            print(f'Computador: {computador}\nVocê: {escolha}\nVO cumputador venceu!!')
        elif computador == 3 and escolha == 2:
            defs.linha()
            print('Resultado do jogo')
            print(f'Computador: {computador}\nVocê: {escolha}\nO cumputador venceu!!')