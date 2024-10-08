import math
arr=[-105,3,5,-2,9,-7,4,8,6]
#arr=[-9,-80,5,-2,9,-7,4,90,6]
mayor = 0
num1 = 0


for x in (arr):
    for i in (arr):
        temp = mayor
        mayor = i*x
        
        temp1 = num1
        num1 = x
        
        if temp > mayor:
            mayor = temp
            
            num1 = temp1
            
print("El resultado mayor de las combinaciones es: "
      +str(num1)+" x "+str(num1)+" = "+str(mayor))

        
