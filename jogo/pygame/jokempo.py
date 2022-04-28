import pygame
pygame.init()

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption('Jokempo')

abertura = True
while abertura:

    # Isso é uma condição para a tela não travar, cria um periodo de recarga da tela
    pygame.time.delay(50)

    # Essa função cria uma detecção de evento, no caso para parar a tela caso clique no X (sair)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            abertura = False

    # A primeira função apenas desenha um circulo na tela, a outra atualiza para o circulo aparecer
    pygame.draw.circle(janela, (0,255,0), (400,300), 50)
    pygame.display.update()

pygame.quit