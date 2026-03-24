def agregar_producto(inventario):
    try:
        entrada_codigo = input("Ingrese el código del producto (entero): ")
        codigo = int(entrada_codigo)
        for producto in inventario:
            if producto["codigo"] == codigo:
                raise ValueError(f"El código {codigo} ya existe.")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))