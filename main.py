from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import requests


class MoodyApp(App):
    def build(self):
        self.cam_obj = Camera(play=True, resolution=(800, 800))

        # button
        button1 = Button(text="Click")
        button1.size_hint = (0.5, 0.2)
        button1.pos_hint = {"x": 0.25, "y": 0.25}

        button1.bind(on_press=self.take_pic)

        # button

        button2 = Button(text="Predict Emotion")
        button2.size_hint = (0.5, 0.2)
        button2.pos_hint = {"x": 0.25, "y": 0.25}
        button2.bind(on_press=self.send_img)

        # Layout

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.cam_obj)
        layout.add_widget(button1)
        layout.add_widget(button2)

        return layout

    def take_pic(self, *args):

        self.cam_obj.export_as_image().save("Images/pic.jpg")

    def send_img(self, *args):
        url = "https://emotion-detection-api2.herokuapp.com/predict"

        payload = {}
        files = [
            ("image", ("Neutral2.jpg", open("Images/image.jpg", "rb"), "image/jpeg"))
        ]
        headers = {}

        response = requests.request(
            "POST", url, headers=headers, data=payload, files=files
        )

        print(response.text)


if __name__ == "__main__":
    MoodyApp().run()