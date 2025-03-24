import pygame #importar a os jogos
from pygame.locals import * #impotar tudo do submodulo locals
from sys import exit #função para fechar a janela

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            #for pega o evento de saia ao clicar no x
    pygame.display.update()
