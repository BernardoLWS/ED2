import tkinter as tk
import random
import math

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

    def mostrar_amigos(self, amistades, amigos_sugeridos=None):
        seleccion = self.listbox_usuarios.curselection()
        self.listbox_amigos.delete(0, tk.END)
        if seleccion:
            if amistades:
                self.listbox_amigos.insert(tk.END, "=== AMIGOS DIRECTOS ===")
                for a in amistades:
                    self.listbox_amigos.insert(tk.END, f"  • {a} (Grado: 1)")
                
                # Mostrar sugerencias
                if amigos_sugeridos:
                    self.listbox_amigos.insert(tk.END, "")
                    self.listbox_amigos.insert(tk.END, "=== AMIGOS SUGERIDOS ===")
                    for sugerencia in amigos_sugeridos:
                        self.listbox_amigos.insert(tk.END, f"  💡 {sugerencia} (Grado: 2)")
            else:
                self.listbox_amigos.insert(tk.END, "No tiene amigos registrados")
  
    def mostrar_grafo(self, usuarios, amistades):
        # Crear nueva ventana
        nueva_ventana = tk.Toplevel(self.root)
        nueva_ventana.title("Grafo de Amigos")
        nueva_ventana.geometry("1200x900")

        # Canvas
        canvas = tk.Canvas(nueva_ventana, width=1200, height=900, bg="white")
        canvas.pack(fill="both", expand=True)

        posiciones = {}
        ancho, alto = 1200, 900
        centro_x, centro_y = ancho / 2, alto / 2
        
        # Identificar todos los nodos
        usuarios_lista = list(usuarios)
        todas_amistades = set()
        for amigos in amistades.values():
            todas_amistades.update(amigos)
        amistades_no_usuarios = todas_amistades - set(usuarios_lista)
        todos_nodos = usuarios_lista + list(amistades_no_usuarios)
        
        # Ordenar nodos usando DFS para minimizar cruces
        def dfs_orden(nodo, visitados, orden, grafo):
            visitados.add(nodo)
            orden.append(nodo)
            for vecino in grafo.get(nodo, []):
                if vecino not in visitados:
                    dfs_orden(vecino, visitados, orden, grafo)
        
        grafo_dict = {nodo: amistades.get(nodo, []) for nodo in todos_nodos}
        visitados = set()
        orden_nodos = []
        
        for nodo in todos_nodos:
            if nodo not in visitados:
                dfs_orden(nodo, visitados, orden_nodos, grafo_dict)
        
        n = max(1, len(orden_nodos))
        r_nodo = max(16, min(28, 240 // max(1, n)))
        max_radio = min(ancho, alto) / 2 - 70

        if n <= 1:
            radio = 0
        else:
            radio_minimo = (r_nodo + 8) / math.sin(math.pi / n)
            radio = min(max_radio, max(100, radio_minimo))

        # Distribuir nodos en círculo con orden optimizado
        for i, nodo in enumerate(orden_nodos):
            angulo = (2 * math.pi * i) / n
            x = centro_x + radio * math.cos(angulo)
            y = centro_y + radio * math.sin(angulo)
            posiciones[nodo] = (x, y)

        # Dibujar aristas (amistades)
        lineas_dibujadas = set()
        for u, amigos in amistades.items():
            if u in posiciones:
                x1, y1 = posiciones[u]
                for v in amigos:
                    if v in posiciones:
                        par = tuple(sorted((u, v)))
                        if par in lineas_dibujadas:
                            continue
                        lineas_dibujadas.add(par)
                        x2, y2 = posiciones[v]
                        canvas.create_line(x1, y1, x2, y2, fill="gray", width=2, smooth=True)

        # Dibujar nodos (usuarios y amistades)
        for nodo, (x, y) in posiciones.items():
            canvas.create_oval(x-r_nodo, y-r_nodo, x+r_nodo, y+r_nodo, fill="lightblue", outline="black")
            canvas.create_text(x, y, text=nodo, font=("Arial", 12, "bold"))
    


    def iniciar(self):
        self.root.mainloop()
