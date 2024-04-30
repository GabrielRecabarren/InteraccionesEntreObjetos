# Desafío - Interacciones entre objetos

En este desafío validaremos nuestros conocimientos de abstracción y encapsulamiento,
colaboración y composición.

El siguiente proyecto responde al desafío de implementar una aplicación de consola en Python que simule el backend de una aplicación móvil de compra y reparto de productos. Se ha utilizado el paradigma orientado a objetos para diseñar e implementar la arquitectura de clases, centrándose principalmente en la entidad principal "Tienda". A continuación, se detallan las características y el funcionamiento de la solución propuesta.

## Descripción

La aplicación de consola implementa tres tipos de tienda: Restaurante, Supermercado y Farmacia. Cada tienda puede ingresar productos, listar los productos existentes y realizar ventas. Al momento de crear una nueva tienda, se solicita el nombre y el costo de delivery, y se crean inicialmente sin productos. No se pueden modificar el nombre ni el costo de delivery de una tienda existente, pero sí se pueden modificar los productos a través del ingreso de nuevos productos o la realización de ventas.

Los productos tienen un nombre, un precio y un stock. Al crear un producto nuevo, se solicitan los tres valores, pero si no se especifica el stock, se asume que es 0. No se puede modificar el nombre ni el precio de un producto, solo su stock. Si se intenta modificar el stock por un valor menor a 0, se asigna 0 en su lugar.

Respecto al comportamiento de cada tipo de tienda:

- En el caso de las tiendas de tipo "Restaurante", los productos siempre tienen un stock igual a 0, ya que se fabrican al momento de realizar una venta. Por lo tanto, no es necesario modificar el stock si se añade nuevamente el mismo producto a la lista.
- Al listar los productos existentes, se oculta el stock en las tiendas de tipo Restaurante y Farmacia. En las tiendas de tipo Supermercado, se agrega el mensaje "Pocos productos disponibles" junto a la cantidad de stock si este es inferior a 10. En las tiendas de tipo Farmacia, se agrega el mensaje "Envío gratis al solicitar este producto" junto al precio de los productos con un valor superior a $15.000.
- Para realizar una venta, se solicita el nombre del producto y la cantidad requerida. En las tiendas de tipo Farmacia y Supermercado, se verifica si hay stock disponible para el producto solicitado. En el caso de las tiendas de tipo Farmacia, no se puede solicitar una cantidad superior a 3 por producto en cada venta, y si la cantidad requerida es superior a la existente, solo se venderá la cantidad disponible.

## Requerimientos

1. **producto.py**: Archivo que contiene la definición de la clase Producto, la cual permite instanciar productos. Se ha implementado utilizando encapsulamiento para garantizar la integridad de los datos de cada producto.

2. **tienda.py**: Archivo que contiene la definición de las clases necesarias para instanciar los distintos tipos de tienda. Cada clase de tienda tiene un método constructor, un método para ingresar un producto (utilizando composición ), un método para listar productos y un método para realizar ventas (utilizando colaboración). Se ha aplicado abstracción y encapsulamiento para asegurar un diseño modular y flexible.

3. **programa.py**: Archivo que implementa la lógica necesaria para crear una tienda e ingresar sus productos a través de la consola. Se solicita ingresar productos hasta que el usuario indique lo contrario. Luego, se ofrecen opciones al usuario para listar los productos existentes, realizar una venta o salir del programa. Se realizan llamadas a los métodos correspondientes de la instancia de la tienda para cada opción seleccionada.

## Uso

1. Clonar el repositorio:

```
git clone https://github.com/GabrielRecabarren/interacciones-entre-objetos.git
```

2. Navegar al directorio del proyecto:

```
cd interacciones-entre-objetos
```

3. Ejecutar el programa principal:

```
python programa.py
```

4. Seguir las instrucciones en la consola para interactuar con la aplicación.

## Autor

[Gabriel Recabarren](https://github.com/GabrielRecabarren)