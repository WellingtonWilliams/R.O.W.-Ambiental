from typing import List
from models.servico import Servico


class ServicoControl:

    def __init__(self) -> None:
        self.__lista_servicos: List[Servico] = []

    def adicionar_servico(self, servico: Servico) -> str:
        self.__lista_servicos.append(servico)
        return "Serviço adicionado com sucesso"

    def acessar_servico(self, indice: int) -> Servico:
        servico = self.__lista_servicos[indice]
        return servico

    def alterar_servico(self, indice: int, servico: Servico) -> str:
        self.__lista_servicos[indice] = servico
        return "Serviço alterado com sucesso"

    def excluir_servico(self, indice: int) -> str:
        del self.__lista_servicos[indice]
        return "Serviço excluído com sucesso"

    @property
    def lista_servicos(self) -> List[Servico]:
        return self.__lista_servicos

    @lista_servicos.setter
    def lista_servicos(self, lista: List[Servico]) -> None:
        pass
