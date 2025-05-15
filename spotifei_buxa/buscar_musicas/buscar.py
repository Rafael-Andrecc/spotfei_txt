# def buscar():
#     musicas = open("./buscar_musicas/musicas.txt")
#     linhas = musicas.readlines()
#     while True:
#         busque = input('digite o nome da musica ou o nome do artista ').upper()
       
#         encontrou = False

#         for linha in linhas:
#             dados = linha.strip().split(',')  # nome_real, user_name, email, senha
#             if len(dados) == 4:
#                 nome_musica, nome_artista, ano_musica, estilo_musical = dados
#                 if nome_musica == busque or nome_artista == busque:
#                     encontrou = True
#                     data_music =(f'Dados musica.\nNome da musica: {nome_musica}\nNome artista: {nome_artista}\nAno musica: {ano_musica} \nEstilo musical: {estilo_musical.strip()}')
#                     print(data_music)
#         if not encontrou:
#             print("Música ou artista não encontrados.")
#         break
#     return dados
def buscar():
    musicas = open("./buscar_musicas/musicas.txt")
    linhas = musicas.readlines()
    
    while True:
        busque = input('Digite o nome da música ou o nome do artista: ').upper()
        encontrou = False

        for linha in linhas:
            dados = linha.strip().split(',')
            if len(dados) == 4:
                nome_musica, nome_artista, ano_musica, estilo_musical = dados

                if nome_musica == busque or nome_artista == busque:
                    encontrou = True
                    data_music = f'Dados musica.\nNome da musica: {nome_musica}\nNome artista: {nome_artista}\nAno musica: {ano_musica}\nEstilo musical: {estilo_musical}'
                    print(data_music)
                    print('tarefa realizada com sucesso...')
                    print('-'*10) 
                    return dados  # ✅ retorna imediatamente os dados corretos

        if not encontrou:
            print("Música ou artista não encontrados.")
            return None  # ✅ se não achou, retorna None


