from kivy.app import App
from kivy.uix.label import Label 

class MinhaApp(App):
    def build(self):
        return Label(
            text='kkk',
            halign='left',
            valign='top',
            size_hint=(None,None),
            size=(400, 400),
            text_size=(None,None)
        )

    
if __name__ == '__main__':
    MinhaApp().run()
