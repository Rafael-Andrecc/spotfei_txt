import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def buscar_playlist():
    
    playlist_name = ''.join(input('qual o nome da playlist desejada: ').upper().split())
    
    caminho_playlist = f'./playlist/playlist_salvas/{playlist_name}.txt'
    if os.path.exists(caminho_playlist):
        playlist_read = open(caminho_playlist, 'r')
        for linha in (playlist_read.readlines()):
            dados = linha.strip().split(',')
            if len(dados) == 4:
                nome_musica, nome_artista, ano_musica, estilo_musical = dados
                data_music = f'Dados musica.\nNome da musica: {nome_musica}\nNome artista: {nome_artista}\nAno musica: {ano_musica}\nEstilo musical: {estilo_musical}'
                print(data_music)
                print('------------------')
    print('tarefa realizada com sucesso...')
    print('-'*10) 
                


        