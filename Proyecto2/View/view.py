import tkinter as tk
import math

class view:
    def __init__(self):
        # Crear ventana principal
        self.root = tk.Tk()
        self.root.title("🌐 Red Social - Grafo de Amigos")
        self.root.geometry("900x700")
        
        # Definir colores
        self.COLOR_AZUL = "#1f77d2"
        self.COLOR_PURPURA = "#6c63ff"
        self.COLOR_VERDE = "#2ecc71"
        self.COLOR_NARANJA = "#f39c12"
        self.COLOR_GRIS_CLARO = "#f0f2f5"
        self.COLOR_BLANCO = "#ffffff"
        self.COLOR_TEXTO = "#2c3e50"
        
        self.root.configure(bg=self.COLOR_GRIS_CLARO)
        
        # Crear partes de la interfaz
        self._crear_header()
        self._crear_seccion_entrada()
        self._crear_botones()
        self._crear_listas()
    
    def _crear_header(self):
        """Crea el encabezado de la aplicación"""
        header = tk.Frame(self.root, bg=self.COLOR_AZUL)
        header.pack(fill="x")
        
        titulo = tk.Label(header, text="🌐 Red Social", 
                         font=("Arial", 24, "bold"), 
                         fg="white", bg=self.COLOR_AZUL)
        titulo.pack(pady=15)
        
        subtitulo = tk.Label(header, text="Gestiona tu red de amigos", 
                            font=("Arial", 10), 
                            fg="white", bg=self.COLOR_AZUL)
        subtitulo.pack()
    
    def _crear_seccion_entrada(self):
        """Crea la sección para escribir el nombre del usuario"""
        main = tk.Frame(self.root, bg=self.COLOR_GRIS_CLARO)
        main.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Marco para entrada
        entrada_frame = tk.Frame(main, bg=self.COLOR_BLANCO)
        entrada_frame.pack(fill="x", pady=(0, 15))
        
        # Etiqueta
        tk.Label(entrada_frame, 
                text="👤 Nombre del Usuario:", 
                font=("Arial", 11, "bold"),
                fg=self.COLOR_TEXTO, 
                bg=self.COLOR_BLANCO).pack(anchor="w", padx=15, pady=(12, 5))
        
        # Campo de texto
        self.entry_nombre = tk.Entry(entrada_frame, 
                                     font=("Arial", 11), 
                                     width=50)
        self.entry_nombre.pack(fill="x", padx=15, pady=(0, 12))
        
        # Guardar referencia del marco principal
        self.main_container = main
    
    def _crear_botones(self):
        """Crea los botones de acciones"""
        botones_frame = tk.Frame(self.main_container, bg=self.COLOR_GRIS_CLARO)
        botones_frame.pack(fill="x", pady=(0, 15))
        
        # Botón para agregar usuario
        self.btn_agregar_usuario = tk.Button(botones_frame, 
                                            text="➕ Agregar Usuario",
                                            bg=self.COLOR_VERDE, 
                                            fg="white",
                                            font=("Arial", 10, "bold"))
        self.btn_agregar_usuario.pack(side="left", padx=5, expand=True, fill="x")
        
        # Botón para agregar amigo
        self.btn_agregar_amigo = tk.Button(botones_frame, 
                                          text="🔗 Agregar Amigo",
                                          bg=self.COLOR_PURPURA, 
                                          fg="white",
                                          font=("Arial", 10, "bold"))
        self.btn_agregar_amigo.pack(side="left", padx=5, expand=True, fill="x")
        
        # Botón para mostrar grafo
        self.btn_grafo = tk.Button(botones_frame, 
                                  text="📊 Grafo Amigos",
                                  bg=self.COLOR_NARANJA, 
                                  fg="white",
                                  font=("Arial", 10, "bold"))
        self.btn_grafo.pack(side="left", padx=5, expand=True, fill="x")
    
    def _crear_listas(self):
        """Crea las listas de usuarios y amigos"""
        listas_frame = tk.Frame(self.main_container, bg=self.COLOR_GRIS_CLARO)
        listas_frame.pack(fill="both", expand=True)
        
        # Lista de usuarios
        self._crear_lista_usuarios(listas_frame)
        
        # Lista de amigos
        self._crear_lista_amigos(listas_frame)
    
    def _crear_lista_usuarios(self, parent):
        """Crea la lista de usuarios"""
        frame = tk.Frame(parent, bg=self.COLOR_BLANCO)
        frame.pack(side="left", fill="both", expand=True, padx=(0, 7))
        
        # Título
        tk.Label(frame, 
                text="👥 Usuarios Registrados", 
                font=("Arial", 12, "bold"),
                fg="white", 
                bg=self.COLOR_AZUL).pack(fill="x")
        
        # Lista
        self.listbox_usuarios = tk.Listbox(frame, 
                                          font=("Arial", 10),
                                          bg=self.COLOR_BLANCO,
                                          fg=self.COLOR_TEXTO)
        self.listbox_usuarios.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(frame, command=self.listbox_usuarios.yview)
        scrollbar.pack(side="right", fill="y", padx=(0, 10))
        self.listbox_usuarios.config(yscrollcommand=scrollbar.set)
    
    def _crear_lista_amigos(self, parent):
        """Crea la lista de amigos"""
        frame = tk.Frame(parent, bg=self.COLOR_BLANCO)
        frame.pack(side="right", fill="both", expand=True, padx=(7, 0))
        
        # Título
        tk.Label(frame, 
                text="💕 Amigos y Sugerencias", 
                font=("Arial", 12, "bold"),
                fg="white", 
                bg=self.COLOR_PURPURA).pack(fill="x")
        
        # Lista
        self.listbox_amigos = tk.Listbox(frame, 
                                        font=("Arial", 10),
                                        bg=self.COLOR_BLANCO,
                                        fg=self.COLOR_TEXTO)
        self.listbox_amigos.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(frame, command=self.listbox_amigos.yview)
        scrollbar.pack(side="right", fill="y", padx=(0, 10))
        self.listbox_amigos.config(yscrollcommand=scrollbar.set)


    def mostrar_usuarios(self, usuarios):
        """Muestra la lista de usuarios"""
        self.listbox_usuarios.delete(0, tk.END)
        
        if not usuarios:
            self.listbox_usuarios.insert(tk.END, "📭 No hay usuarios registrados")
        else:
            # Mostrar cada usuario con número
            for i, usuario in enumerate(usuarios, 1):
                self.listbox_usuarios.insert(tk.END, f"  {i}. 👤 {usuario}")

    def mostrar_amigos(self, amistades, amigos_sugeridos=None):
        """Muestra los amigos del usuario seleccionado"""
        # Obtener usuario seleccionado
        seleccion = self.listbox_usuarios.curselection()
        
        # Limpiar lista
        self.listbox_amigos.delete(0, tk.END)
        
        if not seleccion:
            # No hay usuario seleccionado
            self.listbox_amigos.insert(tk.END, "👈 Selecciona un usuario primero")
            return
        
        if not amistades:
            # Usuario sin amigos
            self.listbox_amigos.insert(tk.END, "📭 Sin amigos registrados")
            return
        
        # Mostrar amigos directos
        self.listbox_amigos.insert(tk.END, "━━━━━ AMIGOS DIRECTOS ━━━━━")
        for amigo in amistades:
            self.listbox_amigos.insert(tk.END, f"  ✓ {amigo} (Grado: 1)")
        
        # Mostrar amigos sugeridos
        if amigos_sugeridos:
            self.listbox_amigos.insert(tk.END, "")
            self.listbox_amigos.insert(tk.END, "━━━ AMIGOS SUGERIDOS ━━━")
            for sugerencia in amigos_sugeridos:
                self.listbox_amigos.insert(tk.END, f"  💡 {sugerencia} (Grado: 2)")
  
    def mostrar_grafo(self, usuarios, amistades):
        """Muestra la visualización del grafo de amigos"""
        # Crear ventana
        ventana = tk.Toplevel(self.root)
        ventana.title("📊 Grafo de Amigos")
        ventana.geometry("1200x900")
        ventana.configure(bg=self.COLOR_GRIS_CLARO)
        
        # Header
        header = tk.Frame(ventana, bg=self.COLOR_NARANJA)
        header.pack(fill="x")
        tk.Label(header, 
                text="📊 Visualización del Grafo de Amigos",
                font=("Arial", 14, "bold"), 
                fg="white", 
                bg=self.COLOR_NARANJA).pack(pady=10)
        
        # Canvas para dibujar
        canvas = tk.Canvas(ventana, 
                          width=1200, 
                          height=850,
                          bg="white")
        canvas.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Calcular posiciones
        posiciones = self._calcular_posiciones(usuarios, amistades)
        
        # Dibujar
        self._dibujar_conexiones(canvas, posiciones, amistades)
        self._dibujar_nodos(canvas, posiciones, usuarios)
        self._dibujar_leyenda(canvas, usuarios)
    
    def _calcular_posiciones(self, usuarios, amistades):
        """Calcula la posición de cada usuario en el grafo"""
        usuarios_lista = list(usuarios)
        
        # Obtener todos los nodos
        todas_amistades = set()
        for amigos in amistades.values():
            todas_amistades.update(amigos)
        
        amigos_no_registrados = todas_amistades - set(usuarios_lista)
        todos_nodos = usuarios_lista + list(amigos_no_registrados)
        
        # Variables para colocar los nodos
        ancho, alto = 1200, 850
        centro_x, centro_y = ancho / 2, alto / 2
        n_nodos = len(todos_nodos)
        
        if n_nodos == 0:
            return {}
        
        # Radio del círculo (más pequeño para acercar los nodos)
        radio = 120
        
        # Colocar cada nodo en un círculo
        posiciones = {}
        for i, nodo in enumerate(todos_nodos):
            angulo = (2 * math.pi * i) / n_nodos
            x = centro_x + radio * math.cos(angulo)
            y = centro_y + radio * math.sin(angulo)
            posiciones[nodo] = (x, y)
        
        return posiciones
    
    def _dibujar_conexiones(self, canvas, posiciones, amistades):
        """Dibuja las líneas de amistad en el canvas"""
        lineas_dibujadas = set()
        
        for usuario, amigos in amistades.items():
            if usuario not in posiciones:
                continue
            
            x1, y1 = posiciones[usuario]
            
            for amigo in amigos:
                if amigo not in posiciones:
                    continue
                
                # Evitar dibujar líneas duplicadas
                par = tuple(sorted((usuario, amigo)))
                if par in lineas_dibujadas:
                    continue
                
                lineas_dibujadas.add(par)
                
                # Dibujar línea
                x2, y2 = posiciones[amigo]
                canvas.create_line(x1, y1, x2, y2, 
                                  fill="#1f77d2", 
                                  width=2.5)
    
    def _dibujar_nodos(self, canvas, posiciones, usuarios):
        """Dibuja los nodos (círculos con nombres) en el canvas"""
        radio_nodo = 25
        usuarios_lista = list(usuarios)
        
        for nodo, (x, y) in posiciones.items():
            # Determinar color
            if nodo in usuarios_lista:
                color = self.COLOR_AZUL  # Usuarios registrados
            else:
                color = self.COLOR_PURPURA  # Amigos referidos
            
            # Dibujar sombra
            canvas.create_oval(x-radio_nodo-2, y-radio_nodo-2,
                              x+radio_nodo+2, y+radio_nodo+2,
                              fill="#ddd", outline="")
            
            # Dibujar nodo
            canvas.create_oval(x-radio_nodo, y-radio_nodo,
                              x+radio_nodo, y+radio_nodo,
                              fill=color, 
                              outline="white", 
                              width=2)
            
            # Dibujar nombre
            canvas.create_text(x, y, 
                              text=nodo,
                              font=("Arial", 9, "bold"),
                              fill="white")
    
    def _dibujar_leyenda(self, canvas, usuarios):
        """Dibuja la leyenda del grafo"""
        usuarios_lista = list(usuarios)
        
        # Leyenda de usuarios registrados
        x1 = 100
        y1 = 800
        radio = 15
        
        canvas.create_oval(x1-radio, y1-radio,
                          x1+radio, y1+radio,
                          fill=self.COLOR_AZUL,
                          outline="white", width=1)
        canvas.create_text(x1+50, y1,
                          text="👤 Usuarios Registrados",
                          font=("Arial", 9),
                          fill=self.COLOR_TEXTO, anchor="w")
        
        # Leyenda de amigos referidos
        x2 = 450
        canvas.create_oval(x2-radio, y1-radio,
                          x2+radio, y1+radio,
                          fill=self.COLOR_PURPURA,
                          outline="white", width=1)
        canvas.create_text(x2+50, y1,
                          text="💡 Amigos Referidos",
                          font=("Arial", 9),
                          fill=self.COLOR_TEXTO, anchor="w")
    
    def iniciar(self):
        """Inicia la aplicación"""
        self.root.mainloop()
