print("---Bienvenido al Instituto de Investigación Avanzada---")

cantidadCientificos = 0
while cantidadCientificos <= 0:
    try:
        cantidadCientificos = int(input("¿Cuántos científicos desea registrar?: "))
        if cantidadCientificos <= 0:
            print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")
    except ValueError:
        print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")
        cantidadCientificos = 0


contadorCientificos = 0
totalPrincipales = 0
totalAsistentes = 0


while contadorCientificos < cantidadCientificos:
    print(f"\n--- Registro del científico #{contadorCientificos + 1} ---")
    
 
    idCientifico = input("Ingrese el ID del científico (ej. SCI0000001PH): ")
    while len(idCientifico) < 12 or " " in idCientifico:
        print("¡ID inválido! Debe tener al menos 12 caracteres y no incluir espacios.")
        idCientifico = input("Ingrese el ID del científico: ")
        

    numeroPublicaciones = 0
    while numeroPublicaciones <= 0:
        try:
            numeroPublicaciones = int(input("Ingrese el número de publicaciones: "))
            if numeroPublicaciones <= 0:
                print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")
        except ValueError:
            print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")
            numeroPublicaciones = 0
            

    if numeroPublicaciones > 12:
        totalPrincipales = totalPrincipales + 1
    else:
        totalAsistentes = totalAsistentes + 1
        
    contadorCientificos = contadorCientificos + 1


print(f"\n¡El instituto cuenta con {totalPrincipales} Investigadores Principales y {totalAsistentes} Investigadores Asistentes! ¡Ciencia en marcha!")
