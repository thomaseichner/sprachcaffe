#!/usr/bin/env python

"""sprachcaffe_app.py: docstring"""

__author__ = 'thomas'
__creation_date__ = '03.02.19'


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class SprachCaffe(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        camera.export_to_png("IMG.png")
        print("Captured")


class SprachCaffeApp(App):
    def build(self):
        return SprachCaffe()


if __name__ == '__main__':
    SprachCaffeApp().run()