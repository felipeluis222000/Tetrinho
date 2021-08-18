import pygame
import random
import os

# Variaveis Globais
LARGURA = 900
ALTURA = 700
LARGURA_GRADE = 300
ALTURA_GRADE = 600
TOPO_X = (LARGURA/2)-(LARGURA_GRADE/2)
TOPO_Y = 50
COLISAO_Y = [[] for _ in range(21)]
COLISAO_Y[0].append(620)

for diretorios,subpastas,arquivos in os.walk("fontes"):
    FONTES = arquivos

pygame.font.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tetrinho")

def Bloquinhos(x,y):
    formatos1 = [[(x,y),(x+30,y),(x,y+30),(x+30,y+30),(255,255,255)]]

    formatos2 = [[(x,y),(x,y+30),(x,y+60),(x,y+90), (255,255,255)],
                 [(x-30,y),(x,y),(x+30,y),(x+60,y), (255,255,255)]]

    formatos3 = [[(x-30,y),(x,y),(x,y+30),(x+30,y+30),(255,255,255)],
                 [(x,y+30),(x+30,y+30),(x,y+60),(x+30,y),(255,255,255)]]

    formatos4 = [[(x-30,y+30),(x,y),(x,y+30),(x+30,y),(255,255,255)],
                 [(x,y),(x,y+30),(x+30,y+30),(x+30,y+60),(255,255,255)]]

    formatos5 = [[(x,y),(x+30,y),(x,y+30),(x+60,y),(255,255,255)],
                 [(x,y),(x+30,y),(x+30,y+30),(x+30,y+60),(255,255,255)],
                 [(x-30,y+30),(x+30,y),(x,y+30),(x+30,y+30),(255,255,255)],
                 [(x,y),(x,y+30),(x,y+60),(x+30,y+60),(255,255,255)]]

    formatos6 = [[(x,y),(x+30,y),(x+60,y+30),(x+60,y),(255,255,255)],
                 [(x,y+60),(x+30,y),(x+30,y+30),(x+30,y+60),(255,255,255)],
                 [(x,y),(x+30,y+30),(x,y+30),(x+60,y+30),(255,255,255)],
                 [(x,y),(x,y+30),(x,y+60),(x+30,y),(255,255,255)]]

    formatos7 = [[(x-30,y),(x,y),(x,y+30),(x+30,y),(255,255,255)],
                 [(x-30,y+30),(x,y),(x,y+30),(x,y+60),(255,255,255)],
                 [(x-30,y+30),(x,y),(x,y+30),(x+30,y+30),(255,255,255)],
                 [(x,y),(x,y+30),(x,y+60),(x+30,y+30),(255,255,255)]]

    lista_de_formatos = [formatos1,formatos2,formatos3,formatos4,formatos5,formatos6,formatos7]
    return random.choice(lista_de_formatos)

def Titulo(fontes):
    cor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    fonte = random.choice(fontes)
    titulo = pygame.font.Font("fontes/{}".format(fonte), 50)
    titulo2 = titulo.render("Tetrinho", 1, (cor))
    return titulo2

def Mapa(tela, x, y, largura, altura):
    for i in range(10):
        pygame.draw.line(tela, (128,128,128), (x+(i*30),y),(x+(i*30),altura+50))
    for i in range(20):
        pygame.draw.line(tela, (128,128,128), (x,y+(i*30)), (x+300,y+(i*30)))
    pygame.draw.rect(tela, (72,61,139), (x,y, largura, altura), 3)

def Movimentacao(bloquinho, sentido):
    final = []
    if sentido == "baixo":
        for i in range(len(bloquinho)):
            final.append([])
            for j in range(len(bloquinho[i])-1):
                posicao = list(bloquinho[i][j])
                final[i].append((posicao[0],posicao[1]+30))
        for i in range(0,len(final)):
            final[i].append(bloquinho[i][-1])
        return final

    elif sentido == "direita":
        for i in range(len(bloquinho)):
            final.append([])
            for j in range(len(bloquinho[i])-1):
                posicao = list(bloquinho[i][j])
                final[i].append((posicao[0]+30,posicao[1]))
        for i in range(0,len(final)):
            final[i].append(bloquinho[i][-1])
        return final

    elif sentido == "esquerda":
        for i in range(len(bloquinho)):
            final.append([])
            for j in range(len(bloquinho[i])-1):
                posicao = list(bloquinho[i][j])
                final[i].append((posicao[0]-30,posicao[1]))
        for i in range(0,len(final)):
            final[i].append(bloquinho[i][-1])
        return final
    elif sentido == "cima":
        for i in range(len(bloquinho)):
            final.append([])
            for j in range(len(bloquinho[i]) - 1):
                posicao = list(bloquinho[i][j])
                final[i].append((posicao[0], posicao[1] - 30))
        for i in range(0, len(final)):
            final[i].append(bloquinho[i][-1])
        return final

def Checar_Movimento_Lateral(index,bloquinho):
    while True:
        if bloquinho[index][0][0] < 300:
            bloquinho = Movimentacao(bloquinho, "direita")
        elif bloquinho[index][3][0] > 570:
            bloquinho = Movimentacao(bloquinho, "esquerda")
        else:
            return bloquinho

def Main(tela):
    global FONTES
    global LARGURA
    global ALTURA
    global LARGURA_GRADE
    global ALTURA_GRADE
    global TOPO_X
    global TOPO_Y

    index = 0
    tamanho = 30
    contador_segundos = 0
    rodando = True
    titulo = Titulo(FONTES)
    bloquinho = Bloquinhos(TOPO_X+120,TOPO_Y)
    while rodando:
        clock.tick(30)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                return rodando
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s:
                    bloquinho = Movimentacao(bloquinho, "baixo")
                elif evento.key == pygame.K_d:
                    bloquinho = Movimentacao(bloquinho, "direita")
                elif evento.key == pygame.K_a:
                    bloquinho = Movimentacao(bloquinho, "esquerda")
                elif evento.key == pygame.K_SPACE:
                    if index + 1 < len(bloquinho):
                        index += 1
                    else:
                        index = 0


        if contador_segundos == 30:
            bloquinho = Movimentacao(bloquinho, "baixo")
            titulo = Titulo(FONTES)
            contador_segundos = 0

        bloquinho = Checar_Movimento_Lateral(index,bloquinho)

        tela.fill((0, 0, 0))
        tela.blit(titulo, (TOPO_X + (TOPO_X/2)-(titulo.get_width()/2),5))
        for i in range(len(bloquinho[index])-1):
            pygame.draw.rect(tela, bloquinho[index][4],(bloquinho[index][i][0],bloquinho[index][i][1], tamanho, tamanho),0)
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