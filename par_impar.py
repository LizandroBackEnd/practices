def par_impar(n):
    if n % 2 == 0:
        return f"El numero {n} es par"
    else:
        return f"El numero {n} es impar"


while True:
    num = input("Ingresa un numero (o escribe salir para terminar el programa): ")
    if num.lower() == "salir":
        print("Saliendo del programa...")
        break
    try:
        num = int(num)
        print(par_impar(num))
    except ValueError:
        print("Error, solo puedes ingresar numeros")