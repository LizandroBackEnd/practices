while True:  
    option = input("¿Los números que vas a ingresar son enteros o decimales? (e/d), si quieres salir del programa escribe 's': ")
    if option.lower() == 'e' or option.lower() == 'd':
        numbers = input("Ingresa una lista de números separados por comas: ").split(",")
        positive_numbers = []
        for n in numbers:
            n = n.strip()
            try:
                value = int(n) if option.lower() == 'e' else float(n)
                if value > 0:
                    positive_numbers.append(value)
            except ValueError:
                print(f"Valor inválido: {n}")
        print("Números positivos:", positive_numbers)
    elif option.lower() == "s":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
        
        