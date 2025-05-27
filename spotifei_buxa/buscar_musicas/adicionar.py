def adicionar_playlist():
    musicas = open("./buscar_musicas/musicas.txt",'a')
    nome_musica = input('Adicione o nome da musica: ').upper()
    nome_autor = input('Adicione o nome do autor: ').upper()
    ano_musica = input('Adicione o ano da musica: ').upper()
    estilo_musica = input('Adicione o estilo musical: ').upper()
    dados = (f'{nome_musica},{nome_autor},{ano_musica},{ano_musica}')
    musicas.write(f'{dados}\n')   
    print('tarefa realizada com sucesso...')
    print('-'*10) 
    input('Precione ENTER para voltar ao menu de tarefas')
    
    