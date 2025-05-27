import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from buscar_musicas.buscar import*


def adicionar_curtidas():
    curtidas = open('./curtir_descurtir/curtidas.txt', 'a')
    dado_musica = buscar()

    print(f"deseja adicionar musica {dado_musica} a lista de curtidas?")
    print("  Sim[1]")
    print("  Não[0]")
    quer_adicionar = int(input("Aguardando resposta: "))

    if quer_adicionar == 1:
        curtidas.write(f'{dado_musica}\n')
    curtidas.close()
    print('tarefa realizada com sucesso...')
    print('-'*10)
    input('Precione ENTER para voltar ao menu de tarefas')
    
    



def adicionar_descurtidas():
    descurtidas = open('./curtir_descurtir/descurtidas.txt', 'a')
    dado_musica = buscar()

    print(f"deseja adicionar musica {dado_musica} a lista de descurtidas?")
    print("  Sim[1]")
    print("  Não[0]")
    quer_adicionar = int(input("Aguardando resposta: "))

    if quer_adicionar == 1:
        descurtidas.write(f'{dado_musica}\n')
    descurtidas.close()
    print('tarefa realizada com sucesso...')
    print('-'*10)
    input('Precione ENTER para voltar ao menu de tarefas')
    

def ler_musicas(a):
    
    
    caminho_playlist = a
    if os.path.exists(caminho_playlist):
        playlist_read = open(caminho_playlist, 'r')
        for linha in (playlist_read.readlines()):
            dados = linha.strip().split(',')
            if len(dados) == 4:
                nome_musica, nome_artista, ano_musica, estilo_musical = dados
                data_music = f'Dados musica.\nNome da musica: {nome_musica}\nNome artista: {nome_artista}\nAno musica: {ano_musica}\nEstilo musical: {estilo_musical}'
                print(data_music)
                print('------------------')
    playlist_read.close()
    print('tarefa realizada com sucesso...')
    print('-'*10) 
    input('Precione ENTER para voltar ao menu de tarefas')
    