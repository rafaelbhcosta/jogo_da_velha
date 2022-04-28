import pygame

pygame.init()
x = 400
y = 300
velocidade = 10

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption('Jokempo')


abertura = True
while abertura:

    # Isso é uma condição para a tela não travar, cria um periodo de recarga da tela
    pygame.time.delay(25)

        # Essa função cria uma detecção de evento, no caso para parar a tela caso clique no X (sair)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            abertura = False
        
    #comandos que determinam a movimentação do circulo
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade
          

    # Sempre que o evento FOR se repetir a tela atualiza o fundo dela para essa cor
    janela.fill((0,0,0))

    # A primeira função apenas desenha um circulo na tela, a outra atualiza para o circulo aparecer
    pygame.draw.circle(janela, (0,255,0), (x,y), 50)
    pygame.display.update()

pygame.quit