#!/usr/bin/env -S uv run --script
import kivy

kivy.require('2.3.1') # replace with your current kivy version !

from kivy.app import App

from core.interface import Screen

# Test Function
def Pri(instance):
    print("TEXTO")

tela = Screen.Box('horizontal')
tela.addGridLayout()
TelaGrid = tela.getGrid()

TelaGrid.setRows(3)
TelaGrid.setCols(3)

for x in range(6):
    if x == 3:
        TelaGrid.addLabel(f"[color=ff3333]Texto[/color] {x}")
        continue
    TelaGrid.addButton(f"Botão {x}")

TelaGrid.renderWidgets()

tela.addButton("Botão 1", Pri, (50, 50))

tela.changeOrientation('vertical')
tela.addLabel("Texto")
cam = tela.addCamera()
cam.orientation="vertical"

def playCam(instance):
    cam.play = True

tela.addButton("Botão 3", FUNC=playCam)


class Interface(App):

    def build(self):
        return tela()


if __name__ == '__main__':
    Interface().run()