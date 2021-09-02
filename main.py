import pygame
import random
import time
import os

# Variaveis Globais
LARGURA = 900
ALTURA = 700
LARGURA_GRADE = 300
ALTURA_GRADE = 600
TOPO_X = (LARGURA/2)-(LARGURA_GRADE/2)
TOPO_Y = 50
volume = 0.1
RANKING = {
    "Jogadores": ["Felipe","Klara","Jorge","Cauã","Augusto","Thiago","Mateus","Josefa","Ingridi","Julia"],
    "Pontos": [100,90,80,70,60,50,40,30,20,10]
}

for diretorios,subpastas,arquivos in os.walk("fontes_uuiii"):
    FONTES = arquivos

pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tetrinho")

def Barulho(arquivo,volume):
    barulho = pygame.mixer.Sound("sons/{}".format(arquivo))
    barulho.set_volume(volume)
    barulho.play()

def Jogador(tela, clock):
    rodando = True
    fonte = pygame.font.SysFont("Lucida Console", 30)
    fonte2 = pygame.font.SysFont("Lucida Console", 15)
    texto = ""
    texto2 = "Digite seu nome"
    texto3 = "Aperte espaço para jogar"
    seu_nome = fonte.render(texto2, 1, (255,255,255))
    contador = 0

    while rodando:
        clock.tick(80)

        if contador <= 30:
            cor2 = (255, 255, 255)

        elif contador >= 30 and contador <= 60:
            cor2 = (0, 0, 0)

        else:
            contador = 0


        if len(texto) <= 9:
            cor = (0, 255, 255)

        else:
            cor = (255,0,0)

        prosseguir = fonte2.render(texto3, 1, cor2)
        nome = fonte.render(texto, 1, (255,255,255))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key != pygame.K_BACKSPACE and evento.key != pygame.K_SPACE and evento.key != pygame.K_ESCAPE:
                    if len(texto) <= 9:
                        Barulho("smw_shell_ricochet.wav",0.5)
                        texto += evento.unicode
                    else:
                        Barulho("smw_yellow_yoshi_stomp.wav",0.5)

                elif evento.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]

                elif evento.key == pygame.K_SPACE:
                    pygame.mixer.music.pause()
                    pygame.mixer.music.unload()
                    Barulho("fall.wav",0.3)
                    Main(tela,clock,texto)
                    rodando = False

                elif evento.key == pygame.K_ESCAPE:
                    Barulho("fall.wav",0.3)
                    Menu(tela,clock)
                    rodando = False


        tela.fill((0,0,0))
        pygame.draw.rect(tela, cor, (445-(nome.get_width()/2),345-(nome.get_height()/2),nome.get_width()+10,nome.get_height()+5),1)
        tela.blit(seu_nome, (450 - (seu_nome.get_width() / 2), 300 - (nome.get_height() / 2)))
        tela.blit(prosseguir, (900 - prosseguir.get_width(), 700 - prosseguir.get_height()))
        tela.blit(nome, (450-(nome.get_width()/2),350-(nome.get_height()/2)))
        pygame.display.flip()

        contador += 1

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

def Titulo(fontes,indicacao,pontos=None, jogador=None, lv=None, tamanho=50):
    global RANKING
    frases = ["Tetrinho","Próximo bloco","{}: {}".format(jogador,pontos), "Maior pontuação: {}".format(pontos), "Nível: {}".format(lv)]
    cor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    fonte = random.choice(fontes)

    if indicacao == 0:
        titulo = pygame.font.Font("fontes_uuiii/{}".format(fonte), tamanho)
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

    elif indicacao == 4:
        titulo = pygame.font.SysFont("Lucida Console", 20)
        titulo2 = titulo.render(frases[4], 1, (255, 255, 255))

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

def Pontos(espacinhos,pontuacao, lv):
    multiplicador = 0
    for i in range(1,len(espacinhos)):
        if len(espacinhos[i]) == 10:
            multiplicador += 1*lv
            descida = espacinhos[1:i]
            descida.insert(0,[])
            espacinhos.remove(espacinhos[i])
            espacinhos.insert(1,[])
            descida = Movimentacao(descida, "baixo")
            for i in range(len(descida)):
                espacinhos[i+1] = descida[i]
            Barulho("clear.wav",0.3)

    pontuacao += 10*multiplicador
    return espacinhos,pontuacao

def Game_Over(espacinhos,jogador,pontuacao):
    global RANKING
    if espacinhos[1]:
        for i in range(len(RANKING["Pontos"])):
            if pontuacao > RANKING["Pontos"][i]:
                RANKING["Pontos"].insert(i,pontuacao)
                RANKING["Jogadores"].insert(i, jogador)
                RANKING["Pontos"].remove(RANKING["Pontos"][-1])
                RANKING["Jogadores"].remove(RANKING["Jogadores"][-1])
                break

        return True

    else:
        return False

def Main(tela,clock, nome_jogador):
    global FONTES
    global LARGURA
    global ALTURA
    global LARGURA_GRADE
    global ALTURA_GRADE
    global TOPO_X
    global TOPO_Y
    global RANKING
    global volume


    index = 0
    tamanho = 30
    contador_segundos = 0
    rodando = True
    pause = False
    pontuacao = 0
    base = 50
    lv = 1
    velocidade = 40

    musica = pygame.mixer.music.load("sons/Techno - Tetris (Remix)_160k.mp3")
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)

    titulo = Titulo(FONTES,0)
    proximo_bloco_texto = Titulo(FONTES,1)
    espacinhos = Vacuos(TOPO_X,TOPO_Y)
    bloquinho,formato = Bloquinhos(TOPO_X+120,TOPO_Y+120)
    prox_bloquinho,prox_formato = Bloquinhos(TOPO_X+120,TOPO_Y+120)

    while rodando:
        if not pause:
            clock.tick(60)

            if pontuacao >= base:
                Barulho("success.wav",0.3)
                lv += 1
                base = base*lv
                if velocidade-10 >= 1:
                    velocidade -= 10
                else:
                    velocidade = 1

            if RANKING["Pontos"][0] >= pontuacao:
                texto_maior_pontuacao = Titulo(FONTES, 3, pontos=RANKING["Pontos"][0])

            else:
                texto_maior_pontuacao = Titulo(FONTES, 3, pontos=pontuacao)

            texto_pontuacao = Titulo(FONTES, 2, pontos=pontuacao, jogador=nome_jogador)
            nivel = Titulo(FONTES,4,lv=lv)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

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
                    elif evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_ESCAPE:
                            pause = True

            if contador_segundos == velocidade:
                trava = Checar_Movimentos(index, bloquinho, espacinhos, "baixo")
                if not trava:
                    bloquinho = Movimentacao(bloquinho, "baixo")

                else:
                    for i in range(len(bloquinho[index])):

                        espacinhos[int((bloquinho[index][i][1]-20)/30)].append((int(bloquinho[index][i][0]),int(bloquinho[index][i][1]),bloquinho[index][i][-1]))
                    espacinhos, pontuacao = Pontos(espacinhos, pontuacao, lv)
                    game_over = Game_Over(espacinhos,nome_jogador,pontuacao)

                    if game_over:
                        pygame.mixer.music.pause()
                        pygame.mixer.music.unload()
                        Barulho("gameover.wav",0.3)
                        Tela_GO(tela,clock)
                        rodando = False
                    Barulho("fall.wav",0.3)
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

            if texto_pontuacao.get_width() == nivel.get_width():
                tela.blit(texto_pontuacao,(900-texto_pontuacao.get_width()-30,680-30))
                tela.blit(nivel, (900-texto_pontuacao.get_width()-30, 680))

            elif texto_pontuacao.get_width() >= nivel.get_width():
                tela.blit(texto_pontuacao,(870-texto_pontuacao.get_width(),650))
                tela.blit(nivel, (870-texto_pontuacao.get_width()+((texto_pontuacao.get_width()/2)-(nivel.get_width())/2), 680))

            elif texto_pontuacao.get_width() <= nivel.get_width():
                tela.blit(texto_pontuacao,(870-texto_pontuacao.get_width(),650))
                tela.blit(nivel, (870-nivel.get_width()+((nivel.get_width()/2)-(texto_pontuacao.get_width())/2), 680))

            Desenhando_prox_bloquinho(prox_bloquinho,prox_formato)
            Mapa(tela, TOPO_X, TOPO_Y, LARGURA_GRADE, ALTURA_GRADE)

            pygame.display.flip()
            contador_segundos = contador_segundos + 1
        if pause:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        pause = False

            fonte = pygame.font.Font("fontes_uuiii/Tetris.ttf", 200)
            pause_texto = fonte.render("PAUSE", 1, (255,255,255))
            tela.blit(pause_texto, (450-(pause_texto.get_width()/2),350-(pause_texto.get_height()/2)))
            pygame.display.flip()


def Menu(tela,clock):
    global volume

    rodando = True
    contador = 0
    contador2 = 0
    contador3 = 0
    marcador = 0
    escolha = "Aperte espaço para prosseguir"
    jogar = "Jogar"
    ranking = "Ranking"

    fonte = pygame.font.SysFont("Lucida Console", 15)
    fonte2 = pygame.font.Font("fontes_uuiii/Tetris.ttf", 50)
    tetrinho = Titulo(FONTES, 0, tamanho=150)

    if not pygame.mixer.get_busy():
        musica = pygame.mixer.music.load("sons/Tetris Theme Slowed Down _160k.mp3")
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)

    iniciar_jogo = fonte2.render(jogar, 1, (255,255,255))
    iniciar_ranking = fonte2.render(ranking, 1, (255,255,255))
    while rodando:
        clock.tick(80)
        if contador == 80:
            tetrinho = Titulo(FONTES,0, tamanho=150)
            contador = 0

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s:
                    Barulho("selection.wav", 0.3)
                    if marcador < 1:
                        marcador += 1
                    else:
                        marcador = 0

                elif evento.key == pygame.K_w:
                    Barulho("selection.wav", 0.3)
                    if marcador > 0:
                        marcador -= 1
                    else:
                        marcador = 1

                elif evento.key == pygame.K_SPACE:
                    Barulho("fall.wav",0.3)
                    if marcador == 0:
                        Jogador(tela,clock)
                        rodando = False
                    elif marcador == 1:
                        Tela_Ranking(tela,clock)
                        rodando = False

        if contador2 <= 30:
            cor = (255, 255, 255)

        elif contador2 >= 30 and contador <= 60:
            cor = (0, 0, 0)

        else:
            contador2 = 0

        escolher = fonte.render(escolha, 1, cor)

        tela.fill((0,0,0))
        tela.blit(escolher, (900 - escolher.get_width(), 700 - escolher.get_height()))
        tela.blit(tetrinho, (450-(tetrinho.get_width()/2),150-(tetrinho.get_height()/2)))
        tela.blit(iniciar_jogo, ((450-(iniciar_jogo.get_width()/2),400-(iniciar_jogo.get_height()/2))))
        tela.blit(iniciar_ranking, ((450-(iniciar_ranking.get_width()/2),500-(iniciar_ranking.get_height()/2))))
        if marcador == 0:
            x = iniciar_jogo.get_width() / 2
            y = iniciar_jogo.get_height() / 2

            if contador3 <= 30:
                pygame.draw.polygon(tela,(255,255,255),((400-x,410-y),(400-x,410),(430-x,(820-y)/2)),0)

            elif contador3 >= 30 and contador <= 60:
                pygame.draw.polygon(tela,(255,255,255),((380-x,410-y),(380-x,410),(410-x,(820-y)/2)),0)

            else:
                contador3 = 0

            pygame.draw.rect(tela,(255,255,255),(440-(iniciar_jogo.get_width()/2),390-(iniciar_jogo.get_height()/2),iniciar_jogo.get_width()+20,iniciar_jogo.get_height()+20),5)


        elif marcador == 1:
            x = iniciar_ranking.get_width()/2
            y = iniciar_ranking.get_height()/2
            if contador3 <= 30:
                pygame.draw.polygon(tela,(255,255,255),((400-x,510-y),(400-x,510),(430-x,(1020-y)/2)),0)

            elif contador3 >= 30 and contador3 <= 60:
                pygame.draw.polygon(tela,(255,255,255),((380-x,510-y),(380-x,510),(410-x,(1020-y)/2)),0)

            else:
                contador3 = 0

            pygame.draw.rect(tela,(255,255,255),(440-(iniciar_ranking.get_width()/2),490-(iniciar_ranking.get_height()/2),iniciar_ranking.get_width()+20,iniciar_ranking.get_height()+20),5)


        pygame.display.flip()

        contador += 1
        contador2 += 1
        contador3 += 1

def Tela_GO(tela,clock):
    global volume
    rodando = True
    subida = 0
    contador = 0

    musica = pygame.mixer.music.load("sons/Game Over - Super Mario World Remix_160k.mp3")
    pygame.mixer.music.set_volume(volume)

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
                    pygame.mixer.music.pause()
                    pygame.mixer.music.unload()
                    rodando = False
                    Menu(tela,clock)

        tela.fill((0,0,0))

        if subida == 200:
            pygame.mixer.music.play(-1)

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

def Tela_Ranking(tela,clock):
    global RANKING

    rodando = True
    tela.fill((0,255,255))
    pygame.display.flip()
    contador = 0

    fonte = pygame.font.Font("fontes_uuiii/Tetris.ttf", 30)
    pontos = fonte.render(str(RANKING["Pontos"][0])+" PTS", 1, (0,0,0))
    marcador_pontos = pontos.get_width()

    while rodando:

        clock.tick(80)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key:
                    Barulho("fall.wav", 0.3)
                    Menu(tela,clock)
                    rodando = False


        if contador == 0:
            for i in range(2000):

                if i <= 700:
                    pygame.draw.line(tela, (168, 168, 168), (0, 0), (0, i), 10)

                if i >= 860-marcador_pontos and i <= 1560-marcador_pontos:
                    pygame.draw.line(tela, (168, 168, 168), (860-marcador_pontos, 0), ((860-marcador_pontos), i-(860-marcador_pontos)), 10)

                if i >= 900 and i <= 1600:
                    pygame.draw.line(tela, (168, 168, 168), (900, 0), (900, i-900), 14)

                if i <= 900:
                    pygame.draw.line(tela, (168, 168, 168), (0, 0), (i, 0), 10)

                if i >= 70 and i <= 1000:
                    pygame.draw.line(tela, (168, 168, 168), (0, 70), (i - 100, 70), 10)

                if i >= 140 and i <= 1140:
                    pygame.draw.line(tela, (168, 168, 168), (0, 140), (i - 140, 140), 10)

                if i >= 210 and i <= 1210:
                    pygame.draw.line(tela, (168, 168, 168), (0, 210), (i - 210, 210), 10)

                if i >= 280 and i <= 1280:
                    pygame.draw.line(tela, (168, 168, 168), (0, 280), (i - 280, 280), 10)

                if i >= 350 and i <= 1350:
                    pygame.draw.line(tela, (168, 168, 168), (0, 350), (i - 350, 350), 10)

                if i >= 420 and i <= 1420:
                    pygame.draw.line(tela, (168, 168, 168), (0, 420), (i - 420, 420), 10)

                if i >= 490 and i <= 1490:
                    pygame.draw.line(tela, (168, 168, 168), (0, 490), (i - 490, 490), 10)

                if i >= 560 and i <= 1560:
                    pygame.draw.line(tela, (168, 168, 168), (0, 560), (i - 560, 560), 10)

                if i >= 630 and i <= 1630:
                    pygame.draw.line(tela, (168, 168, 168), (0, 630), (i - 630, 630), 10)

                if i >= 700 and i <= 1700:
                    pygame.draw.line(tela, (168, 168, 168), (0, 700), (i - 700, 700), 14)

                pygame.display.flip()

        if contador < 10:

            texto = ""
            for i in RANKING["Jogadores"][contador]:
                texto += i
                record = fonte.render(texto, 1, (0, 0, 0))
                tela.blit(record,(10,(70/2)-(record.get_height()/2)+70*contador))
                pygame.display.flip()
                time.sleep(0.02)

            texto = ""
            tamanho_pontos = fonte.render(str(RANKING["Pontos"][contador])+" PTS", 1, (255,255,255))
            for i in str(RANKING["Pontos"][contador])+" PTS":
                texto += i
                pontos = fonte.render(texto, 1, (0, 0, 0))
                tela.blit(pontos, (880-tamanho_pontos.get_width(),(70/2)-(pontos.get_height()/2)+70*contador))
                pygame.display.flip()
                time.sleep(0.02)
            contador += 1

        pygame.display.flip()

Menu(tela,clock)