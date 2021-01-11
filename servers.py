import json

from datetime import datetime
from tornado.web import Application, RequestHandler


from models import ConsultaPessoa, ScoreCredito, ConsultaEventos


class PessoaHandler(RequestHandler):
    
    async def get(self, idpessoa):
        pessoa = await ConsultaPessoa.query.where(
            ConsultaPessoa.id == idpessoa
        ).gino.first()
        print('routehandler async get', pessoa)
        self.write({idpessoa: pessoa})

    async def post(self, dronid):
        data = json.loads(self.request.body)
        pessoa = ConsultaPessoa(**data)
        await pessoa.create()
        print('async post', pessoa)
        self.write({'created': pessoa.id})


class ScoreCreditoHandler(RequestHandler):

    async def get(self, scoreid):
        score = await ScoreCredito.query.where(
            ScoreCredito.id == scoreid
        ).gino.first()
        print('async get', score)
        self.write({scoreid: score})

    async def post(self, scoreid):
        data = json.loads(self.request.body)
        pessoa = await ConsultaPessoa.query.where(
            ConsultaPessoa.id == data['id']
        ).gino.first()
        print('Async Post Score', pessoa)
        if pessoa:
            score = ScoreCredito(**data)
            print(data, score)
            await score.create()
            print('Async post Score', score)
            self.write({'Criado': score.id})
        else:
            self.set_status(404, 'Não Criado')


class ConsultaEventosHandler(RequestHandler):

    async def get(self, eventosid):
        eventos = await ConsultaEventos.query.where(
            ConsultaEventos.id == eventosid
        ).gino.first()
        print('routehandler async get', eventos)
        self.write({eventosid: eventos})

    async def post(self):
        data = json.loads(self.request.body)
        score = await ScoreCredito.query.where(
            ScoreCredito.id == score['id']
        ).gino.first()
        print(' async post', score)
        if eventos:
            data['ultima_consulta'] = datetime.now()
            routepoint = ConsultaEventos(**data)
            await routepoint.create()
            print('async post', routepoint)
            self.write({'Criado': routepoint.id})
        else:
            self.set_status(404, 'Não Criado')
        

def build_service(service_management=None):
    return Application([
        (r"/pessoa/([\w]*)", PessoaHandler),
        (r"/score/([\w]*)", ScoreCreditoHandler),
        (r"/consulta-eventos/", ConsultaEventosHandler),
    ], debug=True
    )