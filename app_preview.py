from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class ChatUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.chat = Label(
            text="AI Chat\n\nHello! I am ready.",
            size_hint_y=0.8
        )

        self.input = TextInput(
            hint_text="Type your message...",
            size_hint_y=0.1,
            multiline=False
        )

        self.send_btn = Button(
            text="Send",
            size_hint_y=0.1
        )
        self.send_btn.bind(on_press=self.send_message)

        self.add_widget(self.chat)
        self.add_widget(self.input)
        self.add_widget(self.send_btn)

    def send_message(self, instance):
        msg = self.input.text.strip()
        if msg:
            self.chat.text += f"\n\nYou: {msg}\nAI: (response here)"
            self.input.text = ""


class AIChatApp(App):
    def build(self):
        return ChatUI()


if __name__ == "__main__":
    AIChatApp().run()
