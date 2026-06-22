import tkinter as tk
import random, math

#   Inicio de ventana
root = tk.Tk()  # inicia
root.title("Red Social - Grafo de Amigos")      # titulo de la ventana
root.geometry("550x600")    # tamaño de la ventana

usuarios = {}
amistades = {}

# caja texto
label_nombre = tk.Label(root,text="Nombre :")
label_nombre.place(x=50,y=40)
entry_nombre = tk.Entry(root, width=40)     
entry_nombre.place(x=150,y=40)

# caja usuario 
label_usuarios = tk.Label(root, text=" USUARIOS :")
label_usuarios.place(x=50,y=130)
listbox_usuarios = tk.Listbox(root, width=30, height=20)
listbox_usuarios.place(x=50,y=150)

# caja amigos
label_usuarios_amigos = tk.Label(root, text=" AMIGOS :")
label_usuarios_amigos.place(x=320,y=130)
listbox_usuarios_amigos = tk.Listbox(root, width=30, height=20)
listbox_usuarios_amigos.place(x=320,y=150)

# Función para agregar usuario
def agregar_usuario():
    nombre = entry_nombre.get().strip()
    if nombre not in usuarios:
        listbox_usuarios.insert(tk.END, nombre)
        entry_nombre.delete(0, tk.END)

        # Posición aleatoria sin colisiones
        """while True:
            x = random.randint(100, 800)
            y = random.randint(100, 500)
            valido = True
            for pos in usuarios.values():
                dx, dy = x - pos[0], y - pos[1]
                if math.sqrt(dx*dx + dy*dy) < 80:
                    valido = False
                    break
            if valido:
                usuarios[nombre] = (x, y)
                break"""
    

def agregar_amigo():
    seleccion = listbox_usuarios.curselection()
    if seleccion:
        usuario = listbox_usuarios.get(seleccion[0])
   
        amigo = entry_nombre.get().strip()

        # Verificar que el amigo exista en usuarios y no sea el mismo
        if amigo:
            if amigo not in amistades[usuario]:
                amistades[usuario].append(amigo)
            if usuario not in amistades[amigo]:
                amistades[amigo].append(usuario)

        entry_nombre.delete(0, tk.END)
        
# Función para agregar amistad
def mostrar_amigos(event=None):
    seleccion = listbox_usuarios.curselection()
    if seleccion:
        usuario = listbox_usuarios.get(seleccion[0])
        amigos = amistades.get(usuario, [])

        # Limpiar el Listbox de amigos antes de mostrar
        listbox_usuarios_amigos.delete(0, tk.END)

        if amigos:
            for amigo in amigos:
                listbox_usuarios_amigos.insert(tk.END,"hola")
        else:
            listbox_usuarios_amigos.insert(tk.END,usuario)
           # listbox_usuarios_amigos.insert(tk.END, "no tiene amigos registrados")
        

# Función para dibujar grafo
def dibujar_grafo():
    ventana_grafo = tk.Toplevel(root)
    ventana_grafo.title("Visualización del Grafo")
    canvas = tk.Canvas(ventana_grafo, width=900, height=600, bg="white")
    canvas.pack()

    # Dibujar aristas
    for u, amigos in amistades.items():
        x1, y1 = usuarios[u]
        for v in amigos:
            x2, y2 = usuarios[v]
            canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

    # Dibujar nodos
    for nombre, (x, y) in usuarios.items():
        canvas.create_oval(x-30, y-30, x+30, y+30, fill="orange")
        canvas.create_text(x, y, text=nombre, font=("Arial", 12))

# Botones
btn_agregar_usuarios = tk.Button(root, text="Agregar Usuario", bg="steelblue", fg="white", command=agregar_usuario)
btn_agregar_usuarios.place(x=100,y=80)

btn_agregar_amigos = tk.Button(root, text="Agregar Amigo", bg="purple", fg="white", command=agregar_amigo)
btn_agregar_amigos.place(x=230,y=80)

"""btn_grafo = tk.Button(root, text="Mostrar Grafo", bg="green", fg="white", command=dibujar_grafo)
btn_grafo.place(x=350,y=80)"""

# Evento al seleccionar usuario
listbox_usuarios.bind("<<ListboxSelect>>", mostrar_amigos)

root.mainloop()