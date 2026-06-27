class NodoMVias:
    """Clase que representa un nodo de un Árbol M-Vías."""

    def __init__(self, orden, claves=None):
        self.orden = orden  # número máximo de hijos
        self.claves = claves if claves else []
        self.hijos = [None] * orden

    # --- Getters ---
    def get_claves(self):
        return self.claves

    def get_hijo(self, indice):
        if 0 <= indice < self.orden:
            return self.hijos[indice]
        return None

    # --- Setters ---
    def set_claves(self, nuevas_claves):
        self.claves = nuevas_claves

    def set_hijo(self, indice, nodo):
        if 0 <= indice < self.orden:
            self.hijos[indice] = nodo

    
class ArbolMVias:
    """Clase que representa un Árbol M-Vías."""

    def __init__(self, orden):
        self.raiz = None
        self.orden = orden

    # --- Getters ---
    def get_raiz(self):
        return self.raiz

    def es_vacio(self):
        return self.raiz is None

    # --- Setters ---
    def set_raiz(self, nodo):
        self.raiz = nodo

    # --- Operaciones ---
    def insertar(self, clave):
        if self.es_vacio():
            self.raiz = NodoMVias(self.orden, [clave])
        else:
            self._insertar_recursivo(self.raiz, clave)

    def _insertar_recursivo(self, nodo, clave):
        # Si aún hay espacio en el nodo, insertamos la clave
        if len(nodo.claves) < self.orden - 1:
            nodo.claves.append(clave)
            nodo.claves.sort()
        else:
            # Decidir a qué hijo ir
            for i, valor in enumerate(nodo.claves):
                if clave < valor:
                    if nodo.hijos[i] is None:
                        nodo.hijos[i] = NodoMVias(self.orden, [clave])
                    else:
                        self._insertar_recursivo(nodo.hijos[i], clave)
                    return
            # Si es mayor que todas las claves
            if nodo.hijos[-1] is None:
                nodo.hijos[-1] = NodoMVias(self.orden, [clave])
            else:
                self._insertar_recursivo(nodo.hijos[-1], clave)

    def buscar(self, clave):
        return self._buscar_recursivo(self.raiz, clave)

    def _buscar_recursivo(self, nodo, clave):
        if nodo is None:
            return False
        if clave in nodo.claves:
            return True
        for i, valor in enumerate(nodo.claves):
            if clave < valor:
                return self._buscar_recursivo(nodo.hijos[i], clave)
        return self._buscar_recursivo(nodo.hijos[-1], clave)

    # --- Recorridos ---
    def inorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        resultado = []
        if nodo:
            for i in range(len(nodo.claves)):
                if nodo.hijos[i]:
                    resultado += self.inorden(nodo.hijos[i])
                resultado.append(nodo.claves[i])
            if nodo.hijos[-1]:
                resultado += self.inorden(nodo.hijos[-1])
        return resultado
    
def main():
    arbol = ArbolMVias(3)  # Árbol ternario (M=3)
    valores = [50, 30, 70, 20, 40, 60, 80]
    for v in valores:
        arbol.insertar(v)

    print("¿Árbol vacío?:", arbol.es_vacio())
    print("Buscar 40:", arbol.buscar(40))
    print("InOrden:", arbol.inorden())

if __name__ == "__main__":
    main()
    