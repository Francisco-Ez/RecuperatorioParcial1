# Listas iniciales de productos y sus cantidades respectivas
nombres=["papas","tomates", "cebollas", "zanahorias"]
cantidades=[100, 20, 30,0]

# Variable para controlar el ciclo del menú
opcion_elegida = 0

# Bucle principal: se repite hasta que el usuario elija la opción 5 (salir)
while opcion_elegida != 6:
     # Mostrar el menú de opciones
    print("Menu de opciones: ")
    print("1.Agregar producto")
    print("2.Ver productos agotados")
    print("3.Actualizar el stock")
    print("4.Ver todos los productos")
    print("5.Consultar stock de un producto")
    print("6.Salir")
    # Variable para verificar si hay productos agotados
    agotados=False

    # Pedir al usuario que seleccione una opción
    opcion_elegida= int(input("¿Que quiere hacer?. escriba el número de la opcion correspondiente: "))
     # Opción 1: Agregar un nuevo producto al inventario
    if opcion_elegida==1:
        nombre_producto=input("Nombre del producto que quiere agregar: ")
        nombres.append(nombre_producto)
        cantidad_producto= int(input("Escriba la cantidad: "))
        cantidades.append(cantidad_producto)
     # Opción 2: Mostrar productos con stock agotado (cantidad == 0)
    elif opcion_elegida == 2:
        print(" Productos con stock agotado:")
        agotados = False
        i = 0
        while i < len(nombres):
            if cantidades[i] == 0:
                print("- " + nombres[i])
                agotados = True
            i += 1
        if not agotados:
            print("Todos los productos tienen stock.")
     # Opción 3: Actualizar el stock de un producto existente
    elif opcion_elegida == 3:
        nombre = input("Ingrese el nombre del producto a actualizar: ")
        encontrado = False
        i = 0
        while i < len(nombres):
            if nombres[i].lower() == nombre.lower():  # Comparación sin distinguir mayúsculas
                nuevo_stock = int(input("Ingrese la nueva cantidad para '" + nombres[i] + "': "))
                if nuevo_stock > 0:
                    cantidades[i] = int(nuevo_stock) # Actualiza la cantidad en la misma posición
                    print("Stock actualizado ")
                else:
                    print("Cantidad inválida.")
                encontrado = True
            i += 1
        if not encontrado:
            print(" Producto no encontrado.")
    # Opción 4: Mostrar todos los productos con sus cantidades
    elif opcion_elegida == 4:
        if len(nombres) == 0:
            print("No hay productos en el inventario.")
        else:
            print(" Lista de productos y stock:")
            i = 0
            while i < len(nombres):
                print("- " + nombres[i] + ": " + str(cantidades[i]) + " unidades")
                i += 1

     # Opciónn 5: Consultar el stock de un producto específico
    elif opcion_elegida == 5:
        consulta = input("Ingrese el nombre del producto que desea consultar: ")
        encontrado = False
        i = 0
        while i < len(nombres):
            if nombres[i].lower() == consulta.lower():
                print("El stock de '" + nombres[i] + "' es: " + str(cantidades[i]) + " unidades")
                encontrado = True
            i += 1
        if not encontrado:
            print("Producto no encontrado.")

    # Opción 6: Salir del programa
    elif opcion_elegida == 6:
        print("Saliendo del programa")
    
   # Si el usuario ingresa una opción inválida
    else:
        print("Opción no válida. Intente nuevamente.")
