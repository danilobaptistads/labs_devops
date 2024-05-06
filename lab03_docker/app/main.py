from flask import Flask, render_template, redirect, request
import banco

if banco.build() == True:

    app = Flask(__name__)
    app.config['secret_KEY'] = '98dssdh08oun9h97g79ubvin02355475bclsldm'

    @app.route('/')
    def home():
        return render_template('login.html')

    @app.route('/login', methods=['POST'])
    def login():
        global nome
        nome= request.form.get('nome_campo')
        senha= request.form.get('senha_campo').encode('utf-8')
        login = banco.valida_login(nome, senha)
        
        if login == True:
            return redirect('/area_logada')
        
        else:
            return redirect('/')
    
    @app.route('/cadastro', methods=['GET','POST'])
    def cadastro():        
        if request.method == "POST":
            nome= request.form.get('nome')
            sobrenome= request.form.get('sobreNome')
            senha= request.form.get('senha').encode('utf-8')
            confirmacao_senha= request.form.get('confirmacao_senha').encode('utf-8')

            cadastrado = banco.cadastra(nome, sobrenome, senha, confirmacao_senha)
            if cadastrado == True:
                return redirect('/')
            else:
                return render_template('/cadastro.html')
        
        return render_template('/cadastro.html')
            
    @app.route('/area_logada')
    def area_logada():
        global nome
        dados_usuario = banco.le_dados_usuario(nome)
        usrname = dados_usuario[0][0]
        sobrenome =  dados_usuario[0][1]
        print(nome)
        return render_template('area_logada.html', usrname=usrname, sobrenome=sobrenome)

    if __name__ in '__main__':
        app.run(debug=True, host="0.0.0.0")
        

else:
    print('Não foi possivel executar a aplicação.\nVerifuque a conexão com o banco')