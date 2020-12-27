# listas 
mi_lista = []
print('mi longitud es =', len(mi_lista))

mi_lista_2 = [1,2,3,4,5]
print('mi longitud es =', len(mi_lista_2))
print(mi_lista_2)
print(mi_lista_2[0])
print(mi_lista_2[1])
print(mi_lista_2[2])
print(mi_lista_2[3])
print(mi_lista_2[4])

# indices negativos

print(mi_lista_2)
print(mi_lista_2[-1])
print(mi_lista_2[-2])
print(mi_lista_2[-3])
print(mi_lista_2[-4])
print(mi_lista_2[-5])
# conocer la ultima posicion con len
print(mi_lista_2[len(mi_lista_2)- 1])
print('\n\n ejercicio del while\n\n')

mi_longitud_1 = len(mi_lista_2)
posicion = 0 
while posicion < mi_longitud_1:
    print(mi_lista_2[posicion])
    posicion = posicion + 1     

# ejercicio 

print('\n\n ejercicio del while 2\n\n')

mi_distancia_1 = [2,4,6,10,'laura',20,18,25,'nel',89]
mi_distancia = len(mi_distancia_1)
posicion = 0
while posicion < mi_distancia:
    print (mi_distancia_1[posicion])
    posicion = posicion + 2

print('\n\n ejercicio con for\n\n')

for numero in mi_distancia_1:
    print(numero)

mi_distancia_1[5] = 'numero'
print(mi_distancia_1)
mi_distancia_1[8] = 'numero'
print(mi_distancia_1)
mi_distancia_1[2] = 'numero'
print(mi_distancia_1)
mi_distancia_1[4] = 'numero'
print(mi_distancia_1)
mi_distancia_1[3] = 'numero'
print(mi_distancia_1)
mi_distancia_1[9] = 'numero'
print(mi_distancia_1)
mi_distancia_1[0] = 'numero'
print(mi_distancia_1)
mi_distancia_1[6] = 'numero'
print(mi_distancia_1)
mi_distancia_1[1] = 'numero'
print(mi_distancia_1)
mi_distancia_1[7] = 'numero'
print(mi_distancia_1)