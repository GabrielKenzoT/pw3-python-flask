# Importando o pacote do Flask
from flask import Flask
from controllers import routes



# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')


#iniciando o flask (app para a função init_app do routes)
routes.init_app(app)

if __name__ == '__main__':
    #Rodando o app
    app.run(host='localhost', port=5000, debug=True)
