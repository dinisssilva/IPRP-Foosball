import turtle as t
import functools
import random as r
import math as m
from pathlib import Path
LARGURA_JANELA = 1024
ALTURA_JANELA = 600
DEFAULT_TURTLE_SIZE = 40
DEFAULT_TURTLE_SCALE = 3
RAIO_JOGADOR = DEFAULT_TURTLE_SIZE / DEFAULT_TURTLE_SCALE
RAIO_BOLA = DEFAULT_TURTLE_SIZE / 2
PIXEIS_MOVIMENTO = 90
LADO_MAIOR_AREA = ALTURA_JANELA / 3
LADO_MENOR_AREA = 50
RAIO_MEIO_CAMPO = LADO_MAIOR_AREA / 4
START_POS_BALIZAS = ALTURA_JANELA / 6
BOLA_START_POS = (5,5)
VELOCIDADE_BOLA = 2




def jogador_cima(estado_jogo, jogador):
    
    jogador_mover=estado_jogo[jogador]
    if ((jogador_mover.ycor()+PIXEIS_MOVIMENTO+RAIO_JOGADOR) <(ALTURA_JANELA/2)):
        jogador_mover.sety(jogador_mover.ycor()+PIXEIS_MOVIMENTO)
    else:
        jogador_mover.sety(jogador_mover.ycor()+((ALTURA_JANELA/2)-jogador_mover.ycor()-RAIO_JOGADOR))
    guarda_posicoes_para_var(estado_jogo)

    
    pass

def jogador_baixo(estado_jogo, jogador):
    jogador_mover=estado_jogo[jogador]
    if ((jogador_mover.ycor()-PIXEIS_MOVIMENTO-RAIO_JOGADOR)>-(ALTURA_JANELA/2)):
        jogador_mover.sety(jogador_mover.ycor()-PIXEIS_MOVIMENTO-RAIO_JOGADOR)

    else:
        jogador_mover.sety(jogador_mover.ycor()-((ALTURA_JANELA/2)+jogador_mover.ycor()+RAIO_JOGADOR))
    guarda_posicoes_para_var(estado_jogo)
    pass
    
def jogador_direita(estado_jogo, jogador):
    jogador_mover=estado_jogo[jogador]
    if((jogador_mover.xcor()+PIXEIS_MOVIMENTO+RAIO_JOGADOR)<(LARGURA_JANELA/2) or ()):
        jogador_mover.setx(jogador_mover.xcor()+PIXEIS_MOVIMENTO)
    else:
        jogador_mover.setx(jogador_mover.xcor()+((LARGURA_JANELA/2)-jogador_mover.xcor()-RAIO_JOGADOR))        
    guarda_posicoes_para_var(estado_jogo)
    
    pass

def jogador_esquerda(estado_jogo, jogador):
    jogador_mover=estado_jogo[jogador]
    if((jogador_mover.xcor()-PIXEIS_MOVIMENTO-RAIO_JOGADOR)>-(LARGURA_JANELA/2)):
        jogador_mover.setx(jogador_mover.xcor()-PIXEIS_MOVIMENTO)
    else:
        jogador_mover.setx(jogador_mover.xcor()-((LARGURA_JANELA/2)+jogador_mover.xcor()-RAIO_JOGADOR))
    guarda_posicoes_para_var(estado_jogo)
    
    pass

def balizas(tartaruga):
    tartaruga.down()
    tartaruga.fd(LADO_MENOR_AREA)
    tartaruga.rt(90)
    tartaruga.fd(LADO_MAIOR_AREA)    
    tartaruga.rt(90)
    tartaruga.fd(LADO_MENOR_AREA)
    tartaruga.rt(90)
    tartaruga.fd(LADO_MAIOR_AREA)  
    tartaruga.up()
    pass
def desenha_linhas_campo():
    #linhas de meio campo{
    tartaruga_pintora=t.Turtle()
    tartaruga_pintora.up()
    tartaruga_pintora.hideturtle()
    tartaruga_pintora.goto(0,ALTURA_JANELA/2)
    tartaruga_pintora.color('white')
    tartaruga_pintora.pensize(10)
    tartaruga_pintora.down()
    tartaruga_pintora.goto(0,-RAIO_MEIO_CAMPO)
    #tartaruga_pintora.showturtle()
    tartaruga_pintora.circle(RAIO_MEIO_CAMPO,360,720)
    tartaruga_pintora.goto(0,-ALTURA_JANELA/2)
    tartaruga_pintora.up()
    #até aqui}
    tartaruga_pintora.goto(-LARGURA_JANELA/2,LADO_MAIOR_AREA/2+tartaruga_pintora.pensize())
    balizas(tartaruga_pintora)
    tartaruga_pintora.seth(180)
    tartaruga_pintora.goto(LARGURA_JANELA/2,-LADO_MAIOR_AREA/2+tartaruga_pintora.pensize())
    balizas(tartaruga_pintora)
    tartaruga_pintora.goto(-512,300)
    tartaruga_pintora.down()
    tartaruga_pintora.goto(512,300)
    tartaruga_pintora.goto(512,-300)
    tartaruga_pintora.goto(-512,-300)
    tartaruga_pintora.goto(-512,300)
    
    pass


def criar_bola():

    r.seed()
    bola=t.Turtle()
    bola.up()
    bola.color('black')
    bola.setpos(BOLA_START_POS)
    bola.shape('circle')
    orientador=r.randint(0,360)
    bola.seth(orientador)
    direcionante_yy=(m.sin(m.radians(orientador)))
    direcionante_xx=(m.cos(m.radians(orientador)))
    dic= dict({'turtle_bola':bola ,'direcao_yy_bola':direcionante_yy,'direcao_xx_bola':direcionante_xx,'last_posi_bola':None})
    return dic


def cria_jogador(x_pos_inicial, y_pos_inicial, cor):  
        jogador=t.Turtle()
        jogador.up()
        jogador.shape('circle')
        jogador.shapesize(DEFAULT_TURTLE_SCALE,DEFAULT_TURTLE_SCALE)
        jogador.color(cor)
        jogador.setpos(x_pos_inicial,y_pos_inicial)   
        return jogador       

def init_state():
    estado_jogo = {}
    estado_jogo['bola'] = None
    estado_jogo['jogador_vermelho'] = None
    estado_jogo['jogador_azul'] = None
    estado_jogo['var'] = {
        'bola' : [],
        'jogador_vermelho' : [],
        'jogador_azul' : [],
    }
    estado_jogo['pontuacao_jogador_vermelho'] = 0
    estado_jogo['pontuacao_jogador_azul'] = 0
    return estado_jogo

def cria_janela():
    #create a window and declare a variable called window and call the screen()
    window=t.Screen()
    window.title("Foosball Game")
    window.bgcolor("green")
    window.setup(width = LARGURA_JANELA,height = ALTURA_JANELA)
    window.tracer(0)
    return window

def cria_quadro_resultados():
    #Code for creating pen for scorecard update
    quadro=t.Turtle()
    quadro.speed(0)
    quadro.color("Blue")
    quadro.penup()
    quadro.hideturtle()
    quadro.goto(0,260)
    quadro.write("Player A: 0\t\tPlayer B: 0 ", align="center", font=('Monaco',24,"normal"))
    return quadro


def terminar_jogo(estado_jogo):
    print("Adeus")
    estado_jogo['janela'].bye()
    fileName= "historico_resultados.csv"
   
    path = "./" + fileName
    if(Path.is_file(path)):
        file = open(fileName, "r+")
        linhas = file.readlines()
        ultima_linha = linhas[-1]
        nr_ultimo_jogo = ultima_linha[0]
        print(nr_ultimo_jogo)
        jogo_atual = int(nr_ultimo_jogo) + 1
        pontuacao_vermelho = str(estado_jogo['pontuacao_jogador_vermelho'])
        pontuacao_azul = str(estado_jogo['pontuacao_jogador_azul'])
        
        string = f"{jogo_atual},{pontuacao_vermelho},{pontuacao_azul}\n"
        
        file.write(string)
        file.close()
    else:
        file = open(fileName, "w")
        file.write("NJogo,JogadorVermelho,JogadorAzul\n")
        jogo_atual = 1
        
        pontuacao_vermelho = str(estado_jogo['pontuacao_jogador_vermelho'])
        pontuacao_azul = str(estado_jogo['pontuacao_jogador_azul'])
        
        string = f"{jogo_atual},{pontuacao_vermelho},{pontuacao_azul}\n"
        
        file.write(string)
        file.close()
    
    t.reset()

def setup(estado_jogo, jogar):
    janela = cria_janela()
    #Assign keys to play
    janela.listen()
    if jogar:
        janela.onkeypress(functools.partial(jogador_cima, estado_jogo, 'jogador_vermelho') ,'w')
        janela.onkeypress(functools.partial(jogador_baixo, estado_jogo, 'jogador_vermelho') ,'s')
        janela.onkeypress(functools.partial(jogador_esquerda, estado_jogo, 'jogador_vermelho') ,'a')
        janela.onkeypress(functools.partial(jogador_direita, estado_jogo, 'jogador_vermelho') ,'d')
        janela.onkeypress(functools.partial(jogador_cima, estado_jogo, 'jogador_azul') ,'Up')
        janela.onkeypress(functools.partial(jogador_baixo, estado_jogo, 'jogador_azul') ,'Down')
        janela.onkeypress(functools.partial(jogador_esquerda, estado_jogo, 'jogador_azul') ,'Left')
        janela.onkeypress(functools.partial(jogador_direita, estado_jogo, 'jogador_azul') ,'Right')
        janela.onkeypress(functools.partial(terminar_jogo, estado_jogo) ,'Escape')
        quadro = cria_quadro_resultados()
        estado_jogo['quadro'] = quadro
    desenha_linhas_campo()
    bola = criar_bola()
    jogador_vermelho = cria_jogador(-((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0, "red")
    jogador_azul = cria_jogador(((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0, "blue")
    estado_jogo['janela'] = janela
    estado_jogo['bola'] = bola
    estado_jogo['jogador_vermelho'] = jogador_vermelho
    estado_jogo['jogador_azul'] = jogador_azul


def update_board(estado_jogo):
    estado_jogo['quadro'].clear()
    estado_jogo['quadro'].write("Player A: {}\t\tPlayer B: {} ".format(estado_jogo['pontuacao_jogador_vermelho'], estado_jogo['pontuacao_jogador_azul']),align="center",font=('Monaco',24,"normal"))

def movimenta_bola(estado_jogo):

    dados_bola=estado_jogo['bola']
    direcao_xx=dados_bola['direcao_xx_bola']
    direcao_yy=dados_bola['direcao_yy_bola']
    bola_mover=dados_bola['turtle_bola']
    jogador_azul=estado_jogo['jogador_azul']
    jogador_vermelho=estado_jogo['jogador_vermelho']
    movimento_xx=direcao_xx*VELOCIDADE_BOLA
    movimento_yy=direcao_yy*VELOCIDADE_BOLA
    vetor_movimento=((((movimento_xx)**2)+((movimento_yy)**2))**(0.5))
    d_bola_azul=bola_mover.distance(jogador_azul)
    d_bola_vermelho=bola_mover.distance(jogador_vermelho)
    if ((bola_mover.distance(jogador_azul)-RAIO_JOGADOR<(vetor_movimento))):
        bola_mover.fd(bola_mover.distance(jogador_azul)-(RAIO_JOGADOR+RAIO_BOLA))
        
    else:
        bola_mover.goto(bola_mover.xcor()+movimento_xx,bola_mover.ycor()+movimento_yy)

        
    dados_bola['last_posi_bola']=bola_mover.position()
    pass
def verifica_colisoes_ambiente(estado_jogo):

    dados_bola=estado_jogo['bola']
    direcao_yy_bola=dados_bola['direcao_yy_bola']
    direcao_xx_bola=dados_bola['direcao_xx_bola']
    bola_reflex=dados_bola['turtle_bola']
    if((bola_reflex.xcor()<=-LARGURA_JANELA/2) or (bola_reflex.xcor()>=LARGURA_JANELA/2)):
        dados_bola['direcao_xx_bola']=-direcao_xx_bola
        guarda_posicoes_para_var(estado_jogo)
        
    if((bola_reflex.ycor()<=-ALTURA_JANELA/2) or (bola_reflex.ycor()>=ALTURA_JANELA/2)or()):
        dados_bola['direcao_yy_bola']=-direcao_yy_bola
        guarda_posicoes_para_var(estado_jogo)
        
    pass


def verifica_golo_jogador_vermelho(estado_jogo):    
    dados_bola=estado_jogo['bola']
    turtle_bola=dados_bola['turtle_bola']
    if((turtle_bola.xcor()<=-LARGURA_JANELA/2) and ((turtle_bola.ycor()<=START_POS_BALIZAS)and(turtle_bola.ycor()>=(START_POS_BALIZAS-LADO_MAIOR_AREA)))):
        estado_jogo['pontuacao_jogador_vermelho']=estado_jogo['pontuacao_jogador_vermelho']+1
        update_board(estado_jogo)
        turtle_bola.setpos(BOLA_START_POS)
        orientador=r.randint(0,360)
        turtle_bola.seth(orientador)        
        direcionante_yy=(m.sin(m.radians(orientador)))
        direcionante_xx=(m.cos(m.radians(orientador))) 
        dados_bola['direcao_yy_bola']=direcionante_yy
        dados_bola['direcao_xx_bola']=direcionante_xx       
        return True
    return False
    

def verifica_golo_jogador_azul(estado_jogo):
    dados_bola=estado_jogo['bola']
    turtle_bola=dados_bola['turtle_bola']
    if((turtle_bola.xcor()>=LARGURA_JANELA/2) and ((turtle_bola.ycor()<=START_POS_BALIZAS)and(turtle_bola.ycor()>=(START_POS_BALIZAS-LADO_MAIOR_AREA)))):
        estado_jogo['pontuacao_jogador_azul']=estado_jogo['pontuacao_jogador_azul']+1
        update_board(estado_jogo)
        turtle_bola.setpos(BOLA_START_POS)
        orientador=r.randint(0,360)
        turtle_bola.seth(orientador)
        direcionante_yy=(m.sin(m.radians(orientador)))
        direcionante_xx=(m.cos(m.radians(orientador))) 
        dados_bola['direcao_yy_bola']=direcionante_yy
        dados_bola['direcao_xx_bola']=direcionante_xx
        return True
          

    
    return False

def verifica_golos(estado_jogo):
    rep = 1000
    if (verifica_golo_jogador_vermelho(estado_jogo) or verifica_golo_jogador_azul(estado_jogo)):
        class_vermelho=estado_jogo['pontuacao_jogador_vermelho']
        class_azul = estado_jogo['pontuacao_jogador_azul']
        fileName = "replay_golo_jv_" + str(class_vermelho) + "_ja_" + str(class_azul) + ".txt"
        file = open(fileName, "w") 
        var = estado_jogo['var']
        pos_bola = var['bola'][::-1]
        pos_vermelho = var['jogador_vermelho'][::-1]
        pos_azul = var['jogador_azul'][::-1]
        if(len(pos_bola) < rep):
            rep = len(pos_bola)-1
        for i in range (rep):
            file.write(str(pos_bola[rep-i][0]) + "," + str(pos_bola[rep-i][1])+";")
        file.write(str(pos_bola[0][0]) + "," + str(pos_bola[0][1]))
        file.write("\n")
        for i in range (rep):
            file.write(str(pos_vermelho[rep-i][0]) + "," + str(pos_vermelho[rep-i][1])+";")
        file.write(str(pos_vermelho[0][0]) + "," + str(pos_vermelho[0][1]))
        file.write("\n")
        
        for i in range (rep):
            file.write(str(pos_azul[rep-i][0]) + "," + str(pos_azul[rep-i][1])+";")  
        file.write(str(pos_azul[0][0]) + "," + str(pos_azul[0][1]))  
        
        file.write("\n")
        
        file.close()

        
        
            
            
            
            
            
            
            
        
    
    def reiniciar_jogadores(jogador,x_pos_inicial, y_pos_inicial):
        jogador.setpos(x_pos_inicial,y_pos_inicial)
        if((verifica_golo_jogador_vermelho(estado_jogo) == True ) or (verifica_golo_jogador_azul(estado_jogo) == True )):
            reiniciar_jogadores(jogador_vermelho,-((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0)
            reiniciar_jogadores(jogador_azul,((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0 )    


def verifica_toque_jogador_azul(estado_jogo):
    dados_bola=estado_jogo['bola']
    turtle_bola=dados_bola['turtle_bola']
    jogador_azul=estado_jogo['jogador_azul']
    direcao_xx=dados_bola['direcao_xx_bola']
    direcao_yy=dados_bola['direcao_yy_bola']
    movimento_xx=direcao_xx*VELOCIDADE_BOLA
    movimento_yy=direcao_yy*VELOCIDADE_BOLA
    if((((turtle_bola.xcor()-jogador_azul.xcor())**2)+((turtle_bola.ycor()-jogador_azul.ycor())**2))<=((RAIO_JOGADOR+RAIO_BOLA)**2)):
        dados_bola['direcao_xx_bola']=-direcao_xx
        dados_bola['direcao_yy_bola']=-direcao_yy  
        guarda_posicoes_para_var(estado_jogo)    
    pass


def verifica_toque_jogador_vermelho(estado_jogo):
    dados_bola=estado_jogo['bola']
    turtle_bola=dados_bola['turtle_bola']
    jogador_vermelho=estado_jogo['jogador_vermelho']
    direcao_xx=dados_bola['direcao_xx_bola']
    direcao_yy=dados_bola['direcao_yy_bola']
    movimento_xx=direcao_xx*VELOCIDADE_BOLA
    movimento_yy=direcao_yy*VELOCIDADE_BOLA
    if((((turtle_bola.xcor()-jogador_vermelho.xcor())**2)+((turtle_bola.ycor()-jogador_vermelho.ycor())**2))<=((RAIO_JOGADOR+RAIO_BOLA)**2)):
        dados_bola['direcao_xx_bola']=-direcao_xx
        dados_bola['direcao_yy_bola']=-direcao_yy  
        guarda_posicoes_para_var(estado_jogo)
        
    pass

def guarda_posicoes_para_var(estado_jogo):
    estado_jogo['var']['bola'].append(estado_jogo['bola']['turtle_bola'].pos())
    estado_jogo['var']['jogador_vermelho'].append(estado_jogo['jogador_vermelho'].pos())
    estado_jogo['var']['jogador_azul'].append(estado_jogo['jogador_azul'].pos())

def main():
    estado_jogo = init_state()
    setup(estado_jogo, True)
    while True:
        estado_jogo['janela'].update()
        if estado_jogo['bola'] is not None:
            movimenta_bola(estado_jogo)
            guarda_posicoes_para_var(estado_jogo)            
        verifica_colisoes_ambiente(estado_jogo)
        verifica_golos(estado_jogo)
        if estado_jogo['jogador_vermelho'] is not None:
            verifica_toque_jogador_azul(estado_jogo)
        if estado_jogo['jogador_azul'] is not None:
            verifica_toque_jogador_vermelho(estado_jogo)

if __name__ == '__main__':
    main()