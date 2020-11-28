while True:
    preco = float(input("Digite o preço do produto, caso queira cancelar a entrada, digite um valor menor ou igual a 0: "))
    if preco > 0:
        print("Preço: R$",preco)
        pais = int(input("Insira seu pais de origem: (1 - EUA, 2 - México, 3 - Outros.) "))
        if pais == 1:
            print("País: Estados Unidos")
        elif pais == 2:
            print("País: México")
        elif pais == 3:
            print("País: Outros")
        else:
            print("País inválido.")

        transp = str(input("Digite o meio de transporte: ( T - Terrestre, F - Fluvial, A - Aéreo) "))
        transp.upper()
        if transp.upper() == "T":
            print("Meio de transporte Terrestre")

        elif transp.upper() == "F":
            print("Meio de transporte Fluvial")
        elif transp.upper() == "A":
            print("Meio de transporte Aéreo")
        else:
            print("Meio de transporte inválido")

        carg = str(input("Carga perigosa? (S - Sim, N - Não) "))
        if carg.upper() == "S":
            print("Sim")
        elif carg.upper() == "N":
            print("Não")
        else:
            print("Tipo de carga inválido")

        print(" ")
        print("//////////////////////////////////////////////////////////////")
        print(" ")

        if carg.upper() == "S" and pais == 1:
            valtransp = 50
            print("Valor de frete dos EUA com carga perigosa é de R$50.00")
        elif carg.upper() == "S" and pais == 2:
            valtransp = 21
            print("Valor de frete do México com carga perigosa é de R$24.00")
        elif carg.upper() == "S" and pais == 3:
            valtransp = 24
            print("Valor de frete de outros países com carga perigosa é de R$24.00")

        elif carg.upper() == "N" and pais == 1:
            valtransp = 12
            print("Valor de frete dos EUA com carga comum é de R$12.00")
        elif carg.upper() == "N" and pais == 2:
            valtransp = 21
            print("Valor de frete do México com carga comum é de R$21.00")
        elif carg.upper() == "N" and pais == 3:
            valtransp = 60
            print("Valor de frete de outros países com carga comum é de R$60.00")

        seg = preco / 2

        if preco <= 100:
            imp = float(preco * 0.05)
            print("O valor do imposto em cima de sua mercadoria é de: R$", imp)
        elif preco > 100:
            imp = float(preco * 0.10)
            print("O valor do imposto em cima de sua mercadoria é de: R$", imp)

        if pais == 2:
            print("O seu valor de seguro é: R$", seg)
            valfinal = str(print("O valor total de sua mercadoria é: R$", imp + preco + valtransp + seg))
        elif transp.upper() == "A":
            print("O seu valor de seguro é: R$", seg)
            valfinal = str(print("O valor total de sua mercadoria é: R$", imp + preco + valtransp + seg))
        else:
            valfinal = str(print("O valor total de sua mercadoria é: R$", imp + preco + valtransp))
        print(" ")
        print("//////////////////////////////////////////////////////////////")
        print(" ")
    else:
        print("Preço inválido ou processo finalizado pelo cliente.")

