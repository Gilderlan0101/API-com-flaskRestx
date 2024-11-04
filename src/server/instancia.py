from flask import Flask
from flask_restx import Api


class Servidor():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(
            self.app,
            version='1.0',
            title='Gestão de vendas',
            description='Uma api simples para loja ',
        )

    def run(self,):
        self.app.run(
            debug=True
        )

servidor = Servidor()