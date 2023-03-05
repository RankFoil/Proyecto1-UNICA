from Reader import *

def main():
    while(1):
        print('---------MENU-------')
        opc = int(input('''
1. Enlistar productos
2. Agregar producto

'''))

        if opc == 1:
            Usuario.verProductos()
        elif opc == 2:
            Producto.agregar()

        else:
            print('Opcion no válida')

main()