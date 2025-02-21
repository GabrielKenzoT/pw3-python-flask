# Comentário em Python
# Importando o pacote do Flask
from flask import Flask, render_template

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')
# Criando a rota principal do site
@app.route('/')
# Criando função no Python
# View funcition - unção de visualização
def home():
    return render_template('index.html')


@app.route('/games')

def games():
    titulo = 'CS-GO'
    ano = 2012
    categoria = 'FPS online'
    jogadores = ['iruah', 'davi_lambari', 'edosonhgf', 'kioto', 
                 'black.butterfly', 'jujudopix']
    jogos = ["gta 5", "lol", "Fortnite", "Elder ring", "Rust", "DayZ", "Dead by daylight"]
    return render_template('games.html', 
                           titulo= titulo, 
                           ano = ano, 
                           categoria = categoria,
                           jogadores = jogadores,
                           jogos = jogos)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    