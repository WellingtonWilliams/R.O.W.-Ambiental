from typing import List
from models.usuario import Usuario


class UsuarioControl:

    def __init__(self):
        self.__lista_usuarios: List[Usuario] = []

    def adicionar_usuario(self, usuario: Usuario) -> str:
        self.__lista_usuarios.append(usuario)
        return "Usuário adicionado com sucesso"

    def consultar_usuario(self, user: str, senha_1: str) -> bool:
        confirmar = False
        for usuario in self.__lista_usuarios:
            if usuario.user == user and usuario.senha_1 == senha_1:
                confirmar = True
                break
        return confirmar

    def acessar_usuario(self, indice: int) -> Usuario:
        usuario = self.__lista_usuarios[indice]
        return usuario

    def alterar_usuario(self, indice: int, usuario: Usuario) -> str:
        self.__lista_usuarios[indice] = usuario
        return "Usuário alterado com sucesso"

    def excluir_usuario(self, indice: int) -> str:
        del self.__lista_usuarios[indice]
        return "Usuário excluído com sucesso"

    @property
    def lista_usuarios(self) -> List[Usuario]:
        return self.__lista_usuarios

    @lista_usuarios.setter
    def lista_usuarios(self, lista: List[Usuario]) -> None:
        pass
