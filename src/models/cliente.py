class Cliente:

    def __init__(self) -> None:
        self.__nome: str = ""
        self.__cpf: str = ""
        self.__endereco: str = ""
        self.__bairro: str = ""
        self.__email: str = ""
        self.__fone: str = ""
        self.__categoria: str = ""
        self.msg_validacao: str = ""

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if nome != "":
            self.__nome = nome
        else:
            self.msg_validacao = 'O campo "Nome" é obrigatório!'

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str) -> None:
        if cpf != "":
            self.__cpf = cpf
        else:
            self.msg_validacao = 'O campo "CPF" é obrigatório!'

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str) -> None:
        if endereco != "":
            self.__endereco = endereco
        else:
            self.msg_validacao = 'O campo "Endereço" é obrigatório!'

    @property
    def bairro(self) -> str:
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro: str) -> None:
        if bairro != "":
            self.__bairro = bairro
        else:
            self.msg_validacao = 'O campo "Bairro" é obrigatório!'

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        if email != "":
            self.__email = email
        else:
            self.msg_validacao = 'O campo "E-mail" é obrigatório!'

    @property
    def fone(self) -> str:
        return self.__fone

    @fone.setter
    def fone(self, fone: str) -> None:
        if fone != "":
            self.__fone = fone
        else:
            self.msg_validacao = 'O campo "Fone" é obrigatório!'

    @property
    def categoria(self) -> str:
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria: str) -> None:
        if categoria != "" and categoria != "-":
            self.__categoria = categoria
        else:
            self.msg_validacao = 'O campo "Categoria" é obrigatório!'
