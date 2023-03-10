import csv
import curses

class Producto:
    def __init__(self: object, newId: int, nombre: str , precio: int, cantidad: int, tipo: str) -> object:
        """Definición del método constructor para le creación de objetos (productos)"""
        self.newId = newId
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.tipo = tipo
    @staticmethod
    def cantidad(producto:str,data:list)->None:
        """Determina el producto que se entrega y reduce su cantidad disponible en 1"""
        with open("data.csv","w",newline="") as f:
            producto[3]=int(producto[3])-1
            w=csv.writer(f)
            for line, row in enumerate(data):
                w.writerow(row)
            print(producto[1]+ " Entregado")
    @staticmethod
    def productos()->list:
        """Retorna una lista con los productos disponibles"""
        lista=[]
        with open("data.csv", "r") as f:
            reader=csv.reader(f)
            lista.extend(reader)
            return lista
    @staticmethod
    def costo(ID:str)->str:
        """Retorna el precio de un producto dado su código (ID)"""
        with open("data.csv","r") as f:
            reader=csv.reader(f)
            for producto in reader:
                if producto[0]==ID:
                    return producto[2]
    @staticmethod
    def agregar(lista)->None:
        """Agrega un producto al archivo data.csv"""
        with open("data.csv","a",newline="") as f:
            w=csv.writer(f)
            w.writerow(lista)
        
class Maquina:
    @staticmethod
    def darProducto(producto:str,dinero:int)->None:
        """Le entrega el producto al usuario tras haber hecho las validaciones pertinentes,
            aumenta el presupuesto de la máquina en base al precio del producto vendido"""
        lista=Producto.productos()
        for i in lista:
            if producto in i:
                if Maquina.evaluarDinero(dinero,producto):
                    if int(i[3])>0:
                        Producto.cantidad(i,lista)
                        with open("dinero.txt", "r") as f:
                            presupuesto=f.readline()
                        cambio=Maquina.calcularCambio(dinero,producto)
                        with open("dinero.txt", "w") as f:
                            presupuesto=int(presupuesto)+dinero-abs(cambio)
                            f.write(str(presupuesto))
                        print("$"+str(abs(cambio))+" regresados")
                    else:
                        print("No hay "+ i[1]+ " disponible(s) *Le regresa sus "+str(dinero)+" pesitos*")
                else:
                    return
                        
    @staticmethod
    def readID()->str:
        """Se encarga de validar que la ID tenga un formato válido, retorna una ID válida"""
        while (True):
            try:
                id=''
                stdscr = curses.initscr()
                stdscr.clear() 
                stdscr.addstr("Ingrese el código del producto: ") 
                for j in range(3):
                    id+=stdscr.getkey()
            except: 
                raise 
            finally: 
                curses.endwin()
            lista=Producto.productos()
            for i in lista:
                if id in i:
                    return id
                else:
                    id.format()
    @staticmethod
    def calcularCambio(dinero:int,ID:str)->int:
        """Calcula el cambio que se dará, de no haber fondos suficientes, regresará el presupuesto disponible"""
        with open("dinero.txt","r") as f:
            presupuesto=f.readline()
        costo=Producto.costo(ID)
        cambio=int(costo)-int(dinero)
        if cambio==0:
            return 0
        elif cambio<0:
            return int(cambio)
    @staticmethod
    def evaluarDinero(dinero:int,ID:str)->bool:
        """Revisa que el dinero ingresado sea suficiente para adquirir un producto"""
        if dinero>=int(Producto.costo(ID)):
            return True
        else:
            print("Fondos insuficientes *Le regresa sus "+str(dinero)+ " pesitos*" )
            return False
            

class Usuario:
    @staticmethod
    def comprar()->None:
        """Le permite al usuario adquirir un producto"""
        flag=True
        while(flag):
            try:
                dinero=int(input("Ingrese su dinero (int): "))
            except ValueError:
                continue
            if dinero>0:
                flag=False
        id=Maquina.readID()
        Maquina.darProducto(id,dinero)
    @staticmethod
    def verProductos()->None:
        """Imprime en la terminal los productos de la máquina"""
        lista=Producto.productos()
        for producto in lista:
            print(producto[0]+" "+producto[1]+" ("+producto[4]+")"+" Precio: $"+producto[2]+" "+producto[3]+" diponible(s)")
    @staticmethod
    def verTipos(tipo:str)->None:
        """Imprime en la terminal los productos que coincidan con el tipo dado"""
        lista=Producto.productos()
        for producto in lista:
            if producto[4]==tipo:
                print("ID: "+producto[0]+" "+producto[1]+" ("+producto[4]+")"+" Precio: $"+producto[2]+" "+producto[3]+" diponible(s)")

class IDAlreadyExists_Exception(Exception):
    def __init__(self) -> None:
        """Excepción que se lanza en caso de que se intente agregar una ID ya existente"""
        print("La ID ya existe")