linguagens = ["python", "js", "c", "java", "csharp"]
# sort ordena a lista, no caso de string em ordem alfabética
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
# ordena de trás para frente
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

# ordena de acordo com uma condição, nesse caso a qtde de caracteres
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

# combina sort(key) com sort(reverse) que reverte a ordem preestabelecida
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
