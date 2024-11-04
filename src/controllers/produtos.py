from flask_restx import Resource

from src.server.instancia import servidor
from src.models.produtos import produto

app, api = servidor.app, servidor.api

class ProdutoCRUD(object):
    def __init__(self):
        self.counter = 0
        self.produtos = []

    def get(self, id):
        for produto in self.produtos:
            if produto['id'] == id:
                return produto
        api.abort(404, "Produto {} não existe".format(id))

    def create(self, data):
        produto = data
        produto['id'] = self.counter = self.counter + 1
        self.produtos.append(produto)
        return produto
    

    def update(self, id, data):
        produto = self.get(id)
        produto.update(data)
        return produto
    
    def delete(self, id):
        produto = self.get(id)
        self.produtos.remove(produto)

produtos_db = ProdutoCRUD()
produtos_db.create({'nome': 'Notebook', 'preco': 2499.00})
produtos_db.create({'nome': 'Moto', 'preco': 50.000})
produtos_db.create({'nome': 'Celuar', 'preco': 1500.00})


@api.route("/produtos")
class ProductList(Resource):

    '''GET mostra uma lista de produtos'''

    @api.doc('Lista de produtos')
    @api.marshal_list_with(produto)
    def get(self,):
        '''
        Retorna uma lista de produtos
        '''
        return produtos_db.produtos
    
    @api.doc('cria_produtos')
    @api.expect(produto, valitade=True)
    @api.marshal_with(produto, code=201)
    def post(self,):
        '''
        Adiciona um novo produto na lista
        '''
        return produtos_db.create(api.payload), 201

@api.route('/produtos/<int:id>')
@api.response(404, 'Produto não encontrado')
@api.param('id', 'O identificador do produto')
class Produto(Resource):
    '''
    Mostra um único produto e permite que voce os delete
    '''

    @api.doc('get_produto')
    @api.marshal_with(produto)
    def get(self, id):

        '''
        Lista um produto dando o seu ID
        '''

        return produtos_db.get(id)
    
    @api.doc('delete_produto')
    @api.response(204, 'produto deleted')
    def delete(self, id):

        '''
        Deleta um produto dando seu ID
        '''

        produtos_db.delete(id)
        return '', 204

    @api.expect(produto)
    @api.marshal_with(produto)
    def put(self,id):
        
        '''
        Atualize um produto dando o seu ID
        '''
        return produtos_db.update(id, api.payload)