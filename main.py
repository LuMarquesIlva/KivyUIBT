#!/usr/bin/env -S uv run --script
import kivy

kivy.require('2.3.1') # replace with your current kivy version !

from kivy.app import App

from core.interface import Screen

# Test Function
def Pri(instance):
    print("TEXTO")

Screen.Grid.addButton("Teste 1", Pri, (50, 50))


class Interface(App):

    def build(self):
        return Screen()


if __name__ == '__main__':
    Interface().run()