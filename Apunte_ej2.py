print("¡Bienvenido al sistema de gestión de equipos del Laboratorio Central de Investigación!")


equiposDisponibles = 25
capacidadMaxima = 20  
historialUsos = 0
opcionMenu = 0


while opcionMenu != 5:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1.- Equipos disponibles.")
    print("2.- Asignar equipo.")
    print("3.- Liberar equipo.")
    print("4.- Historial de usos.")
    print("5.- Salir.")

    
    try:
        opcionMenu = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        opcionMenu = 0

    
    match opcionMenu:
        case 1:
            print(f"Equipos disponibles actualmente: {equiposDisponibles}")

        case 2:
            if equiposDisponibles == 0:
                print("No hay equipos disponibles para asignar en este momento.")
            else:
                cantidadAsignar = 0
                while cantidadAsignar <= 0 or cantidadAsignar > equiposDisponibles:
                    try:
                        cantidadAsignar = int(input("Ingrese la cantidad de equipos a asignar: "))
                        if cantidadAsignar <= 0:
                            print("Error: La cantidad a asignar debe ser mayor a 0.")
                        elif cantidadAsignar > equiposDisponibles:
                            print(f"Error: No hay suficientes equipos disponibles (Stock actual: {equiposDisponibles}).")
                    except ValueError:
                        print("Error: Ingrese un número entero válido.")
                        cantidadAsignar = 0

                equiposDisponibles = equiposDisponibles - cantidadAsignar
                historialUsos = historialUsos + cantidadAsignar
                print(f"Se han asignado {cantidadAsignar} equipos correctamente.")

        case 3:
            if equiposDisponibles >= capacidadMaxima:
                print(f"No se pueden liberar más equipos. El laboratorio ya tiene el máximo permitido ({capacidadMaxima} equipos).")
            else:
                cantidadLiberar = 0
                while cantidadLiberar <= 0 or (equiposDisponibles + cantidadLiberar) > capacidadMaxima:
                    try:
                        cantidadLiberar = int(input("Ingrese la cantidad de equipos a liberar: "))
                        if cantidadLiberar <= 0:
                            print("Error: La cantidad a liberar debe ser mayor a 0.")
                        elif (equiposDisponibles + cantidadLiberar) > capacidadMaxima:
                            print(f"Error: No se puede superar la capacidad máxima del laboratorio ({capacidadMaxima} equipos).")
                    except ValueError:
                        print("Error: Ingrese un número entero válido.")
                        cantidadLiberar = 0

                equiposDisponibles = equiposDisponibles + cantidadLiberar
                historialUsos = historialUsos - cantidadLiberar
                print(f"Se han liberado {cantidadLiberar} equipos correctamente.")

        case 4:
            print(f"Historial de usos (equipos asignados durante la sesión): {historialUsos}")

        case 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
        case _:
            print("Opción inválida. Por favor, elija una opción del 1 al 5.")