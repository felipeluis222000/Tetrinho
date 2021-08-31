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
RANKING = {
    "Jogadores": ["Felipe","","","","","","","","",""],
    "Pontos": [10,0,0,0,0,0,0,0,0,0]
}

for diretorios,subpastas,arquivos in os.walk("fontes_uuiii"):
    FONTES = arquivos

pygame.font.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tetrinho")

def Bloquinhos(x,y):
    formatos1 = [[(x,y-90,(0,0,205)),(x+30,y-90,(0,0,205)),(x,y-120,(0,0,205)),(x+30,y-120,(0,0,205))]]

    formatos2 = [[(x,y-30,(0,128,0)),(x,y-60,(0,128,0)),(x,y-90,(0,128,0)),(x,y-120 ,(0,128,0))],
                 [(x,y-30,(0,128,0)),(x+30,y-30,(0,128,0)),(x+60,y-30,(0,128,0)),(x+90,y-30,(0,128,0))]]

    formatos3 = [[(x,y-90,(148,0,211)),(x+30,y-90,(148,0,211)),(x+30,y-120,(148,0,211)),(x+60,y-120,(148,0,211))],
                 [(x+30,y-60,(148,0,211)),(x+30,y-90,(148,0,211)),(x,y-90,(148,0,211)),(x,y-120,(148,0,211))]]

    formatos4 = [[(x+60,y-90,(255,20,147)),(x+30,y-90,(255,20,147)),(x+30,y-120,(255,20,147)),(x,y-120,(255,20,147))],
                 [(x,y-60,(255,20,147)),(x,y-90,(255,20,147)),(x+30,y-90,(255,20,147)),(x+30,y-120,(255,20,147))]]

    formatos5 = [[(x,y-90,(255,0,0)),(x+30,y-90,(255,0,0)),(x+60,y-90,(255,0,0)),(x+30,y-120,(255,0,0))],
                 [(x,y-30,(255,0,0)),(x,y-60,(255,0,0)),(x+30,y-60,(255,0,0)),(x,y-90,(255,0,0))],
                 [(x+30,y-90,(255,0,0)),(x+30,y-120,(255,0,0)),(x+60,y-120,(255,0,0)),(x,y-120,(255,0,0))],
                 [(x+30,y-30,(255,0,0)),(x+30,y-60,(255,0,0)),(x,y-60,(255,0,0)),(x+30,y-90,(255,0,0))]]

    formatos6 = [[(x,y-90,(255,69,0)),(x,y-120,(255,69,0)),(x+30,y-90,(255,69,0)),(x+60,y-90,(255,69,0))],
                 [(x,y-60,(255,69,0)),(x,y-90,(255,69,0)),(x,y-120,(255,69,0)),(x+30,y-120,(255,69,0))],
                 [(x,y-120,(255,69,0)),(x+30,y-120,(255,69,0)),(x+60,y-120,(255,69,0)),(x+60,y-90,(255,69,0))],
                 [(x,y-60,(255,69,0)),(x+30,y-60,(255,69,0)),(x+30,y-90,(255,69,0)),(x+30,y-120,(255,69,0))]]

    formatos7 = [[(x,y-90,(255,255,0)),(x,y-120,(255,255,0)),(x+30,y-120,(255,255,0)),(x+60,y-120,(255,255,0))],
                 [(x+30,y-60,(255,255,0)),(x+30,y-90,(255,255,0)),(x+30,y-120,(255,255,0)),(x,y-120,(255,255,0))],
                 [(x,y-90,(255,255,0)),(x+30,y-90,(255,255,0)),(x+60,y-90,(255,255,0)),(x+60,y-120,(255,255,0))],
                 [(x,y-60,(255,255,0)),(x+30,y-60,(255,255,0)),(x,y-90,(255,255,0)),(x,y-120,(255,255,0))]]


    lista_de_formatos = random.choice([[formatos1,"1"],[formatos2,"2"],[formatos3,"3"],[formatos4,"4"],[formatos5,"5"],[formatos6,"6"],[formatos7,"7"]])
    return lista_de_formatos[0],lista_de_formatos[1]

def Titulo(fontes,indicacao,pontos=None):
    global RANKING
    frases = ["Tetrinho","Próximo bloco","Pontuação: {}".format(pontos), "Maior pontuação: {}".format(pontos)]
    cor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    fonte = random.choice(fontes)
    if indicacao == 0:
        titulo = pygame.font.Font("fontes_uuiii/{}".format(fonte), 50)
        titulo2 = titulo.render(frases[0], 1, (cor))
    elif indicacao == 1:
        titulo = pygame.font.SysFont("Lucida Console", 30)
        titulo2 = titulo.render(frases[1], 1, (255,255,255))
    elif indicacao == 2:
        titulo = pygame.font.SysFont("Lucida Console", 20)
        titulo2 = titulo.render(frases[2], 1, (255, 255, 255))
    elif indicacao == 3:
        titulo = pygame.font.SysFont("Lucida Console", 20)
        titulo2 = titulo.render(frases[3], 1, (255, 255, 255))
    return titulo2

def Mapa(tela, x, y, largura, altura):
    for i in range(10):
        pygame.draw.line(tela, (169,169,169), (x+(i*30),y),(x+(i*30),altura+50))
    for i in range(20):
        pygame.draw.line(tela, (169,169,169), (x,y+(i*30)), (x+300,y+(i*30)))
    pygame.draw.rect(tela, (75,0,130), (x,y, largura, altura), 3)

def Desenhando_prox_bloquinho(prox_bloquinho,prox_formato):
    for i in range(len(prox_bloquinho[0])):
        pygame.draw.rect(tela, prox_bloquinho[0][i][-1],(prox_bloquinho[0][i][0]+300,prox_bloquinho[0][i][1]+320,30,30), 0)
    if prox_formato == "1":
        for i in range(3):
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+300,prox_bloquinho[0][0][1]+(i*30)+290),(prox_bloquinho[0][0][0]+360,prox_bloquinho[0][0][1]+(i*30)+290))
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+290),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+350))
    elif prox_formato == "2":
        for i in range(5):
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+300,prox_bloquinho[0][0][1]+(i*30)+230),(prox_bloquinho[0][0][0]+330,prox_bloquinho[0][0][1]+(i*30)+230))
        for i in range(2):
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+230),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+350))
    elif prox_formato == "3":
        for i in range(2):
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+330,prox_bloquinho[0][0][1]+(i*30)+290),(prox_bloquinho[0][0][0]+390,prox_bloquinho[0][0][1]+(i*30)+290))
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+300,prox_bloquinho[0][0][1]+(i*30)+320),(prox_bloquinho[0][0][0]+360,prox_bloquinho[0][0][1]+(i*30)+320))
        for i in range(3):
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+320),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+350))
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+(i*30)+330,prox_bloquinho[0][0][1]+290),(prox_bloquinho[0][0][0]+(i*30)+330,prox_bloquinho[0][0][1]+320))
    elif prox_formato == "4":
        for i in range(3):
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+(i*30)+240,prox_bloquinho[0][0][1]+290),(prox_bloquinho[0][0][0]+(i*30)+240,prox_bloquinho[0][0][1]+320))
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+(i*30)+270,prox_bloquinho[0][0][1]+320),(prox_bloquinho[0][0][0]+(i*30)+270,prox_bloquinho[0][0][1]+350))
        for i in range(2):
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+270,prox_bloquinho[0][0][1]+(i*30)+320),(prox_bloquinho[0][0][0]+330,prox_bloquinho[0][0][1]+(i*30)+320))
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+240,prox_bloquinho[0][0][1]+(i*30)+290),(prox_bloquinho[0][0][0]+300,prox_bloquinho[0][0][1]+(i*30)+290))
    elif prox_formato == "5":
        for i in range(2):
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+(i*30)+330,prox_bloquinho[0][0][1]+290),(prox_bloquinho[0][0][0]+(i*30)+330,prox_bloquinho[0][0][1]+320))
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+330,prox_bloquinho[0][0][1]+(i*30)+290),(prox_bloquinho[0][0][0]+360,prox_bloquinho[0][0][1]+(i*30)+290))
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+300,prox_bloquinho[0][0][1]+(i*30)+320),(prox_bloquinho[0][0][0]+390,prox_bloquinho[0][0][1]+(i*30)+320))
        for i in range(4):
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+320),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+350))
    elif prox_formato == "6":
        for i in range(2):
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+290),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+320))
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+300,prox_bloquinho[0][0][1]+(i*30)+320),(prox_bloquinho[0][0][0]+390,prox_bloquinho[0][0][1]+(i*30)+320))
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+300,prox_bloquinho[0][0][1]+(i*30)+290),(prox_bloquinho[0][0][0]+330,prox_bloquinho[0][0][1]+(i*30)+290))
        for i in range(4):
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+320),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+350))
    elif prox_formato == "7":
        for i in range(4):
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+290),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+320))
        for i in range(2):
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+320),(prox_bloquinho[0][0][0]+(i*30)+300,prox_bloquinho[0][0][1]+350))
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+300,prox_bloquinho[0][0][1]+(i*30)+290),(prox_bloquinho[0][0][0]+390,prox_bloquinho[0][0][1]+(i*30)+290))
            pygame.draw.line(tela,(169,169,169),(prox_bloquinho[0][0][0]+300,prox_bloquinho[0][0][1]+(i*30)+320),(prox_bloquinho[0][0][0]+330,prox_bloquinho[0][0][1]+(i*30)+320))

def Vacuos(x,y):
    espacinhos = [[] for _ in range(0,21)]
    for i in range(10):
        espacinhos[0].append((x+i*30 ,y-30,(0,0,0)))
    for i in range(10):
        espacinhos[0].append((x+i*30,y+30*20,(0,0,0)))
    for i in range(20):
        espacinhos[0].append((x-30,y+i*30,(0,0,0)))
    for i in range(20):
        espacinhos[0].append((x+30*10,y+i*30,(0,0,0)))
    return espacinhos

def Movimentacao(bloquinho, sentido):
    final = []
    if sentido == "baixo":
        for i in range(len(bloquinho)):
            final.append([])
            for j in range(len(bloquinho[i])):
                posicao = list(bloquinho[i][j])
                final[i].append((posicao[0],posicao[1]+30,posicao[2]))

        return final

    elif sentido == "direita":
        for i in range(len(bloquinho)):
            final.append([])
            for j in range(len(bloquinho[i])):
                posicao = list(bloquinho[i][j])
                final[i].append((posicao[0]+30,posicao[1],posicao[2]))
        return final

    elif sentido == "esquerda":
        for i in range(len(bloquinho)):
            final.append([])
            for j in range(len(bloquinho[i])):
                posicao = list(bloquinho[i][j])
                final[i].append((posicao[0]-30,posicao[1],posicao[2]))
        return final
    elif sentido == "cima":
        for i in range(len(bloquinho)):
            final.append([])
            for j in range(len(bloquinho[i])):
                posicao = list(bloquinho[i][j])
                final[i].append((posicao[0], posicao[1] - 30,posicao[2]))
        return final
    else:
        return bloquinho

def Checar_Movimentos(index,bloquinho,espacinhos,sentido,formato=None,contador=0):
    if sentido == "espaco":
        if formato == "2" and index == 1:
            limite = 3
        else:
            limite = 1
        contador = contador
        while contador <= limite:
            for i in range(len(espacinhos)):
                for j in range(len(espacinhos[i])):
                    for i2 in range(len(bloquinho[index])):
                        if bloquinho[index][i2][0] == espacinhos[i][j][0] and bloquinho[index][i2][1] == espacinhos[i][j][1]:
                            contador += 1
                            bloquinho = Movimentacao(bloquinho, "esquerda")
                            bloquinho,trava = Checar_Movimentos(index,bloquinho,espacinhos,sentido,formato=formato,contador=contador)
                            if trava:
                                return bloquinho,True
                            else:
                                break
            return bloquinho,False
        return bloquinho,True

    else:
        passo_falso = Movimentacao(bloquinho, sentido)
        for i in range(len(espacinhos)):
            for j in range(len(espacinhos[i])):
                for i2 in range(len(passo_falso[index])):
                    if passo_falso[index][i2][0] == espacinhos[i][j][0] and passo_falso[index][i2][1] == espacinhos[i][j][1]:
                        return True

def Pontos(espacinhos,pontuacao, multiplicador=0):
    multiplicador = 0
    for i in range(1,len(espacinhos)):
        if len(espacinhos[i]) == 10:
            multiplicador += 1
            descida = espacinhos[1:i]
            descida.insert(0,[])
            espacinhos.remove(espacinhos[i])
            espacinhos.insert(1,[])
            descida = Movimentacao(descida, "baixo")
            for i in range(len(descida)):
                espacinhos[i+1] = descida[i]

    pontuacao += 10*multiplicador
    return espacinhos,pontuacao

def Game_over(espacinhos):
    if espacinhos[1]:
        return True
    else:
        return False

def Main(tela):
    global FONTES
    global LARGURA
    global ALTURA
    global LARGURA_GRADE
    global ALTURA_GRADE
    global TOPO_X
    global TOPO_Y
    global RANKING


    index = 0
    tamanho = 30
    contador_segundos = 0
    rodando = True
    pontuacao = 0
    titulo = Titulo(FONTES,0)
    proximo_bloco_texto = Titulo(FONTES,1)
    espacinhos = Vacuos(TOPO_X,TOPO_Y)
    bloquinho,formato = Bloquinhos(TOPO_X+120,TOPO_Y+120)
    prox_bloquinho,prox_formato = Bloquinhos(TOPO_X+120,TOPO_Y+120)
    while rodando:
        texto_maior_pontuacao = Titulo(FONTES, 3, pontos=RANKING["Pontos"][0])
        texto_pontuacao = Titulo(FONTES, 2, pontos=pontuacao)
        clock.tick(30)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                return rodando
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s:
                    trava = Checar_Movimentos(index, bloquinho, espacinhos, "baixo")
                    if not trava:
                        bloquinho = Movimentacao(bloquinho, "baixo")
                elif evento.key == pygame.K_d:
                    trava = Checar_Movimentos(index, bloquinho, espacinhos, "direita")
                    if not trava:
                        bloquinho = Movimentacao(bloquinho, "direita")
                elif evento.key == pygame.K_a:
                    trava = Checar_Movimentos(index,bloquinho,espacinhos,"esquerda")
                    if not trava:
                        bloquinho = Movimentacao(bloquinho, "esquerda")
                elif evento.key == pygame.K_SPACE:
                    bloquinho2 = bloquinho
                    if index + 1 < len(bloquinho):
                        index += 1
                        bloquinho,trava = Checar_Movimentos(index,bloquinho,espacinhos,"espaco",formato=formato)
                        if trava:
                            bloquinho = bloquinho2
                            index -= 1

                    else:
                        index = 0
                        bloquinho,trava = Checar_Movimentos(index,bloquinho,espacinhos,"espaco",formato=formato)
                        if trava:
                            bloquinho = bloquinho2
                            index = len(bloquinho)-1

        if contador_segundos == 30:
            trava = Checar_Movimentos(index, bloquinho, espacinhos, "baixo")
            if not trava:
                bloquinho = Movimentacao(bloquinho, "baixo")
            else:
                for i in range(len(bloquinho[index])):
                    espacinhos[int((bloquinho[index][i][1]-20)/30)].append((int(bloquinho[index][i][0]),int(bloquinho[index][i][1]),bloquinho[index][i][-1]))
                espacinhos, pontuacao = Pontos(espacinhos, pontuacao)
                game_over = Game_over(espacinhos)
                if game_over:
                    rodando = False
                    Tela_GO(tela,clock)
                bloquinho,formato = prox_bloquinho,prox_formato
                prox_bloquinho,prox_formato = Bloquinhos(TOPO_X+120,TOPO_Y+120)
                index = 0

            titulo = Titulo(FONTES,0)
            contador_segundos = 0

        tela.fill((0, 0, 0))
        for i in range(len(bloquinho[index])):
            pygame.draw.rect(tela, bloquinho[index][i][-1],(bloquinho[index][i][0],bloquinho[index][i][1], tamanho, tamanho),0)
        for i in range(len(espacinhos)):
            for j in range(len(espacinhos[i])):
                pygame.draw.rect(tela,espacinhos[i][j][-1],(espacinhos[i][j][0],espacinhos[i][j][1],tamanho,tamanho))
        tela.blit(titulo, (TOPO_X + (TOPO_X/2)-(titulo.get_width()/2),5))
        tela.blit(proximo_bloco_texto, (600+150-(proximo_bloco_texto.get_width()/2),325))
        tela.blit(texto_maior_pontuacao, (0,0))
        tela.blit(texto_pontuacao,(900-texto_pontuacao.get_width()-30,680))
        Desenhando_prox_bloquinho(prox_bloquinho,prox_formato)
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

def Tela_GO(tela,clock):
    rodando = True
    subida = 0
    contador = 0
    fonte = pygame.font.SysFont("Lucida Console",60)
    texto = fonte.render("Game Over",False,(255,255,255))
    fonte2 = pygame.font.SysFont("Lucida Console", 20)
    while rodando:
        clock.tick(80)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    rodando = False
                    Menu(tela)
        tela.fill((0,0,0))
        if 800 - subida > 350 - (texto.get_height()/2):
            subida += 1
        else:
            contador += 1
            if contador <= 30:
                cor = (255,255,255)
            elif contador >= 30 and contador <= 60:
                cor = (0,0,0)
            else:
                contador = 0
            texto2 = fonte2.render("Aperte espaço para voltar ao menu", False, cor)
            tela.blit(texto2, (450 - (texto2.get_width() / 2), 900 - subida))
        tela.blit(texto, (450 - (texto.get_width() / 2), 800 - subida))
        pygame.display.flip()

Menu(tela)