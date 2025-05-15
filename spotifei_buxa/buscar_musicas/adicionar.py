def adicionar_playlist():
    musicas = open("./buscar_musicas/musicas.txt",'a')
    nome_musica = input('Adicione o nome da musica: ')
    nome_autor = input('Adicione o nome do autor: ')
    ano_musica = input('Adicione o ano da musica: ')
    estilo_musica = input('Adicione o estilo musical: ')
    dados = (f'{nome_musica},{nome_autor},{ano_musica},{ano_musica}')
    musicas.write(dados)   
    print('tarefa realizada com sucesso...')
    print('-'*10) 

    
    