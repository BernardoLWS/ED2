class NodoAMV:
    def __init__(self, indice, datos=None):
        self.indice = indice          # clave principal
        self.datos = datos or []      # lista de valores asociados
        self.izq = None
        self.der = None
        self.altura = 1

class ArbolAMV:
    def __init__(self):
        self.raiz = None

    def insertar(self, indice, dato=None):
        self.raiz = self._insertar(self.raiz, indice, dato)

    def _insertar(self, nodo, indice, dato):
        if nodo is None:
            return NodoAMV(indice, [dato] if dato else [])

        if indice < nodo.indice:
            nodo.izq = self._insertar(nodo.izq, indice, dato)
        elif indice > nodo.indice:
            nodo.der = self._insertar(nodo.der, indice, dato)
        else:
            # si el índice ya existe, agregamos el dato a su lista
            if dato is not None:
                nodo.datos.append(dato)
        return nodo

    def in_orden(self):
        return self._in_orden(self.raiz)

    def _in_orden(self, nodo):
        if nodo is None:
            return []
        return self._in_orden(nodo.izq) + [(nodo.indice, nodo.datos)] + self._in_orden(nodo.der)

# ------------------ Ejemplo de uso ------------------
def main():
    arbol = ArbolAMV()
    # Insertamos raíces con sus datos
    arbol.insertar(5, 3)
    arbol.insertar(5, 4)
    arbol.insertar(10, 8)
    arbol.insertar(30, 40)

    print("InOrden:", arbol.in_orden())

if __name__ == "__main__":
    main()
