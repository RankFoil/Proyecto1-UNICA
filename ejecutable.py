from Reader import *

def main():
    while(1):
        print('---------MENU-------')
        opc = int(input('''
1. Enlistar productos
2. Agregar producto

'''))

        if opc == 1:
            print(Producto.productos())

            producto_comprado = input('Ingresa ID de tu producto: ')
            Producto.costo(producto_comprado)
            
            
        elif opc == 2:
            Producto.agregar()

        else:
            print('Opcion no válida')

main()