class Servico:

    def __init__(self) -> None:
        self.__nome_servico: str = ""
        self.__codigo: str = ""
        self.__preco: str = ""
        self.__quantidade: str = ""
        self.msg_validacao: str = ""

    @property
    def nome_servico(self) -> str:
        return self.__nome_servico

    @nome_servico.setter
    def nome_servico(self, nome_servico: str) -> None:
        if nome_servico != "":
            self.__nome_servico = nome_servico
        else:
            self.msg_validacao = 'O campo "Nome" é obrigatório!'

    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: str) -> None:
        if codigo != "":
            self.__codigo = codigo
        else:
            self.msg_validacao = 'O campo "Código" é obrigatório!'

    @property
    def preco(self) -> str:
        return self.__preco

    @preco.setter
    def preco(self, preco: str) -> None:
        if preco != "":
            if float(preco) >= 0:
                self.__preco = preco
            else:
                self.msg_validacao = 'O "Preço" não pode ser negativo'
        else:
            self.msg_validacao = 'O campo "Preço" é obrigatório!'

    @property
    def quantidade(self) -> str:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: str) -> None:
        if quantidade != "":
            if int(quantidade) >= 0:
                self.__quantidade = quantidade
            else:
                self.msg_validacao = 'O campo "Quantidade" não pode ser negativo!'
        else:
            self.msg_validacao = 'O campo "Quantidade" é obrigatório'
