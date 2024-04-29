from kivy.app import App 
from kivy.uix.checkbox import Image

class MinhaApp(App):
    def build(self):
        return Image(source="/Users/aluno.sesipaulista/Desktop/hellenzinha/minha princesa é gostosa/25916255-28be-47b7-aa92-3676d0496f2c.jpg")
    
if __name__ == "__main__":
    MinhaApp().run()