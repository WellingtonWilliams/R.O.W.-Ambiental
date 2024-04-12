from typing import List
from models.cliente import Cliente


class ClienteControl:

    def __init__(self):
        self.__lista_clientes: List[Cliente] = []

    def adicionar_cliente(self, cliente: Cliente) -> str:
        self.__lista_clientes.append(cliente)
        return "Cliente adicionado com sucesso"

    def acessar_cliente(self, indice: int) -> Cliente:
        cliente = self.__lista_clientes[indice]
        return cliente

    def alterar_cliente(self, indice: int, cliente: Cliente) -> str:
        self.__lista_clientes[indice] = cliente
        return "Cliente alterado com sucesso"

    def excluir_cliente(self, indice: int) -> str:
        del self.__lista_clientes[indice]
        return "Cliente excluído com sucesso"

    @property
    def lista_clientes(self) -> List[Cliente]:
        return self.__lista_clientes

    @lista_clientes.setter
    def lista_clientes(self, lista: List[Cliente]) -> None:
        pass
