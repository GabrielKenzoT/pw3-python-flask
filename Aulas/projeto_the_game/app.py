# Comentário em Python
# Importando o pacote do Flask
from flask import Flask

# Carregando o Flask na variável app
app = Flask(__name__)
# Criando a rota principal do site
@app.route('/')
# Criando função no Python

def home():
    return '<h1>Gosto de comer</h1>'


@app.route('/games')

def games():
    return '<ha1>seja bem vindo a página de games</h1>'


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    