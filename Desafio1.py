integer = int(input('Ingrese un número entero(seran los segundos): '))

hour = (integer // 3600)
seconds = integer - (hour * 3600)
minutes = (seconds // 60)
seconds = seconds - (minutes*60)


print('Resultado de hora: ',hour)
print('Resultado de minutos: ',minutes)
print('Resultado de segundos: ',seconds)

print(hour, ':', minutes, ':', seconds)


## Proceso inverso

setHour = int(input('Hora: '))
setMinutes =  int(input('Minutos: '))
setSeconds = int(input('Segundos: '))

hourToSeconds = setHour * 3600
minutesToSeconds = setMinutes * 60

totalSeconds = setSeconds + minutesToSeconds + hourToSeconds

print('Segundos totales: ', totalSeconds)
