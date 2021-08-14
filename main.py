import pygame
import random

# Variaveis Globais
LARGURA = 900
ALTURA = 700
LARGURA_GRADE = 300
ALTURA_GRADE = 600
TOPO_X = (LARGURA/2)-(LARGURA_GRADE/2)
TOPO_Y = 50



pygame.font.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tetris")

def Mapa(tela, x, y, largura, altura):
    for i in range(10):
        pygame.draw.line(tela, (128,128,128), (x+(i*30),y),(x+(i*30),altura+50))
    for i in range(20):
        pygame.draw.line(tela, (128,128,128), (x,y+(i*30)), (x+300,y+(i*30)))
    pygame.draw.rect(tela, (72,61,139), (x,y, largura, altura), 3)

def Main(tela):
    global LARGURA
    global ALTURA
    global LARGURA_GRADE
    global ALTURA_GRADE
    global TOPO_X
    global TOPO_Y

    tamanho = 30
    x = (LARGURA/2)-(tamanho/2)
    y = 50
    contador_segundos = 0
    rodando = True

    while rodando:
        clock.tick(30)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s:
                    y += 30
                if evento.key == pygame.K_d:
                    x += 30
                if evento.key == pygame.K_a:
                    x -= 30

        if contador_segundos == 30:
            y += 30
            contador_segundos = 0

        tela.fill((0, 0, 0))
        pygame.draw.rect(tela, (127,0,0), ((x-(tamanho/2)), y, 30, 30), 0)
        Mapa(tela, TOPO_X, TOPO_Y, LARGURA_GRADE, ALTURA_GRADE)
        pygame.display.flip()
        contador_segundos = contador_segundos + 1

def Menu(tela):
    rodando = True
    inicair = pygame.font.SysFont("cambria", 60)
    texto = inicair.render("Aperte espaço para iniciar", 1, (255,255,255))

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    rodando = Main(tela)

        tela.fill((0,0,0))
        tela.blit(texto, ((LARGURA/2)-(texto.get_width()/2), (ALTURA/2)-(texto.get_height()/2)))
        pygame.display.flip()

Menu(tela)