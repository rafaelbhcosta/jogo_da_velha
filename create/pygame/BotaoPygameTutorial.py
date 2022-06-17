import pygame


fps = pygame.time.Clock()
largura = 1024
altura = 600

JogoLoop = True


tela = pygame.display.set_mode( [largura , altura] )
pygame.display.set_caption("Tutorial pygame.")

ColorBack = { "azul":[0,132, 252] , "vermelho":[137,28,36]} 



class Botao(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super().__init__(*groups)
        


        self.image = pygame.image.load("data/red_button01.png").convert_alpha()
        self.image = pygame.transform.scale(self.image , [ 190 , 49  ] )
        self.rect = pygame.Rect(190 , 49 , 190 , 49)
        self.rect = self.image.get_rect()

        self.image1 = pygame.image.load("data/red_button01.png").convert_alpha()
        self.image2 = pygame.image.load("data/red_button02.png").convert_alpha()


        self.touche = False

    def update(self):
        self.mouse = pygame.mouse.get_pressed()
        self.MousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(self.MousePos):
            
            if self.mouse[0]:
                self.touche = True
                pygame.mouse.get_rel()
                self.image = self.image2
                
            else:
                self.touche = False
                self.image = self.image1

        pass
    




ButtonGrups = pygame.sprite.Group()


Botton_1 = Botao(ButtonGrups)
Botton_1.rect.center = (512 , 300)

Botton_2 = Botao(ButtonGrups)
Botton_2.rect.center = (250 , 300)


while JogoLoop:
    fps.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            JogoLoop = False

        if Botton_1.touche == True:
            tela.fill( ColorBack["vermelho"] )

        else:
            tela.fill( ColorBack["azul"] )





        
        ButtonGrups.update()
        ButtonGrups.draw(tela)


        pygame.display.update()
pygame.quit()




        
