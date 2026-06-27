class Nodo:
    def __init__(self, palabra_es, palabra_en):
        self.palabra_es = palabra_es
        self.palabra_en = palabra_en
        self.izq = None
        self.der = None

class DiccionarioBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, palabra_es, palabra_en):
        self.raiz = self._insertar(self.raiz, palabra_es, palabra_en)

    def _insertar(self, nodo, palabra_es, palabra_en):
        if nodo is None:
            return Nodo(palabra_es, palabra_en)
        if palabra_es < nodo.palabra_es:
            nodo.izq = self._insertar(nodo.izq, palabra_es, palabra_en)
        elif palabra_es > nodo.palabra_es:
            nodo.der = self._insertar(nodo.der, palabra_es, palabra_en)
        else:
            nodo.palabra_en = palabra_en  # actualizar traducción
        return nodo

    def buscar(self, palabra_es):
        return self._buscar(self.raiz, palabra_es)

    def _buscar(self, nodo, palabra_es):
        if nodo is None:
            return None
        if palabra_es == nodo.palabra_es:
            return nodo.palabra_en
        elif palabra_es < nodo.palabra_es:
            return self._buscar(nodo.izq, palabra_es)
        else:
            return self._buscar(nodo.der, palabra_es)

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izq, resultado)
            resultado.append((nodo.palabra_es, nodo.palabra_en))
            self._inorden(nodo.der, resultado)
