# Quando queremos comparar se os valores ocupam a mesma regiao de memória usamos os operadores de identidade
# is, is not
# Retornam valores booleanos

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)
print(curso is not nome_curso)
print(saldo is limite)

