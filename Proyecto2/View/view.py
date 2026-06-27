import tkinter as tk

class view:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Red Social - Grafo de Amigos")
        self.root.geometry("600x600")

        # Caja texto
        frame_texto = tk.Frame(self.root)
        frame_texto.pack(fill="x", padx=10, pady=10)

        tk.Label(frame_texto, text="Nombre :").pack(side="left")
        self.entry_nombre = tk.Entry(frame_texto, width=40)
        self.entry_nombre.pack(side="left", fill="x", expand=True)

        # Botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(fill="x", padx=10, pady=10)

        self.btn_agregar_usuario = tk.Button(frame_botones, text="Agregar Usuario", bg="steelblue", fg="white")
        self.btn_agregar_usuario.pack(side="left", padx=30)

        self.btn_agregar_amigo = tk.Button(frame_botones, text="Agregar Amigo", bg="purple", fg="white")
        self.btn_agregar_amigo.pack(side="left", padx=30)

        self.btn_grafo = tk.Button(frame_botones, text="Grafo Amigos", bg="green", fg="white")
        self.btn_grafo.pack(side="left", padx=30)

        # Caja usuarios y amigos
        frame_listas = tk.Frame(self.root)
        frame_listas.pack(fill="both", expand=True, padx=10, pady=10)

        frame_usuarios = tk.Frame(frame_listas)
        frame_usuarios.pack(side="left", fill="both", expand=True, padx=5)

        tk.Label(frame_usuarios, text="USUARIOS :").pack(anchor="w")
        self.listbox_usuarios = tk.Listbox(frame_usuarios)
        self.listbox_usuarios.pack(fill="both", expand=True)

        frame_amigos = tk.Frame(frame_listas)
        frame_amigos.pack(side="left", fill="both", expand=True, padx=5)

        tk.Label(frame_amigos, text="AMIGOS :").pack(anchor="w")
        self.listbox_amigos = tk.Listbox(frame_amigos)
        self.listbox_amigos.pack(fill="both", expand=True)

    def mostrar_usuarios(self, usuarios):
        self.listbox_usuarios.delete(0, tk.END)
        for u in usuarios:
            self.listbox_usuarios.insert(tk.END, u)

    def mostrar_amigos(self, amistades):
        seleccion = self.listbox_usuarios.curselection()
        self.listbox_amigos.delete(0, tk.END)
        if seleccion:
            if amistades:
                for a in amistades:
                    self.listbox_amigos.insert(tk.END , a)
            else:
                self.listbox_amigos.insert(tk.END, "No tiene amigos registrados")
  
    def mostrar_grafo(self):
        # Crear una nueva ventana vacía
        nueva_ventana = tk.Toplevel(self.root)
        nueva_ventana.title("Grafo de Amigos")
        nueva_ventana.geometry("1200x900")

        # Por ahora solo un label para confirmar que está vacía
        tk.Label(nueva_ventana, text="Aquí se mostrará el grafo").pack(expand=True)

    def iniciar(self):
        self.root.mainloop()
