import Projeto_Foosball_Dinis
import turtle as t
def le_replay(nome_ficheiro):

    
    replay = {
        'bola': [], 
        'jogador_vermelho' : [],
        'jogador_azul': []
    }
    
    with open(nome_ficheiro,'r') as ficheiro:
        coord_bola=ficheiro.readline()
        coord_jv=ficheiro.readline()
        coord_ja=ficheiro.readline()

        lista_bola = coord_bola.split(";")
        lista_jv = coord_jv.split(";")
        lista_ja = coord_ja.split(";")
        
        

        for i in range (len(lista_bola)):
            coordenadas_bola = lista_bola[i].strip().split(",")
            coordenad_bola_t=(float(coordenadas_bola[0]),float(coordenadas_bola[1]))
            replay['bola'].append(coordenad_bola_t)
            
            coordenadas_jv = lista_jv[i].strip().split(",")
            coordenad_jv_t=(float(coordenadas_jv[0]),float(coordenadas_jv[1]))
            replay['jogador_vermelho'].append(coordenad_jv_t)
            
            
            coordenadas_ja = lista_ja[i].strip().split(",")
            coordenad_ja_t=(float(coordenadas_ja[0]),float(coordenadas_ja[1]))
            replay['jogador_azul'].append(coordenad_ja_t)        
    return replay
        

        


def main():
    estado_jogo = Projeto_Foosball_Dinis.init_state()
    Projeto_Foosball_Dinis.setup(estado_jogo, False)
    replay = le_replay('replay_golo_jv_1_ja_0.txt')
    for i in range(len(replay['bola'])):
        estado_jogo['janela'].update()
        estado_jogo['jogador_vermelho'].setpos(replay['jogador_vermelho'][i])
        estado_jogo['jogador_azul'].setpos(replay['jogador_azul'][i])
        estado_jogo['bola']['turtle_bola'].setpos(replay['bola'][i])
    estado_jogo['janela'].exitonclick()
    t.reset()
    


if __name__ == '__main__':
    main()