class Usuario:

    def __init__(self):
        self.__nome: str = ""
        self.__user: str = ""
        self.__senha_1: str = ""
        self.__senha_2: str = ""
        self.msg_validacao: str = ""

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if nome != "":
            self.__nome = nome
        else:
            self.msg_validacao = 'O campo "Nome" é obrigatório'

    @property
    def user(self) -> str:
        return self.__user

    @user.setter
    def user(self, user: str) -> None:
        if user != "":
            self.__user = user
        else:
            self.msg_validacao = 'O campo "User" é obrigatório'

    @property
    def senha_1(self) -> str:
        return self.__senha_1

    @senha_1.setter
    def senha_1(self, senha_1: str) -> None:
        if senha_1 != "":
            if len(senha_1) >= 4 and len(senha_1) <= 8:
                self.__senha_1 = senha_1
            else:
                self.msg_validacao = "A senha deve ter de 4 a 8 caracteres"
        else:
            self.msg_validacao = 'O campo "Senha" é obrigatório'

    @property
    def senha_2(self) -> str:
        return self.__senha_2

    @senha_2.setter
    def senha_2(self, senha_2: str) -> None:
        if senha_2 != "":
            if senha_2 == self.senha_1:
                self.__senha_2 = senha_2
            else:
                self.msg_validacao = "As senhas não coincidem"
        else:
            self.msg_validacao = "É obrigatória a confirmação da Senha"
