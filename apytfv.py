from kivy.app import App 
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):
        return AsyncImage(source="https://resizing.flixster.com/ybhJbc83wFrkLr9bDH45KMxAwJw=/206x305/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p17155833_b_v13_aa.jpg")
    
if __name__ == "__main__":
    MinhaApp().run()