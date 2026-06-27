from view.view import DiccionarioView
from model.model import DiccionarioBST
from controller.controller import DiccionarioController
import tkinter as tk


def main():
    ventana = tk.Tk()
    modelo = DiccionarioBST()
    vista = DiccionarioView(ventana)
    controlador = DiccionarioController(modelo, vista)
    vista.set_controlador(controlador)
    ventana.mainloop()


if __name__ == "__main__":
    main()