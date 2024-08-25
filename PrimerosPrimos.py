print('Esto es un archivo de prueba, ya se encuentra en GitHub')
print('En la rama main se trabaja en conseguir los primeros n primos')
print('Se van a buscar los primeros n primos')

cantidad_primos = int(input('Por favor ingresar cuáles son los primeros primos que desea >> '))

ciclos = 1 # Cantidad de veces que el ciclo while ha hecho iteraciones
primos = [] # Lista donde se van a guardar los primos

def comprobar_primo(primo):
    rango = range(2, primo + 1)
    numeros = list(filter(lambda numero : primo % numero == 0 , rango))
    if len(numeros) == 1:
        return True
    else:
        return False

while len(primos) < cantidad_primos:
    if comprobar_primo(ciclos + 1):
        primos.append(ciclos + 1)
    ciclos += 1

print('Los primeros n primos son :')
puesto = 1 # Variable para asignar un puesto a los primos conseguidos
for numero in primos:
    print(f'{puesto}. {numero}')
    puesto += 1
