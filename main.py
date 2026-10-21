from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget

# Заливаем весь экран чисто черным цветом (RGB: 0, 0, 0)
Window.clearcolor = (0, 0, 0, 1)


class PixelCanvas(Widget):

    def on_touch_down(self, touch):
        # Когда нажимаем на экран, рисуем на холсте
        with self.canvas:
            # Выбираем белый цвет (RGB: 1, 1, 1)
            Color(1, 1, 1, 1)
            # Ставим точку размером 1x1 пиксель в месте касания (touch.x, touch.y)
            Rectangle(pos=(touch.x, touch.y), size=(1, 1))


class WhitePixelApp(App):

    def build(self):
        return PixelCanvas()


if __name__ == '__main__':
    WhitePixelApp().run()
