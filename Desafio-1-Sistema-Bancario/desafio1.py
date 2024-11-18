menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 4000
LIMITE_SAQUE = 500
extrato = ""
LIMITE_NUMERO_SAQUE = 3
numero_saque = 0
total_deposito = 0
total_saque = 0


while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
   
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
            total_deposito += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!/n")
    
        else:
            print("Valor informado deve ser positivo")
    
    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > LIMITE_SAQUE

        excedeu_quantidade_saque = numero_saque >= LIMITE_NUMERO_SAQUE

        if excedeu_saldo:
            print(f"O valor R$ {valor:.2f} excede o valor total da conta R$ {saldo:.2f}")
        
        
        elif excedeu_limite:
            print(f"O valor do saque {valor:.2f} excede o limite de R$ {LIMITE_SAQUE:.2f} diário por saque")
        
        elif excedeu_quantidade_saque:
            print("Número de limite de 3 saques diários já foi atingido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saque += 1
            total_saque -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!/n")

        else:
            print("O valor informado deve ser positivo")

    elif opcao == "e":
        print("=====================EXTRATO=====================\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Total de depósito: R$ {total_deposito:.2f}")
        print(f"Total de saque: R$ {total_saque:.2f}")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================================")
    
    elif opcao == "q":
        break
    
    else:
        print("Opção inválida, tente novamente ou entre em contato no atendimento via app")