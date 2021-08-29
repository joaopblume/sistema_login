import mysql.connector
import stdiomask

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='users'
)


def menu():
    escolha = 0
    while (escolha < 1) or (escolha > 3):
        print('=' * 20)
        print("Sistema de login".center(20))
        print('=' * 20)
        print("Escolha sua opção: \n")
        print("[1] Cadastrar novo usuário\n")
        print("[2] Fazer login\n")
        print("[3] Sair\n")
        escolha = int(input("Digite sua opção: "))
    return escolha


def fazer_login():
    login = input("Digite seu login: ")
    senha = stdiomask.getpass(prompt='Digite sua senha: ', mask='*')
    return(login, senha)


def validar_usuario(login, senha):
    # buscando o usuario
    cursor = db.cursor()
    comando = f'SELECT COUNT(log) as quantidade FROM users WHERE log = "{login}";'
    cursor.execute(comando)
    log = cursor.fetchone()

    # buscando a senha de acordo com o usuario
    comando = f'SELECT (pswd) FROM users WHERE log = "{login}";'
    cursor.execute(comando)
    password = cursor.fetchone()

    # se o usuario existir
    if log[0] > 0:
        if password[0] == senha:
            print("Você entrou com sucesso!\n\n")
        else:
            print("Senha inválida!\n\n")

    else:
        print("Usuário não encontrado!\n\n")


def buscar_usuario(login):
    cursor = db.cursor()
    comando = f'SELECT COUNT(log) as quantidade FROM users WHERE log = "{login}";'
    cursor.execute(comando)
    log = cursor.fetchone()

    return log[0]

def cadastrar(login, senha):
    try: 
        cursor = db.cursor()
        comando = f'INSERT INTO users(log, pswd) VALUES ("{login}", "{senha}");'
        cursor.execute(comando)
        db.commit()
    except:
        print("Ops, algo de errado aconteceu!\n")
    else:
        print("Cadastrado com sucesso!")

while True:
    escolha = menu()
    if escolha == 1:
        login, senha = fazer_login()
        
        if buscar_usuario(login) == 1:
            print("Usuário já existe!\n\n")

        elif (login == '') or (senha == ''):
            print("Login ou senha não podem ficar em branco!\n\n")
            
        
        elif login == senha:
            print("A senha deve ser diferente do login!\n\n")
            

        else:
            cadastrar(login, senha)
        
    elif escolha == 2:
        login, senha = fazer_login()
        validar_usuario(login, senha)

    elif escolha == 3:
        break



