import os
while True:
    inputUsuario = int(input('Qual ação é desejada? 1 - Git Status  2 - Git add/commit/push '))
    if inputUsuario == 1:
      os.system("cd C:\\Users\\exile\\projetos\\projetos")
      print(os.system("git status"))
    elif inputUsuario == 2:  
        os.system("cd C:\\Users\\exile\\projetos\\projetos")
        nomeArquivo = str(input('Insira o nome do arquivo/pasta desejado: '))
        commit = str(input('Insira o comentario do commit: '))

        os.system('git add '+ nomeArquivo)
        os.system('git commit -m '+ commit )
        os.system('git push')
    else:
        print('Ação inválida!')    

        