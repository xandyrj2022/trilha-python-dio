linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

# Diferente do append, extend inclui varios objetos a lista, porém não exclui duplicados
linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

linguagens.extend(["VB", "c"])

print(linguagens)  # ['python', 'js', 'c', 'java', 'csharp', 'VB', 'c']