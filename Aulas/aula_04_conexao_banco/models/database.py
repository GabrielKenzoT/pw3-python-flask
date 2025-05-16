from flask_sqlalchemy import SQLAlchemy

#Carregadp o SQlAlchemy em uma variavel
db = SQLAlchemy()

# Classe da entidade Games
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    plataforma = db.Column(db.String(150)) 
    preco = db.Column(db.Float)
    
    # Metodo construtor da classe
    def _init_(self, titulo, ano, categoria, plataforma, preco):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.plataforma = plataforma
        self.preco = preco