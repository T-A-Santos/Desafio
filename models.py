from gino_tornado import Gino

db = Gino()

class ConsultaPessoa(db.Model):
    __tablename__ = "ConsultaPessoa"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    CPF = db.Column(db.Integer())
    nome = db.Column(db.String(255))
    endereco = db.Column(db.String(255))
    lista_dividas = db.Column(db.String(255))


    def dict_repr(self):
        return {
            'id' : int(self.id),
            'CPF' : str(self.CPF),
            'nome': self.nome,
            'endereco': self.endereco,
            'lista_dividas':self.lista_dividas
        }


class ScoreCredito(db.Model):
    __tablename__ = "ScoreCredito"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    CPF = db.Column(db.Integer())
    idade = db.Column(db.SmallInteger())
    lista_bens = db.Column(db.String(255))
    fonte_renda = db.Column(db.String(255))

    def dict_repr(self):

        return {
            'id': str(self.id),
            'CPF': str(self.CPF),
            'idade': str(self.idade),
            'lista_bens': self.lista_bens,
            'fonte_renda': self.fonte_renda
        }
    
    async def traceback(self):
        eventos = await ConsultaEventos.query.where(
            ConsultaEventos.CPF == str(self.CPF)
        ).gino.first()
        return [a.dict_repr() for a in eventos]

    
class ConsultaEventos(db.Model):
    __tablename__ = 'ConsultaEventos'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    CPF = db.Column(db.Integer())
    ultima_consulta = db.Column(db.DateTime())
    movimentacao_financeira = db.Column(db.Integer())
    ultima_compra = db.Column(db.String(255))

    def dict_repr(self):
        return {
            'id': str(self.id),
            'ultima_consulta': self.ultima_consulta,
            'movimentacao_financeira': str(self.movimentacao_financeira),
            'ultima_compra': self.ultima_compra
        }
