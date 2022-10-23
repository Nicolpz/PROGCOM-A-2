from tkinter import *
from tkinter import ttk
class market:
	def __init__(self,a):
		self.a = a
		self.a.configure(bg='violet')
		self.productos = ("Leche (litro)-$3500","Huevos (cartón)-$15000","Pan (unidad)-$2000","Chocolate (libra)-$8000","Cafe (libra)-$5000","Arepas (unidad)-$1500","Queso (libra)-$7000","Harina (libra)-$3000","Azucar (libra)-$3500","Sal (libra)-$1500","Aceite (litro)-$16000","Mantequilla (pesa)-$2500", "Cebolla (libra)-$2000")
		self.b = IntVar()
		self.c = IntVar()
		self.total = 0
		self.d()
	def d(self):
		self.a.title("Mini Market Los Pollos Hermanos")
		self.a.geometry("650x450")
		Label(self.a,text="Producto a comprar").place(x=10,y=10)
		Label(self.a,text="Cantidad").place(x=10,y=60)
		Label(self.a,text="Total: ").place(x=470,y=400)
		self.combo = ttk.Combobox(self.a,state="")
		self.combo.place(x=10,y=35)
		self.combo["values"]=self.productos
		self.combo.current(0)
		Entry(self.a,textvariable=self.b).place(x=10,y=85)
		Entry(self.a,textvariable=self.c).place(x=520,y=400)
		Button(self.a,text="Agregar",command=self.agregarProducto).place(x=10,y=110)
		self.tabla = ttk.Treeview(self.a,columns=("Cantidad","Subtotal"))
		self.tabla.heading("#0",text="Producto")
		self.tabla.heading("Cantidad",text="Cantidad")
		self.tabla.heading("Subtotal",text="Subtotal")
		self.tabla.place(x=10,y=150)
	def agregarProducto(self):
		texto = self.combo.get()  
		datos = texto.split("-$")
		producto = datos[0]
		precio = datos[1]
		cantidad = self.b.get()
		subtotal = int(precio)*int(cantidad)
		self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(subtotal)))
		self.total = self.total + subtotal
		self.c.set("$"+str(self.total))
obj = market(Tk())
obj.a.mainloop()