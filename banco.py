#Mensaje de bienvenida
print("Bienvenido al Banco de CETIS 50")
print("***********************************")

# Saldo inicial
saldo =1000 #saldo inicial

#Bucle del cajero automatico
while True:
    print("\nSeleccione una opcion:")
    print("1. Consultar saldo")
    print("2. Realizar deposito")
    print("3. Realizar retiro")
    print("4. salir")
    opcion = input("Ingresa el numero de la opcion deseada: ")
    
    # Consultar saldo
    if opcion == "1":
        print(f"Su saldo actual es: $[saldo]")
    
    # Realizar deposito
    elif opcion == "2":
        deposito = float(input("Ingresa el moto a depositar: "))
        saldo += deposito
        print(f"Deposito realizado. Su nuevo saldo es: $[saldo]")
        
    #Realizar retiro
    elif opcion == "3":
        retiro = float(input("Ingresa el monto a retirar: "))
        if retiro > saldo:
            print("Saldo insificiente. ")
        else:
            saldo -= retiro
        print(f"Retiro realizado. Su nuevo saldo es: $[saldo]")
    # salir
    elif opcion == "4":
        print("Gracias por usa Banco CETIS 50. !Hasta luego!")
        break
    
    # opcion invalida
    else:
        print("Opcion invalida. Intete nuevamente.")
        