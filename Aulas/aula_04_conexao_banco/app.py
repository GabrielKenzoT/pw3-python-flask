# Importando o pacote do Flask
from flask import Flask, render_template
#importando o PyMySQL
import pymysql
#Importando as rotas que estão nos controllers
from controllers import routes
#Importando os models
from models.database import db



# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')


#iniciando o flask (app para a função init_app do routes)
routes.init_app(app)

#Define o nome do banco de dados
DB_NAME = 'games'
# COnfigura o flask com o banco definido
app.config['DATABASE_NAME'] = DB_NAME

#Passando o endereço do banco ao Flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'



if __name__ == '__main__':
    #criando os dados de conexão
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    #Tentando criar o banco
    try:
        #with cria um recurso temporariamente
        with connection.cursor() as cursor:
            #Cria o banco de dados (se ele não existir)
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DB_NAME}')
            print(f'O banco de dados {DB_NAME} está criado!')
            
    except Exception as e:
        print(f'Erro ao criar o banco de dados: {e}')
    finally:
        connection.close()
        
    #Passando o flask para SQLAlchemy
    db.init_app(app=app)
    #Criando as tabelas a partir do model
    with app.test_request_context():
        db.create_all()
    #Rodando a aplicação Flask
    app.run(host='localhost', port=5000, debug=True)
