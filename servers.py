import json

from datetime import datetime
from tornado.web import Application, RequestHandler


from models import ConsultaPessoa, ScoreCredito, ConsultaEventos


class PessoaHandler(RequestHandler):
    
    async def get(self, id):
        pessoa = await ConsultaPessoa.query.where(
            ConsultaPessoa.id == id
        ).gino.first()
        print('donhandler async get', pessoa)
        self.write({f'{id_pessoa}': pessoa})

    async def post(self, dronid):
        data = json.loads(self.request.body)
        pessoa = ConsultaPessoa(**data)
        await pessoa.create()
        print('donhandler async post', pessoa)
        self.write({'created': pessoa.id})
        

def build_service(service_management=None):
    return Application([
        (r"/pessoa/([\w]*)", PessoaHandler),
        #(r"/route/([\w]*)", RouteHandler),
        #(r"/route-point/", RoutePointHandler),
    ], debug=True
    )