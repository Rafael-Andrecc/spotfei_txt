# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from buscar_musicas.buscar import*

# def criar_playlist():
#     playlist_name = input('qual o nome da playlist desejada: ').upper().split()
#     playlist_new = open(f'./playlist/playlist_salvas/{playlist_name}.txt', 'a')
# criar_playlist()

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buscar_musicas.buscar import*

def criar_playlist():
    playlist_name = ''.join(input('qual o nome da playlist desejada: ').upper().split())
    playlist_new = open(f'./playlist/playlist_salvas/{playlist_name}.txt', 'a')
    print('A playlist deve conter pelo menos uma musica')
    adicionar_musica()
# criar_playlist()

def adicionar_musica():
    playlist_name = ''.join(input('qual o nome da playlist desejada: ').upper().split())
    caminho_playlist = f'./playlist/playlist_salvas/{playlist_name}.txt'
    if os.path.exists(caminho_playlist):
        playlist_add = open(caminho_playlist, 'a')
        playlist_add.write(buscar())
        print('tarefa realizada com sucesso...')
        print('-'*10) 
    else:
        playlist_name_invalid =int(input('essa playlist não existe deseja criar ela?\nSim[1]\nNão[0]\n Aguardando resposta: '))
        if playlist_name_invalid == 1 :
            criar_playlist()
            print('tarefa realizada com sucesso...')
            print('-'*10) 
        else:
            print('operção cancelada')
            print('tarefa realizada com sucesso...')
            print('-'*10) 
        
    