from View.view import view
from Model.model import model
from Controller.controller import controller

if __name__ == "__main__" :
    vista = view()
    modelo = model()
    controlador = controller(vista,modelo)
    vista.iniciar()
    