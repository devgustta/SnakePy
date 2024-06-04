import sys
import time

import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
x = largura / 2
y = altura / 2

# Variáveis para a posição do retângulo azul
x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0
# Configurando a fonte
font = pygame.font.SysFont("arial", 40, True, True)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

# Lista para armazenar os segmentos da cobra
cobra = [(x,y)]

def verifica_colisao():
    gameOver = font.render(f'Gamer Over', True, (255, 255, 255))
    tela.blit(gameOver, (150, 180))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    mensagem = f"Pontos: {pontos}"
    # Formatando o nosso texto
    texto_formatado = font.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x -= 20
    if pygame.key.get_pressed()[K_d]:
        x += 20
    if pygame.key.get_pressed()[K_w]:
        y -= 20
    if pygame.key.get_pressed()[K_s]:
        y += 20

    # Atualiza a posição do retângulo vermelho
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 30, 40))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 30, 40))

    # Verifica as colisões nas bordas da tela
    if x < 0:
       # x = 0
       verifica_colisao()
    if x > largura - 30:
       # x = largura - 40
       verifica_colisao()
    if y < 0:
      #  y = 0
       verifica_colisao()
    if y > altura - 30:
     #   y = altura - 50
       verifica_colisao()

    # Adiciona a nova posição da cabeça da cobra na posição zero e a cabeça vai para segunda posição e assim por diante
    cobra.insert(0,(x,y))

    # A cada frame é adicionado um segmento ao corpo então
    # Removemos o ultimo segmento, a menos que tenhamos acabado de comer uma maçã
    if len(cobra) > pontos + 1:
        cobra.pop()

    #Desenha os segmentos da cobra
    for segmentos in cobra:
        #           onde mostrar,   cor,                     posição e           tamanho
        pygame.draw.rect(tela, (255,0,0), (segmentos[0], segmentos[1],40,50))


    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1


    # Mostrando a mensagem na tela
    tela.blit(texto_formatado, (440, 10))

    pygame.display.update()
