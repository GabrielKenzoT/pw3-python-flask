from flask import render_template, request

jogadores = ['iruah', 'davi_lambari', 'edosonhgf', 'kioto',
        'black.butterfly', 'jujudopix']

gamelist = [
    {'titulo': 'CS-GO','ano': 2012,'categoria': 'FPS online'},
    {'titulo': 'CS-GO','ano': 2012,'categoria': 'FPS online'},
    {'titulo': 'CS-GO','ano': 2012,'categoria': 'FPS online'},
    {'titulo': 'CS-GO','ano': 2012,'categoria': 'FPS online'},
    {'titulo': 'CS-GO','ano': 2012,'categoria': 'FPS online'},
    ]
consolelist = [
    {'nome': 'Playstation', 'ano': '1000', 'marca': 'sony'}
]

def init_app(app):

    
    @app.route('/')
    # Criando função no Python
    # View funcition - unção de visualização
    def home():
        return render_template('index.html')


    @app.route('/games', methods=['GET', 'POST'])
    def games():
        # acessando o primeiro jogo da lista de jogos
        game = gamelist[0]
   
        
        if request.method == 'POST':
            if request.form.get('jogador'): # nome do input
                jogadores.append(request.form.get('jogador'))
        
        jogos = ["gta 5", "lol", "Fortnite", "Elder ring",
                "Rust", "DayZ", "Dead by daylight"]
        
        return render_template('games.html',
                            game=game,
                            jogadores=jogadores,
                            jogos=jogos)
        
    
    @app.route('/cadgames', methods=['GET','POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'titulo': request.form.get('titulo'), 
                                'ano': request.form.get('ano'),
                                'categoria': request.form.get('categoria')})
                
        return render_template('cadgames.html', 
                               gamelist=gamelist)
        
    @app.route('/consoles', methods=['GET','POST'])
    def consoles():
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('ano') and request.form.get('marca'):
                consolelist.append({'nome': request.form.get('nome'),
                                    'ano': request.form.get('ano'),
                                    'marca': request.form.get('marca')})
                
        return render_template('consoles.html',
                               consolelist = consolelist)
