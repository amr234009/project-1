import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.core.window import Window
Window.size=(400,600)
Builder.load_string('''
<Helloworldscreen>:
    cols:1
    label:
    Button:
        text: 'start [sebah] : %d' % root.counter
        on_release: root.my_callback()
''')
class Helloworldscreen(GridLayout):
    counter = NumericProperty(0)
    def my_callback(self):
        self.counter +=1
class Fapp(App):
    def build(self):
        return Helloworldscreen()
    
if __name__ == '__main__':
    Fapp().run()