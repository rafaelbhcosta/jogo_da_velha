import pygame
pygame.init()

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption('Sudoku')

abertura = True
while abertura:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            abertura = False

pygame.quit