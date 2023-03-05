from Reader import *

def main():
    while(1):
        print('---------MENU-------')
        opc = int(input('''
1. Enlistar productos
2. Agregar producto

'''))

        if opc == 1:
            pass
            #Usuario.verProductos()

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
                
                Nombre=input("Nombre del producto: ")
                Precio=int(input("Precio del producto: "))
                Cantidad=int(input("Cantidad de productos disponibles: "))
                Tipo=input("Tipo de producto: ")
                Nombre=Nombre.title()
                Tipo=Tipo.title()
                print('-----Producto agregado----\n\n')
            except ValueError:
                print("No se pudo agregar el producto")
                return
            new_product = Producto(newID, Nombre, Precio, Cantidad, Tipo)
            lista=[new_product.newId, new_product.nombre, new_product.precio, new_product.cantidad, new_product.tipo ]
            Producto.agregar(lista)

        else:
            print('Opcion no válida')

main()