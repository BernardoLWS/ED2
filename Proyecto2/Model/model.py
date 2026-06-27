class model:
    def __init__(self):
        self.usuarios = {}
        self.amistades = {}

    def agregar_usuario(self, nombre):
        if nombre and nombre not in self.usuarios:
            self.usuarios[nombre] = None
            self.amistades[nombre] = []

    def agregar_amigo(self, usuario, amigo):
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
        return self.amistades[usuario]