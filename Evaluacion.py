def main():
    try:
        inventario = crear_inventario()
        print("Inventario inicial creado con éxito.")
    except Exception as e:
        print(f"Error fatal al iniciar: {e}")
        return

    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Ver estadísticas")
        print("4. Exportar inventario")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        match opcion:

            case '1':
                agregar_producto(inventario)
            
            case '2':
                try:
                    producto = buscar_producto(inventario)
                    if producto:
                        print(f"Producto encontrado: {producto['nombre']}")
                except KeyError as e:
                    print(e)
            
            case '3':
                try:
                    estadisticas(inventario)
                except ValueError as e:
                    print(e)
            
            case '4':
                exportado = exportar_inventario(inventario)
                if exportado:
                    print(f"Inventario exportado con {len(exportado)} registros.")
            
            case '5':
                print("Cerrando el sistema...")
                break 
            
            case _:
                print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()