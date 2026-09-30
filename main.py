# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp

Window.clearcolor = (0.06, 0.08, 0.12, 1)

KV = '''
<RootWidget>:
    orientation: 'vertical'
    padding: dp(15)
    spacing: dp(10)

    Label:
        text: '✨ Text Styler ✨'
        font_size: '26sp'
        bold: True
        color: 0, 0.83, 1, 1
        size_hint_y: None
        height: dp(50)

    Label:
        text: 'اكتب النص ثم اختر الشكل:'
        font_size: '14sp'
        color: 0.8, 0.8, 0.8, 1
        size_hint_y: None
        height: dp(30)

    TextInput:
        id: text_input
        hint_text: 'اكتب هنا...'
        multiline: False
        size_hint_y: None
        height: dp(60)
        background_color: 0.1, 0.12, 0.18, 1
        foreground_color: 1, 1, 1, 1
        cursor_color: 0, 0.83, 1, 1
        font_size: '16sp'

    BoxLayout:
        size_hint_y: None
        height: dp(50)
        spacing: dp(8)

        Button:
            text: '⌐╦╦═─'
            background_normal: ''
            background_color: 0.15, 0.4, 0.6, 1
            on_release: root.style_text('box1')

        Button:
            text: '▄▀▄▀▄'
            background_normal: ''
            background_color: 0.2, 0.5, 0.3, 1
            on_release: root.style_text('box2')

        Button:
            text: '★彡'
            background_normal: ''
            background_color: 0.6, 0.4, 0.1, 1
            on_release: root.style_text('star')

        Button:
            text: '♛'
            background_normal: ''
            background_color: 0.5, 0.2, 0.5, 1
            on_release: root.style_text('crown')

    Label:
        text: 'النتيجة:'
        font_size: '14sp'
        bold: True
        color: 0, 1, 0.53, 1
        size_hint_y: None
        height: dp(30)

    ScrollView:
        Label:
            id: result_label
            text: '(ستظهر النتيجة هنا)'
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.width, None
            padding: dp(10)
            font_size: '18sp'
            color: 1, 1, 1, 1
            halign: 'center'
            valign: 'middle'
'''

Builder.load_string(KV)


class RootWidget(BoxLayout):
    def style_text(self, style):
        text = self.ids.text_input.text.strip()
        if not text:
            self.ids.result_label.text = "⚠️ اكتب نصاً أولاً!"
            return

        if style == 'box1':
            result = "⌐╦╦═─ " + text + " ─═╦╦⌐"
        elif style == 'box2':
            result = "▄▀▄▀▄ " + text + " ▄▀▄▀▄"
        elif style == 'star':
            result = "★彡[ " + text + " ]彡★"
        elif style == 'crown':
            result = "♛━━ " + text + " ━━♛"
        else:
            result = text

        self.ids.result_label.text = result


class SimpleTextApp(App):
    def build(self):
        self.title = "Text Styler"
        return RootWidget()


if __name__ == '__main__':
    SimpleTextApp().run()
