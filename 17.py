
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class TelaLogin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(cols=1, spacing=10, padding=(20, 20))
        layout.add_widget(Image(source='materiasrepositorio792-1507924830.jpeg', size_hint_y=None, height=200))

        layout_usuario_senha = GridLayout(cols=2, spacing=10, size_hint_y=None, height=100)

        # Nome de Usuário
        label_username = Label(text='Nome de Usuário:', size_hint_x=None, width=150)
        self.username_input = TextInput(multiline=False, size_hint_x=None, width=200)
        layout_usuario_senha.add_widget(label_username)
        layout_usuario_senha.add_widget(self.username_input)

        # Senha
        label_password = Label(text='Senha:', size_hint_x=None, width=150)
        self.password_input = TextInput(password=True, multiline=False, size_hint_x=None, width=200)
        layout_usuario_senha.add_widget(label_password)
        layout_usuario_senha.add_widget(self.password_input)

        layout.add_widget(layout_usuario_senha)

        # Botão de Login
        self.botao_login = Button(text="Login", size_hint=(None, None), size=(200, 40))
        self.botao_login.bind(on_press=self.login)
        layout.add_widget(self.botao_login)

        # Botão de Registro
        self.botao_registro = Button(text="Registrar", size_hint=(None, None), size=(200, 40))
        self.botao_registro.bind(on_press=self.redirecionar_para_registro)
        layout.add_widget(self.botao_registro)

        # Botão de Esqueci Minha Senha
        self.botao_esqueci_senha = Button(text="Esqueci Minha Senha", size_hint=(None, None), size=(200, 40))
        self.botao_esqueci_senha.bind(on_press=self.redirecionar_para_esqueci_senha)
        layout.add_widget(self.botao_esqueci_senha)

        # Rótulo para exibir mensagens
        self.label_mensagem = Label()
        layout.add_widget(self.label_mensagem)

        self.add_widget(layout)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        if username == "usuario" and password == "senha":
            self.label_mensagem.text = "Login bem-sucedido!"
        else:
            self.label_mensagem.text = "Login falhou. Verifique suas credenciais."

    def redirecionar_para_registro(self, instance):
        self.manager.current = 'registro'

    def redirecionar_para_esqueci_senha(self, instance):
        self.manager.current = 'esqueci_senha'


class TelaRegistro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(cols=2, spacing=10, padding=(20, 20))
        layout.add_widget(Label(text="Nome de Usuário:"))
        self.username_input = TextInput(multiline=False, size_hint=(None, None), width=200, height=40)
        layout.add_widget(self.username_input)

        layout.add_widget(Label(text="Email:"))
        self.email_input = TextInput(multiline=False, size_hint=(None, None), width=200, height=40)
        layout.add_widget(self.email_input)

        layout.add_widget(Label(text="Senha:"))
        self.password_input = TextInput(password=True, multiline=False, size_hint=(None, None), width=200, height=40)
        layout.add_widget(self.password_input)

        self.botao_registro = Button(text="Registrar", size_hint=(None, None), width=200, height=40)
        self.botao_registro.bind(on_press=self.registrar)
        layout.add_widget(self.botao_registro)

        self.label_mensagem = Label()
        layout.add_widget(self.label_mensagem)

        self.add_widget(layout)

    def registrar(self, instance):
        username = self.username_input.text
        email = self.email_input.text
        password = self.password_input.text
        if len(username) == 0 or len(email) == 0 or len(password) == 0:
            self.label_mensagem.text = "Por favor, preencha todos os campos."
        else:
            self.label_mensagem.text = "Registro bem-sucedido!"


class TelaEsqueciSenha(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(cols=1, spacing=10, padding=(20, 20))
        layout.add_widget(Label(text="Esqueci Minha Senha"))
        layout.add_widget(Label(text="Por favor, insira seu endereço de e-mail:"))

        self.email_input = TextInput(multiline=False, size_hint=(None, None), width=200, height=40)
        layout.add_widget(self.email_input)

        botao_enviar = Button(text="Enviar", size_hint=(None, None), width=200, height=40)
        botao_enviar.bind(on_press=self.enviar_link)
        layout.add_widget(botao_enviar)

        self.label_mensagem = Label()
        layout.add_widget(self.label_mensagem)

        self.add_widget(layout)

    def enviar_link(self, instance):
        email = self.email_input.text
        if len(email) == 0:
            self.label_mensagem.text = "Por favor, insira um endereço de e-mail válido."
        else:
            self.label_mensagem.text = "Link de redefinição de senha enviado para {}".format(email)


class AppLogin(App):
    def build(self):
        Window.size = (400, 600)  # Definindo tamanho da tela como 400x600
        

        Window.size = (360, 640)  # Definindo o tamanho da janela para se parecer com um celular
        Window.minimum_width, Window.minimum_height = Window.size  # Bloqueando o redimensionamento
        Window.maximum_width, Window.maximum_height = Window.size  # Bloqueando o redimensionamento
        gerenciador_de_telas = ScreenManager()
        gerenciador_de_telas.add_widget(TelaLogin(name='login'))
        gerenciador_de_telas.add_widget(TelaRegistro(name='registro'))
        gerenciador_de_telas.add_widget(TelaEsqueciSenha(name='esqueci_senha'))
        return gerenciador_de_telas


if __name__ == "__main__":
    AppLogin().run()

