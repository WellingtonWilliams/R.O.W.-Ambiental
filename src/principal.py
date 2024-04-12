import sys

from gui_principal import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QTableWidgetItem
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from models.cliente import Cliente
from models.servico import Servico
from models.usuario import Usuario
from controllers.cliente_control import ClienteControl
from controllers.servico_control import ServicoControl
from controllers.usuario_control import UsuarioControl


class Principal(Ui_MainWindow, QMainWindow):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.inicializar_componentes()
        self.controle_cliente = ClienteControl()
        self.controle_servico = ServicoControl()
        self.controle_usuario = UsuarioControl()
        self.usuario_padrao()
        self.erro = "background-color: rgb(255, 0, 0); color: rgb(255, 255, 255)"
        self.sucesso = "background-color: rgb(0, 155, 119); color: rgb(255, 255, 255)"

    def inicializar_componentes(self) -> None:

        # page_login
        self.frame_login_msg.hide()
        self.label_login_icone.setPixmap(QPixmap("src/img/user_icon.png"))
        self.pushButton_login_entrar.clicked.connect(self.realizar_login)
        self.pushButton_login_cadastrar.clicked.connect(self.acessar_cadastro_usuario)
        self.pushButton_login_fechar_msg.clicked.connect(self.frame_login_msg.hide)

        # page_principal
        self.label_principal_logo.setPixmap(QPixmap("src/img/logo_ROW_maior.png"))
        self.pushButton_principal_cliente.clicked.connect(self.acessar_cad_cliente)
        self.pushButton_principal_servicos.clicked.connect(self.acessar_cad_servicos)
        self.pushButton_principal_usuarios.clicked.connect(self.acessar_usuarios)
        self.pushButton_principal_sair.clicked.connect(self.sair)

        # page_cad_cliente
        self.frame_cad_cliente_msg.hide()
        self.label_cad_cliente_logo.setPixmap(QPixmap("src/img/logo_ROW_menor.png"))
        self.pushButton_cad_cliente_salvar.clicked.connect(self.salvar_cliente)
        self.pushButton_cad_cliente_lista.clicked.connect(self.acessar_list_cliente)
        self.pushButton_cad_cliente_voltar.clicked.connect(self.acessar_principal)
        self.pushButton_cad_cliente_fechar_msg.clicked.connect(
            self.frame_cad_cliente_msg.hide
        )

        # page_list_cliente
        self.frame_list_cliente_msg.hide()
        self.label_list_cliente_logo.setPixmap(QPixmap("src/img/logo_ROW_menor.png"))
        self.pushButton_list_cliente_alterar.clicked.connect(self.alterar_dados_cliente)
        self.pushButton_list_cliente_excluir.clicked.connect(self.excluir_cliente)
        self.pushButton_list_cliente_voltar.clicked.connect(self.acessar_principal)
        self.pushButton_list_cliente_fechar_msg.clicked.connect(
            self.frame_list_cliente_msg.hide
        )

        # page_cad_servicos
        self.frame_cad_servicos_msg.hide()
        self.label_cad_servicos_logo.setPixmap(QPixmap("src/img/logo_ROW_menor.png"))
        self.pushButton_cad_servicos_salvar.clicked.connect(self.salvar_servico)
        self.pushButton_cad_servicos_listar.clicked.connect(self.acessar_list_servicos)
        self.pushButton_cad_servicos_voltar.clicked.connect(self.acessar_principal)
        self.pushButton_cad_servicos_fechar_msg.clicked.connect(
            self.frame_cad_servicos_msg.hide
        )

        # page_list_servicos
        self.frame_list_servicos_msg.hide()
        self.label_list_servicos_logo.setPixmap(QPixmap("src/img/logo_ROW_menor.png"))
        self.pushButton_list_servicos_alterar.clicked.connect(self.alterar_servico)
        self.pushButton_list_servicos_excluir.clicked.connect(self.excluir_servico)
        self.pushButton_list_servicos_voltar.clicked.connect(self.acessar_principal)
        self.pushButton_list_servicos_fechar_msg.clicked.connect(
            self.frame_list_servicos_msg.hide
        )

        # page_cadastro_usuario
        self.frame_cad_usuario_msg.hide()
        self.label_cad_usuario_icone.setPixmap(QPixmap("src/img/user_icon.png"))
        self.pushButton_cad_usuario_cadastrar.clicked.connect(self.cadastrar_usuario)
        self.pushButton_cad_usuario_sair.clicked.connect(self.sair)
        self.pushButton_cad_usuario_fechar_msg.clicked.connect(
            self.frame_cad_usuario_msg.hide
        )

        # page_usuarios
        self.frame_usuarios_msg.hide()
        self.label_usuarios_logo.setPixmap(QPixmap("src/img/logo_ROW_menor.png"))
        self.pushButton_usuarios_alterar.clicked.connect(self.alterar_dados_usuario)
        self.pushButton_usuarios_excluir.clicked.connect(self.excluir_usuario)
        self.pushButton_usuarios_cadastrar.clicked.connect(
            self.acessar_cadastro_usuario
        )
        self.pushButton_usuarios_voltar.clicked.connect(self.acessar_principal)
        self.pushButton_usuarios_fechar_msg.clicked.connect(
            self.frame_usuarios_msg.hide
        )

    def usuario_padrao(self) -> None:
        admin = Usuario()
        admin.nome = "Admin Bot"
        admin.user = "admin"
        admin.senha_1 = "12345"
        admin.senha_2 = "12345"
        self.controle_usuario.adicionar_usuario(admin)

    def realizar_login(self) -> None:
        login = self.lineEdit_login_user.text()
        senha = self.lineEdit_login_senha.text()
        if self.controle_usuario.consultar_usuario(login, senha):
            self.lineEdit_login_user.clear()
            self.lineEdit_login_senha.clear()
            self.frame_login_msg.hide()
            self.__atualizar_sistema()
            self.acessar_principal()
            print("Login realizado com sucesso!")
        else:
            msg = "Login ou Senha incorretos"
            self.label_login_msg.setText(msg)
            self.label_login_msg.setStyleSheet(self.erro)
            self.frame_login_msg.show()

    # Métodos de Cliente

    def salvar_cliente(self) -> None:
        indice = self.tableWidget_list_cliente.currentRow()
        cliente = Cliente()
        cliente.nome = self.lineEdit_cad_cliente_nome.text()
        cliente.cpf = self.lineEdit_cad_cliente_cpf.text()
        cliente.endereco = self.lineEdit_cad_cliente_endereco.text()
        cliente.bairro = self.lineEdit_cad_cliente_bairro.text()
        cliente.email = self.lineEdit_cad_cliente_email.text()
        cliente.fone = self.lineEdit_cad_cliente_fone.text()
        cliente.categoria = self.comboBox_cad_cliente_categoria.currentText()
        if cliente.msg_validacao != "":
            self.label_cad_cliente_msg.setText(cliente.msg_validacao)
            self.label_cad_cliente_msg.setStyleSheet(self.erro)
            self.frame_cad_cliente_msg.show()
        else:
            if indice >= 0:
                msg = self.controle_cliente.alterar_cliente(indice, cliente)
                self.label_cad_cliente_msg.setText(msg)
                self.label_cad_cliente_msg.setStyleSheet(self.sucesso)
                self.frame_cad_cliente_msg.show()
                self.tabelar_cliente()
                self.limpar_formulario_cliente()
                self.tableWidget_list_cliente.clearSelection()
            else:
                msg = self.controle_cliente.adicionar_cliente(cliente)
                self.label_cad_cliente_msg.setText(msg)
                self.label_cad_cliente_msg.setStyleSheet(self.sucesso)
                self.frame_cad_cliente_msg.show()
                self.tabelar_cliente()
                self.limpar_formulario_cliente()

    def tabelar_cliente(self) -> None:
        cont_linhas = 0
        self.tableWidget_list_cliente.clearContents()
        self.tableWidget_list_cliente.setRowCount(
            len(self.controle_cliente.lista_clientes)
        )
        for cliente in self.controle_cliente.lista_clientes:
            self.tableWidget_list_cliente.setItem(
                cont_linhas, 0, QTableWidgetItem(cliente.nome)
            )
            self.tableWidget_list_cliente.setItem(
                cont_linhas, 1, QTableWidgetItem(cliente.cpf)
            )
            self.tableWidget_list_cliente.setItem(
                cont_linhas, 2, QTableWidgetItem(cliente.endereco)
            )
            self.tableWidget_list_cliente.setItem(
                cont_linhas, 3, QTableWidgetItem(cliente.bairro)
            )
            self.tableWidget_list_cliente.setItem(
                cont_linhas, 4, QTableWidgetItem(cliente.email)
            )
            self.tableWidget_list_cliente.setItem(
                cont_linhas, 5, QTableWidgetItem(cliente.fone)
            )
            self.tableWidget_list_cliente.setItem(
                cont_linhas, 6, QTableWidgetItem(cliente.categoria)
            )
            cont_linhas += 1

    def alterar_dados_cliente(self) -> None:
        indice = self.tableWidget_list_cliente.currentRow()
        if indice >= 0:
            cliente = self.controle_cliente.acessar_cliente(indice)
            self.lineEdit_cad_cliente_nome.setText(cliente.nome)
            self.lineEdit_cad_cliente_cpf.setText(cliente.cpf)
            self.lineEdit_cad_cliente_endereco.setText(cliente.endereco)
            self.lineEdit_cad_cliente_bairro.setText(cliente.bairro)
            self.lineEdit_cad_cliente_email.setText(cliente.email)
            self.lineEdit_cad_cliente_fone.setText(cliente.fone)
            if cliente.categoria == "Nível 1":
                i = 1
            elif cliente.categoria == "Nível 2":
                i = 2
            elif cliente.categoria == "Nível 3":
                i = 3
            self.comboBox_cad_cliente_categoria.setCurrentIndex(i)
            self.acessar_cad_cliente()
        else:
            msg = "Selecione o Cliente a ser alterado"
            self.label_list_cliente_msg.setText(msg)
            self.label_list_cliente_msg.setStyleSheet(self.erro)
            self.frame_list_cliente_msg.show()

    def excluir_cliente(self) -> None:
        indice = self.tableWidget_list_cliente.currentRow()
        if indice >= 0:
            msg = self.controle_cliente.excluir_cliente(indice)
            self.label_list_cliente_msg.setText(msg)
            self.label_list_cliente_msg.setStyleSheet(self.sucesso)
            self.frame_list_cliente_msg.show()
            self.tabelar_cliente()
            self.tableWidget_list_cliente.clearSelection()
        else:
            msg = "Selecione o Cliente a ser excluído"
            self.label_list_cliente_msg.setText(msg)
            self.label_list_cliente_msg.setStyleSheet(self.erro)
            self.frame_list_cliente_msg.show()

    def limpar_formulario_cliente(self) -> None:
        self.lineEdit_cad_cliente_nome.clear()
        self.lineEdit_cad_cliente_cpf.clear()
        self.lineEdit_cad_cliente_endereco.clear()
        self.lineEdit_cad_cliente_bairro.clear()
        self.lineEdit_cad_cliente_email.clear()
        self.lineEdit_cad_cliente_fone.clear()
        self.comboBox_cad_cliente_categoria.setCurrentIndex(0)

    # Métodos Serviço

    def salvar_servico(self) -> None:
        indice = self.tableWidget_list_servicos.currentRow()
        servico = Servico()
        servico.nome_servico = self.lineEdit_cad_servicos_nome.text()
        servico.codigo = self.lineEdit_cad_servicos_codigo.text()
        servico.preco = self.lineEdit_cad_servicos_preco.text()
        servico.quantidade = self.lineEdit_cad_servicos_quantidade.text()
        if servico.msg_validacao != "":
            self.label_cad_servicos_msg.setText(servico.msg_validacao)
            self.label_cad_servicos_msg.setStyleSheet(self.erro)
            self.frame_cad_servicos_msg.show()
        else:
            if indice >= 0:
                msg = self.controle_servico.alterar_servico(indice, servico)
                self.label_cad_servicos_msg.setText(msg)
                self.label_cad_servicos_msg.setStyleSheet(self.sucesso)
                self.frame_cad_servicos_msg.show()
                self.tabelar_servico()
                self.limpar_formulario_servico()
                self.tableWidget_list_servicos.clearSelection()
            else:
                msg = self.controle_servico.adicionar_servico(servico)
                self.label_cad_servicos_msg.setText(msg)
                self.label_cad_servicos_msg.setStyleSheet(self.sucesso)
                self.frame_cad_servicos_msg.show()
                self.tabelar_servico()
                self.limpar_formulario_servico()

    def tabelar_servico(self) -> None:
        cont_linhas = 0
        self.tableWidget_list_servicos.clearContents()
        self.tableWidget_list_servicos.setRowCount(
            len(self.controle_servico.lista_servicos)
        )
        for servico in self.controle_servico.lista_servicos:
            self.tableWidget_list_servicos.setItem(
                cont_linhas, 0, QTableWidgetItem(servico.nome_servico)
            )
            self.tableWidget_list_servicos.setItem(
                cont_linhas, 1, QTableWidgetItem(servico.codigo)
            )
            self.tableWidget_list_servicos.setItem(
                cont_linhas, 2, QTableWidgetItem(servico.preco)
            )
            self.tableWidget_list_servicos.setItem(
                cont_linhas, 3, QTableWidgetItem(servico.quantidade)
            )
            cont_linhas += 1

    def alterar_servico(self) -> None:
        indice = self.tableWidget_list_servicos.currentRow()
        if indice >= 0:
            servico = self.controle_servico.acessar_servico(indice)
            self.lineEdit_cad_servicos_nome.setText(servico.nome_servico)
            self.lineEdit_cad_servicos_codigo.setText(servico.codigo)
            self.lineEdit_cad_servicos_preco.setText(servico.preco)
            self.lineEdit_cad_servicos_quantidade.setText(servico.quantidade)
            self.acessar_cad_servicos()
        else:
            msg = "Selecione o Serviço a ser alterado"
            self.label_list_servicos_msg.setText(msg)
            self.label_list_servicos_msg.setStyleSheet(self.erro)
            self.frame_list_servicos_msg.show()

    def excluir_servico(self) -> None:
        indice = self.tableWidget_list_servicos.currentRow()
        if indice >= 0:
            msg = self.controle_servico.excluir_servico(indice)
            self.label_list_servicos_msg.setText(msg)
            self.label_list_servicos_msg.setStyleSheet(self.sucesso)
            self.frame_list_servicos_msg.show()
            self.tabelar_servico()
            self.tableWidget_list_servicos.clearSelection()
        else:
            msg = "Selecione o Serviço a ser excluído"
            self.label_list_servicos_msg.setText(msg)
            self.label_list_servicos_msg.setStyleSheet(self.erro)
            self.frame_list_servicos_msg.show()

    def limpar_formulario_servico(self) -> None:
        self.lineEdit_cad_servicos_nome.clear()
        self.lineEdit_cad_servicos_codigo.clear()
        self.lineEdit_cad_servicos_preco.clear()
        self.lineEdit_cad_servicos_quantidade.clear()

    # Métodos Usuários

    def cadastrar_usuario(self) -> None:
        indice = self.tableWidget_usuarios.currentRow()
        usuario = Usuario()
        usuario.nome = self.lineEdit_cad_usuario_nome.text()
        user = self.lineEdit_cad_usuario_user.text()
        usuario.user = user
        senha_1 = self.lineEdit_cad_usuario_senha_1.text()
        usuario.senha_1 = senha_1
        usuario.senha_2 = self.lineEdit_cad_usuario_senha_2.text()
        if usuario.msg_validacao != "":
            self.label_cad_usuario_msg.setText(usuario.msg_validacao)
            self.label_cad_usuario_msg.setStyleSheet(self.erro)
            self.frame_cad_usuario_msg.show()
        else:
            if indice > 0:
                msg = self.controle_usuario.alterar_usuario(indice, usuario)
                self.label_cad_usuario_msg.setText(msg)
                self.label_cad_usuario_msg.setStyleSheet(self.sucesso)
                self.frame_cad_usuario_msg.show()
                self.tabelar_usuarios()
                self.tableWidget_usuarios.clearSelection()
                self.limpar_formulario_usuario()
            else:
                if self.controle_usuario.consultar_usuario(user, senha_1):
                    msg = "Nome de usuário já utilizado"
                    self.label_cad_usuario_msg.setText(msg)
                    self.label_cad_usuario_msg.setStyleSheet(self.erro)
                    self.frame_cad_usuario_msg.show()
                else:
                    msg = self.controle_usuario.adicionar_usuario(usuario)
                    self.label_cad_usuario_msg.setText(msg)
                    self.label_cad_usuario_msg.setStyleSheet(self.sucesso)
                    self.frame_cad_usuario_msg.show()
                    self.tabelar_usuarios()
                    self.limpar_formulario_usuario()

    def tabelar_usuarios(self) -> None:
        cont_linhas = 0
        self.tableWidget_usuarios.clearContents()
        self.tableWidget_usuarios.setRowCount(len(self.controle_usuario.lista_usuarios))
        for usuario in self.controle_usuario.lista_usuarios:
            self.tableWidget_usuarios.setItem(
                cont_linhas, 0, QTableWidgetItem(usuario.nome)
            )
            self.tableWidget_usuarios.setItem(
                cont_linhas, 1, QTableWidgetItem(usuario.user)
            )
            cont_linhas += 1

    def alterar_dados_usuario(self) -> None:
        indice = self.tableWidget_usuarios.currentRow()
        if indice >= 0:
            if indice > 0:
                usuario = self.controle_usuario.acessar_usuario(indice)
                self.lineEdit_cad_usuario_nome.setText(usuario.nome)
                self.lineEdit_cad_usuario_user.setText(usuario.user)
                self.lineEdit_cad_usuario_senha_1.setText(usuario.senha_1)
                self.lineEdit_cad_usuario_senha_2.setText(usuario.senha_2)
                self.acessar_cadastro_usuario()
            else:
                msg = "Não é permitido alterar o usuário Admin Bot"
                self.label_usuarios_msg.setText(msg)
                self.label_usuarios_msg.setStyleSheet(self.erro)
                self.frame_usuarios_msg.show()
        else:
            msg = "Selecione o usuário que deseja alterar"
            self.label_usuarios_msg.setText(msg)
            self.label_usuarios_msg.setStyleSheet(self.erro)
            self.frame_usuarios_msg.show()

    def excluir_usuario(self) -> None:
        indice = self.tableWidget_usuarios.currentRow()
        if indice >= 0:
            if indice > 0:
                msg = self.controle_usuario.excluir_usuario(indice)
                self.label_usuarios_msg.setText(msg)
                self.label_usuarios_msg.setStyleSheet(self.sucesso)
                self.frame_usuarios_msg.show()
                self.tableWidget_usuarios.clearSelection()
                self.tabelar_usuarios()
            else:
                msg = "Não é possível excluir o usuário Admin Bot"
                self.label_usuarios_msg.setText(msg)
                self.label_usuarios_msg.setStyleSheet(self.erro)
                self.frame_usuarios_msg.show()
        else:
            msg = "Selecione o usuário que deseja excluir"
            self.label_usuarios_msg.setText(msg)
            self.label_usuarios_msg.setStyleSheet(self.erro)
            self.frame_usuarios_msg.show()

    def limpar_formulario_usuario(self) -> None:
        self.lineEdit_cad_usuario_nome.clear()
        self.lineEdit_cad_usuario_user.clear()
        self.lineEdit_cad_usuario_senha_1.clear()
        self.lineEdit_cad_usuario_senha_2.clear()

    # Métodos Gerais

    def acessar_principal(self) -> None:
        self.stackedWidget.setCurrentWidget(self.page_principal)

    def acessar_cad_cliente(self) -> None:
        self.stackedWidget.setCurrentWidget(self.page_cad_cliente)

    def acessar_list_cliente(self) -> None:
        self.stackedWidget.setCurrentWidget(self.page_list_cliente)

    def acessar_cad_servicos(self) -> None:
        self.stackedWidget.setCurrentWidget(self.page_cad_servicos)

    def acessar_list_servicos(self) -> None:
        self.stackedWidget.setCurrentWidget(self.page_list_servicos)

    def acessar_cadastro_usuario(self) -> None:
        self.stackedWidget.setCurrentWidget(self.page_cadastro_usuario)

    def acessar_usuarios(self) -> None:
        self.stackedWidget.setCurrentWidget(self.page_usuarios)

    def sair(self) -> None:
        self.stackedWidget.setCurrentWidget(self.page_login)

    def __atualizar_sistema(self) -> None:
        self.tabelar_cliente()
        self.tabelar_servico()
        self.tabelar_usuarios()


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    qt.exec()
