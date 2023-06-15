from funciones import*
from Gestion_de_clientes import menuclientes
from Gestion_de_productos import menuproductos

respuesta = input("seleccione 1: ")
if respuesta == "1":
    menuclientes()

def menu_admin():
    print("          -------- [ Administrador ] --------          \n")
    print("     1. Gestion de Clientes")
    print("     2. Gestion de Productos")
    print("     3. Gestion de Ventas")
    print("     4. Gestion de Pagos")
    print("     5. Gestion de Envíos")
    opcion = input("     Ingrese el número de opción deseada: ")
    validar(opcion,"Rango",None,6)
    if opcion == "1":
        pass
    elif opcion == "2":
        pass

    
