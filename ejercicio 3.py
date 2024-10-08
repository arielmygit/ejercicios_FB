def encontrar_serie(arr, serie):
    a = len(arr)  
    s = len(serie)  
    
    for i in range(a - s + 1):
        match = True
        
        for j in range(s):
            if arr[i + j] != serie[j]:
                match = False
                break
        if match:
            return True, i  

    return False, -1  

arr1 = [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1]
serie1 = [2, 1, 0, 1]

resultado, posicion = encontrar_serie(arr1, serie1)

if resultado:
    print("La serie "+str(serie1)+" aparece en el arreglo comenzando en la posición "+str(posicion))
    print("Arreglo: "+str(arr1))
else:
    print("La serie no aparece en el arreglo.")
