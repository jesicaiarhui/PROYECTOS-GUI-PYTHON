

import tkinter as tk
#CONTADOR ASCENDENTE
class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CONTADOR")
        self.root.resizable(False, False)  # Evita que la ventana sea redimensionable

        self.contador = 0

        self.etiqueta = tk.Label(root, text="CONTADOR")
        self.etiqueta.pack()

        self.valor_contador = tk.StringVar()
        self.valor_contador.set(str(self.contador))
        self.lineEdit = tk.Entry(root, textvariable=self.valor_contador, state="readonly")
        self.lineEdit.pack(side=tk.LEFT, padx=10, expand=False)
        

        self.boton_mas = tk.Button(root, text="+", command=self.incrementar_contador)
        self.boton_mas.pack(side=tk.LEFT, expand=False)

    def incrementar_contador(self):
        self.contador += 1
        self.valor_contador.set(str(self.contador))

root = tk.Tk()
root.geometry("180x150") #redimensionar
app = ContadorApp(root)
root.mainloop()
