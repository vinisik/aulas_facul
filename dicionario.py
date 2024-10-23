aluno = {}

for i in range(1,4):
    nome = input('Digite o nome do aluno: ')
    nota = int(input('Digite a nota: '))

    aluno[nome] = nota

for n in aluno:
    print(f'{n}: {aluno[n]}')

soma = 0
for nota in aluno.values():
    soma = soma + nota
    media = soma/len(aluno)
    media_arred = round(media, 2)

print(f'A media dos alunos foi de {media_arred}')