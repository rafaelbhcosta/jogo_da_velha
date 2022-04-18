import random
import defs

rep = True

while rep:
    computador = random.randint(1,3)
    defs.linha()
    print('Olá jogador, seja bem vindo ao jogo da velha')
    defs.linha()
    escolha = int(input('Faça sua escolha\n1 - Pedra\n2 - Papel\n3 - Tesoura\nEscolha: '))
    