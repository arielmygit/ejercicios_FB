def maquina_de_cambio(monedas, cantidad):
    mejor_combinacion = []
    menos_monedas = float('inf')

    for i in range(cantidad // monedas[0] + 1):
        for j in range(cantidad // monedas[1] + 1):
            for k in range(cantidad // monedas[2] + 1):
                for l in range(cantidad // monedas[3] + 1):

                    suma = i * monedas[0] + j * monedas[1] + k * monedas[2] + l * monedas[3]
                    
                    if suma == cantidad:
                        total_monedas = i + j + k + l
                        if total_monedas < menos_monedas:
                            menos_monedas = total_monedas
                            mejor_combinacion = [monedas[0]] * i + [monedas[1]] * j + [monedas[2]] * k + [monedas[3]] * l

    
    if menos_monedas == float('inf'):
        return -1, []
    return menos_monedas, mejor_combinacion

monedas = [1, 2, 5, 10]
cantidad = 67

resultado, combinacion = maquina_de_cambio(monedas, cantidad)
if resultado != -1:
    print("La cantidad mínima de monedas necesarias para regresar "+ str(cantidad)+ " pesos es: "+str(resultado))
    print("Las monedas para el cambio son: "+ str(combinacion))
else:
    print(f"No es posible formar "+str(cantidad)+" con las monedas dadas.")




