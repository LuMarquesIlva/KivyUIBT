#!/usr/bin/env -S uv run --script
import kivy

kivy.require('2.3.1') # replace with your current kivy version !

from kivy.app import App

from core.interface import Screen

# Test Function
def Pri(instance):
    print("TEXTO")

tela = Screen.Box('horizontal', 100)
tela.addGridLayout()
TelaGrid = tela.getGrid()

TelaGrid.setRows(3)
TelaGrid.setCols(3)

for x in range(6):
    if x == 3:
        TelaGrid.addLabel(f"[color=ff3333]TEST[/color] {x}")
        print("YEAHHSH")
        print(TelaGrid.WidgetsList)
        continue
    TelaGrid.addButton(f"TEST {x}")

TelaGrid.renderWidgets()

tela.addButton("Test 1", Pri, (50, 50))
tela.addLabel("TEXTO")
tela.changeOrientation('vertical')
#tela.addButton("TESTE 2", POSITION=(130, 300))


class Interface(App):

    def build(self):
        return tela()


if __name__ == '__main__':
    Interface().run()