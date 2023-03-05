from Reader import *

def main():
    '''Funcion encargada de mostrar un menu para realizar las opciones que se pueden ejecutar'''
    opc=0
    while(opc!=5):
        Maquina.verPresupuesto()
        print('---------MENU-------')
        try:
            opc = int(input('''
1. Enlistar productos
2. Comprar producto
3. Enlistar productos por tipo
4. Agregar producto
5. Salir
'''))
        except ValueError:
            opc=0
            tipo = ''

        if opc == 1:
            Usuario.verProductos()
            """Regresa la lista de productos que se almacenan en el archivo data.csv"""
        elif opc==2:
            Usuario.comprar()
            """Permite realizar la compra que desea el usuario"""
        elif opc==3:
            try:
                opc2=int(input("Ingrese el tipo de producto a buscar\n1. Bebida\n2. Alimento\n"))
                if opc2 == 1:
                    tipo = 'Bebida'
                elif opc2 == 2:
                    tipo = 'Alimento'
                else:
                    print('Opcion no valida')
                #tipo = tipo.title()
            except ValueError:
                pass
            Usuario.verTipos(tipo)
            """Regresa los productos de acuerdo al tipo de productos solicitado que se almacenan en el archivo data.csv"""

        elif opc == 4:
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
                try:
                    Tipostr=int(input("Tipo de producto(1. Alimento/ 2. Bebida): "))
                    if Tipostr == 2:
                        Tipo = 'Bebida'
                    elif Tipostr == 1:
                        Tipo = 'Alimento'
                    else:
                        print('Opcion no valida')
                    #tipo = tipo.title()
                except ValueError:
                    pass
                Nombre=Nombre.title()
                #Tipo=Tipo.title()
                print('-----Producto agregado----\n\n')
            except ValueError:
                print("No se pudo agregar el producto")
                continue
            except IDAlreadyExists_Exception:
                continue
            new_product = Producto(newID, Nombre, Precio, Cantidad, Tipo)
            lista=[new_product.newId, new_product.nombre, new_product.precio, new_product.cantidad, new_product.tipo ]
            Producto.agregar(lista)
            """Instancia los productos que se agregan a la máquina, los productos se almacenan en una nueva linea del archivo data.csv"""
            
        elif opc==5:
            break
        else:
            print('Opcion no válida')

main()