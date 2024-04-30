from tienda import Farmacia, Supermercado, Restaurante
from producto import Producto

def accion(opcion_accion, tienda):
    """Realiza una acción según la opción seleccionada.

    Args:
        opcion_accion (int): La opción seleccionada.
        tienda (Tienda): La instancia de la tienda sobre la cual se realizará la acción.
    """
    if opcion_accion == 1:
        print(tienda.listar_productos())
    elif opcion_accion == 2:
        print(tienda.listar_productos())
        nombre_compra = input("Ingrese el nombre del producto que desea comprar\n")
        cantidad = int(input("Ingrese la cantidad que desea comprar\n"))
        tienda.realizar_venta(nombre_compra, cantidad)
    else:
        print("Adiós")
        exit()

def main():
    """Función principal del programa."""
    print("Bienvenido")
    nombre = input("Ingrese el nombre de la tienda\n")
    costo_delivery = int(input("Ingrese costo de delivery\n"))

    tipo_tienda = int(input('''¿Qué tipo de tienda deseas crear?
    1. Farmacia
    2. Supermercado
    3. Restaurante
    '''))

    if tipo_tienda == 1:
        tienda = Farmacia(nombre, costo_delivery)
    elif tipo_tienda == 2:
        tienda = Supermercado(nombre, costo_delivery)
    elif tipo_tienda == 3:
        tienda = Restaurante(nombre, costo_delivery)

    opcion_ingreso = 1
    print("Ingrese productos")
    while opcion_ingreso == 1:
        nombre_producto = input("Indique nombre\n")
        precio_producto = int(input("Indique precio\n"))
        
        if tipo_tienda != 3:
            stock_producto = int(input("Ingrese stock\n"))
            tienda.ingresar_producto(Producto(nombre_producto, precio_producto, stock_producto))
        else:
            tienda.ingresar_producto(Producto(nombre_producto, precio_producto))
            
        opcion_ingreso = int(input('''¿Desea agregar más productos?
        1. Si
        2. No
        '''))

    opcion_accion = int(input('''¿Qué quieres hacer?
    1. Listar productos
    2. Realizar una venta
    3. Finalizar
    '''))
    while opcion_accion in [1, 2]:
        accion(opcion_accion, tienda)
        opcion_accion = int(input('''¿Qué quieres hacer?
        1. Listar productos
        2. Realizar una venta
        3. Finalizar
        '''))

    if opcion_accion == 3:
        print("Adiós")

if __name__ == "__main__":
    main()
