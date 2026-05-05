#!/usr/bin/env -S uv run --script
import kivy

kivy.require('2.3.1') # replace with your current kivy version !

from kivy.app import App

from core.interface import Screen

# Test Function
def Pri(instance):
    print("TEXTO")

tela = Screen.Grid()
tela.addButton("Teste 1", Pri, (50, 50))
tela.addButton("TESTE 2", POSITION=(130, 300))


class Interface(App):

    def build(self):
        return tela()


if __name__ == '__main__':
    Interface().run()