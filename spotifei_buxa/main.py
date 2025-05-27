from login_cadastro.login_cadastro import *
from buscar_musicas.buscar import *
from curtir_descurtir.Curtir_descurtir import *
from playlist.Criar_playlist import *
from playlist.buscar_playlist import *
from buscar_musicas.adicionar import *


acesso = int(input('já possui login \n Digite 0 para [NÃO]\n Digite 1 para [SIM]\n aguardando resposta:  '))
if acesso == 0 :
    cadastrar()
else:
    login()
    
def decidir():
    fazer = int(input('Que ação vc deseja tomar.\n----------\n Buscar musicas[0]\n----------\n Criar playlists[1] \n----------\n Buscar playlist[2]\n----------\n Adicionar musicas a uma playlist já existente[3]\n----------\nCurtir uma musica[4]\n----------\nDescurtir uma musica[5]\n----------\nVer musicas curtidas[6]\n----------\nVer musicas descurtirdas[7]\n----------\nAdicionar uma musica ao banco de dados[8]\n----------\nVisualizar historico de busca[9]\n----------\nSair do sistema[10]\n----------\nAguardando resposta: '))
    if fazer == 0:
        print('buscando musica...')
        buscar()
    elif fazer == 1:
        print('Criando playlist...')
        
        criar_playlist()
    elif fazer == 2:
        print('buscando playlist...')
        
        buscar_playlist()
        
    elif fazer == 3:
        print('adicionando musica a playlist...')
        
        adicionar_musica()
    elif fazer == 4:
        print('adicionando musica a curtidas...')
        
        adicionar_curtidas()
    elif fazer == 5:
        print('adicionando musica a descurtidas...')
        
        adicionar_descurtidas()
    elif fazer == 6:
        print('carregando musicas curtidas...')
        
        ler_musicas(('./curtir_descurtir/curtidas.txt'))
    elif fazer == 7:
        print('carregando musicas descurtidas...')
        ler_musicas(('./curtir_descurtir/descurtidas.txt'))
    elif fazer == 8:
        print('adicionando musica ao banco de dados...')
        adicionar_playlist()
    elif fazer == 9:
        print('visualizar historico de busca...')
        ler_musicas("./buscar_musicas/historico.txt")
    elif fazer == 10:
        print('Encerrando programa...')
    return fazer

while decidir() != 10:       
    decidir()
    