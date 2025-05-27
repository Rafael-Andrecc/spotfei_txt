
def cadastrar():
    usuarios = open('./login_cadastro/usuarios.txt','a')
    nome_real = input('digite seu nome: ')
    user_name = input('digite seu user_name: ')
    email = input('digite seu email: ')
    print(f'email digitado: {email}')
    confirmar_email= int(input('Seu email esta correto\nSIm[1]\nNão[0]'))
    while confirmar_email == 0:
        email = input('digite seu email: ')
        print(f'email digitado: {email}')
        confirmar_email= int(input('Seu email esta correto\nSIm[1]\nNão[0]'))
    senha = input('Digite sua senha: ')
    confirme_sua_senha = input('confirme sua senha: ')
    while confirme_sua_senha != senha:
        senha = input('Digite sua senha: ')
        confirme_sua_senha = input('confirme sua senha: ')
    usuarios.write(f'{nome_real},{user_name},{email},{senha} \n')
    print(f'Nome: {nome_real}\n Username: {user_name}\n Email: {email} \n Senha: {senha}\n Cadastro realizado com sucesso')
    usuarios.close() 
    print('tarefa realizada com sucesso...')
    print('-'*10)   
def login():
    with open('./login_cadastro/usuarios.txt', 'r') as usuarios:
        linhas = usuarios.readlines()
    
    while True:
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        encontrou = False

        for linha in linhas:
            dados = linha.strip().split(',')  # nome_real, user_name, email, senha
            if len(dados) == 4:
                nome_real, user_name, email_arquivo, senha_arquivo = dados
                if email == email_arquivo and senha == senha_arquivo:
                    encontrou = True
                    print(f'Bem-vindo(a), {nome_real} ({user_name})!')
                    break

        if encontrou:
            print('Login realizado com sucesso!')
            print('tarefa realizada com sucesso...')
            print('-'*10) 
            break
        else:
            print(f'Email digitado: {email}')
            resposta = input('Senha ou email errados.\nDeseja tentar novamente?\nSim[1]\nNão[0]\nAguardando resposta: ')
            if resposta != '1':
                print('Encerrando login.')
                break
        
