from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

# Definición de la interfaz de usuario en KV Language como un string de Python
kv = '''
BoxLayout:
    orientation: 'vertical'
    Label:
        text: '¡Hola Mundo!'
        font_size: 24
    Button:
        text: 'Haz clic aquí'
        on_press: app.saludar()
'''

class Contenedor(BoxLayout):
    pass

class HolaMundoApp(App):
    def build(self):
        # Cargamos la definición de la UI desde el string KV
        return Builder.load_string(kv)

    def saludar(self):
        print("¡Hola desde el botón!")

if __name__ == '__main__':
    HolaMundoApp().run()sudo apt-get in