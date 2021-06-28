sucesion = int(input('cargue un numero: '))
longitud = 1
promedio = 0
sumatoria = sucesion
array = []
while (sucesion != 1):
    if (sucesion % 2 != 0):
        sucesion = (sucesion*3) + 1
        sumatoria += sucesion
        longitud += 1
        array.append(sucesion)
    else:
        sucesion = sucesion // 2
        sumatoria += sucesion
        longitud += 1
        array.append(sucesion)
    promedio = sumatoria / longitud

print(longitud)
print(sumatoria)
print(promedio)
max = max(array)
print(max)
