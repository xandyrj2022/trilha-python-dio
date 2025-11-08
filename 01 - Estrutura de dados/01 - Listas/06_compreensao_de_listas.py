# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
# pares =[]

# for numero in numeros:
#     if numero % 2 == 0:
#         pares.append(numero)

# Forma simplificada - a 1ª e 2ª parte são obrigatórios
# pares = [(numero)-1º retorno (for numero in numeros)-2º iteração (if numero % 2 == 0)-3º condição filtro]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
# quadrado =[]


# for numero in numeros:
#     quadrado.append(numero ** 2)

# Ou a forma simplificada abaixo

quadrado = [numero**2 for numero in numeros]
print(quadrado)
