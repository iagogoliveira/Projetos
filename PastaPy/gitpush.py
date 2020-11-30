import os

nomeArquivo = str(input('Insira o nome do arquivo/pasta desejado: '))
commit = str(input('Insira o comentario do commit: '))
path = 'cd projetos/projetos'

os.system(path)

os.system('git add '+ nomeArquivo)
os.system('git commit -m ' + commit)
os.system('git push')