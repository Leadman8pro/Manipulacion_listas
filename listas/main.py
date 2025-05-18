#Joel H. Maisonet Ayala
#Comp315 C4
#Pro. Hector Concepción
#29 de mayo de 2025

"""
Esta tarea esta hecha para poner en práctica
los conocimientos y habilidades con las listas
y a la vez reforzar los conocimientos básicos

"""

#Le pido al usuario que me ingrese los numeros que desea por separado en espacios
entrada = input("Ingresa una serie de números separados por espacios: ")

#Convierto los datos en una lista, lo pongo entero y para separar los numeros
numeros = list(map(int, entrada.split()))


#Creo las variables para sumer, numero máx, mín, conteo de numeros, elimino duplicados y ordeno
sumar = lambda lista: sum(lista)
mayor = lambda num_mayor: max(num_mayor)
menor = lambda num_menor: min(num_menor)
nume = len(numeros)
duplicado = set(numeros)
ordenar = lambda orden: sorted(orden)


        
#Lo convierto en datos para poder manejar
numero_menor = menor(numeros)
numero_mayor = mayor(numeros)
result = sumar(numeros)
promedio = result / nume
orden_num = ordenar(numeros)

#Imprimo en pantalla
print("Lista original", numeros)
print("Suma de todos los números ", result)
print("Valor máximo: ", numero_mayor)
print("Valor mínimo: ", numero_menor)
print(f"Promedio: {promedio:.3}")
print("Lista sin duplicados: ", duplicado)
print(f"Lista ordenada: {orden_num}")

#Tuve que hacerlo aparte  para los números pares. 
print("Números pares:", end=" ")
for i in numeros:
    if i % 2 == 0:
        print(i, end=" ")

#Fin del código