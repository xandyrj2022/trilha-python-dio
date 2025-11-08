linguagens = ["python", "js", "c", "java", "csharp"]

# sorted(função built-in) também ordena iteráveis, funciona como o sort, porém com a sintaxe de uma função

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"] 
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
