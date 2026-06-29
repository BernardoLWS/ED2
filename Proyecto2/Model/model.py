class model:
    def __init__(self):
        self.usuarios = {}
        self.amistades = {}

    def agregar_usuario(self, nombre):
        if nombre and nombre not in self.usuarios:
            self.usuarios[nombre] = None
            self.amistades[nombre] = []

    def agregar_amigo(self, usuario, amigo):
        if usuario not in self.usuarios:
            self.agregar_usuario(usuario)
        if amigo not in self.usuarios:
            self.agregar_usuario(amigo)

        if usuario not in self.amistades:
            self.amistades[usuario] = []
        if amigo not in self.amistades:
            self.amistades[amigo] = []

        if amigo != usuario:
            if amigo not in self.amistades[usuario]:
                self.amistades[usuario].append(amigo)
            if usuario not in self.amistades[amigo]:
                self.amistades[amigo].append(usuario)

    def get_amigos(self, usuario):
        return self.amistades.get(usuario, [])
    
    def get_amigos_de_amigos(self, usuario):
        """Retorna amigos de amigos (sin incluir al usuario ni sus amigos directos)"""
        if usuario not in self.amistades:
            return []
        
        amigos_directos = set(self.amistades[usuario])
        amigos_de_amigos = set()
        
        for amigo in amigos_directos:
            for amigo_del_amigo in self.amistades.get(amigo, []):
                if amigo_del_amigo != usuario and amigo_del_amigo not in amigos_directos:
                    amigos_de_amigos.add(amigo_del_amigo)
        
        return list(amigos_de_amigos)
    
    def calcular_grado_separacion(self, usuario1, usuario2):
        """Calcula los grados de separación entre dos usuarios usando BFS"""
        if usuario1 not in self.usuarios or usuario2 not in self.usuarios:
            return -1
        
        if usuario1 == usuario2:
            return 0
        
        from collections import deque
        
        visitados = {usuario1}
        cola = deque([(usuario1, 0)])
        
        while cola:
            usuario_actual, distancia = cola.popleft()
            
            for amigo in self.amistades.get(usuario_actual, []):
                if amigo == usuario2:
                    return distancia + 1
                
                if amigo not in visitados:
                    visitados.add(amigo)
                    cola.append((amigo, distancia + 1))
        
        return -1  # No hay conexión