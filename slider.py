from kivy.app import App 
from kivy.uix.slider import Slider

class MyApp(App):
    def build(self):
        return Slider(min=40, max=700, value = 80)
if __name__ == "__main__":
    MyApp().run()