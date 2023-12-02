from core.services.ConnectionService import ConnectionService


class FoodManagerRepository:
    def __init__(self, conexao: ConnectionService) -> None:
        self.conexao = conexao

    def insert(self, collection, **kwargs):
        self.conexao.insert(collection, **kwargs)
