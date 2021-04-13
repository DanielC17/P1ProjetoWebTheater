from application.model.entity.categoria import Categoria
from application import categorylist

class CategoriaDAO():

    def __init__(self):
        self.__categorylist = categorylist

    def get_categorylist(self) -> list:
        return self.__categorylist
