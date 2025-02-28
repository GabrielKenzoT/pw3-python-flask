from flask import render_template, request


def init_app(app):
    
    @app.route('/')
    # Criando função no Python
    # View funcition - unção de visualização
    def home():
        return render_template('index.html')


    @app.route('/games', methods=['GET', 'POST'])
    def games():
        # Dicionario no Python (objeto)
        game = {
            'titulo': 'CS-GO',
            'ano': 2012,
            'categoria': 'FPS online'
        }

        jogadores = ['iruah', 'davi_lambari', 'edosonhgf', 'kioto',
                    'black.butterfly', 'jujudopix']
        
        if request.method == 'POST':
            if request.form.get('jogador'): # nome do input
                jogadores.append(request.form.get('jogador'))
        
        jogos = ["gta 5", "lol", "Fortnite", "Elder ring",
                "Rust", "DayZ", "Dead by daylight"]
        
        return render_template('games.html',
                            game=game,
                            jogadores=jogadores,
                            jogos=jogos)
