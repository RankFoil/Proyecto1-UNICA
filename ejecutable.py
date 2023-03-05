from Reader import *

def main():
    opc=0
    while(opc!=5):
        Maquina.verPresupuesto()
        print('---------MENU-------')
        try:
            opc = int(input('''
1. Enlistar productos
2. Agregar producto
3. Comprar producto
4. Enlistar productos por tipo
5. Salir
'''))
        except ValueError:
            opc=0

        if opc == 1:
            Usuario.verProductos()

        elif opc == 2:
            try:
                print('Agregando producto...')
                id=int(input("Ingrese su ID (3 dígitos): "))
                newID=str(id)
                if len(str(id))>3:
                    print("No se pudo agregar el producto")
                    return
                elif len(str(id))<3:
                    newID=str(id).zfill(3)
                with open("data.csv", "r") as f:
                    reader=csv.reader(f)
                    for IDS in reader:
                        if newID==IDS[0]:
                            raise IDAlreadyExists_Exception()
                Nombre=input("Nombre del producto: ")
                Precio=int(input("Precio del producto: "))
                Cantidad=int(input("Cantidad de productos disponibles: "))
                Tipo=input("Tipo de producto: ")
                Nombre=Nombre.title()
                Tipo=Tipo.title()
                print('-----Producto agregado----\n\n')
            except ValueError:
                print("No se pudo agregar el producto")
                continue
            except IDAlreadyExists_Exception:
                continue
            new_product = Producto(newID, Nombre, Precio, Cantidad, Tipo)
            lista=[new_product.newId, new_product.nombre, new_product.precio, new_product.cantidad, new_product.tipo ]
            Producto.agregar(lista)
        
        elif opc==3:
            Usuario.comprar()
        elif opc==4:
            tipo=input("Ingrese el tipo de producto a buscar: ")
            Usuario.verTipos(tipo)
        elif opc==5:
            break

        else:
            print('Opcion no válida')

main()