import mysql.connector
import os
from hashlib import sha256

def conectadb():
    
    global conexao_db
    global cursor
    DBHOST = os.environ ["DB_HOST"]
    USER = os.environ ["DB_USR"]
    PASSWORD = os.environ ["DB_PASSWORD"]
    DB = os.environ ["DB"]

    try: 
        

        conexao_db = mysql.connector.connect(host= DBHOST, user= USER, password= PASSWORD, database= DB)
    except Exception:
        return False
    else:
        cursor= conexao_db.cursor()
        return True


def build():
    if conectadb() == True:

        cursor.execute("""CREATE TABLE IF NOT EXISTS cadastro(user_id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(40) NOT NULL, lastname VARCHAR(40) NOT NULL, password VARCHAR(64) NOT NULL);""")
        conexao_db.close()
        return True
    else:
        print('Não foi possível criar o banco')
        return False

def valida_login(nome, senha):
    if conectadb() == True:
        senha = sha256(senha).hexdigest()
        nome = nome.upper()
        cursor.execute(f""" SELECT username, password FROM cadastro WHERE username= '{nome}' 
                            AND password= '{senha}';""")
        validado = cursor.fetchall()
        print(validado)
        print(len(validado))
        if len(validado) != 0:
 
            if nome == validado[0][0] and senha == validado[0][1] :
                conexao_db.close()
                return True
            else:
                return False
        
        else:
            return False
    else:
        print('Não foi possível conectar ao banco')
        return False 


def le_dados_usuario(nome):
    if conectadb() == True:
        cursor.execute(f" SELECT username, lastname FROM cadastro WHERE username= '{nome}';")
        res = cursor.fetchall()
        conexao_db.close()
        return res
    else:
        print('Não foi possível conectar ao banco')

def cadastra(nome, sobrenome, senha, confirmacao_senha):
    print('Executpo cadastro')
    if conectadb() == True:
        if senha == confirmacao_senha:

            senha = sha256(senha).hexdigest()
            cursor.execute(f""" INSERT INTO cadastro (username, lastname, password)
                    VALUES ("{nome.upper()}", "{sobrenome.upper()}", "{senha}"); """)
            conexao_db.commit()
            conexao_db.close()
            return True
        else:
            print(senha)
            print(confirmacao_senha)
            print('senhas não conferem')
            return False
            
        
    else:
        print('Não foi possível conectar ao banco')
        return False


