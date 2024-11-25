import textwrap

def menu():
    menu = """\n
================ MENU ================
    
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[u]\tNovo Usuário
[c]\tNova Conta
[lc]\tListar Contas
[q]\tSair

=> """
    return input(textwrap.dedent(menu))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Já existe usuário cadastrado com este cpf")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("informe o endereço (logradouro - n - bairro - cidade-UF): ")
    
    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("\nUsuário criado com Sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o número do cpf (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, verifique cpf")

def depositar(saldo, valor, extrato, total_deposito, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de \tR$ {valor:.2f}\n"
        total_deposito += valor
        print(f"\nDepósito R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\nValor informado deve ser positivo")
    
    return saldo, extrato, total_deposito

def sacar(*, saldo, valor, extrato, LIMITE_SAQUE, numero_saque, LIMITE_NUMERO_SAQUE, total_saque):     

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > LIMITE_SAQUE
    excedeu_quantidade_saque = numero_saque > LIMITE_NUMERO_SAQUE

    if excedeu_saldo:
        print(f"\nO valor R$ {valor:.2f} excede o valor total da conta R$ {saldo:.2f}")
    
    elif excedeu_limite:
        print(f"\nO valor do saque {valor:.2f} excede o limite de R$ {LIMITE_SAQUE:.2f} diário por saque")
    
    elif excedeu_quantidade_saque:
        print("\nNúmero de limite de 3 saques diários já foi atingido")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque \tR$ {valor:.2f}\n"
        numero_saque += 1
        total_saque -= valor
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!\n")

    else:
        print("O valor informado deve ser positivo")

    return saldo, extrato, total_saque

def extrato_conta(saldo, total_deposito, total_saque,/, *, extrato):
    print("=====================EXTRATO=====================\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Total depósito: \tR$ {total_deposito:.2f}")
    print(f"Total saque:    \tR$ {total_saque:.2f}")
    print(f"\nSaldo:          \tR$ {saldo:.2f}")
    print("===================================================")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta["agencia"]}
        C/C:    \t{conta["numero_conta"]}
        Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    AGENCIA = "0001"
    LIMITE_SAQUE = 500
    LIMITE_NUMERO_SAQUE = 3
    
    saldo = 1000
    extrato = ""
    numero_saque = 0
    total_deposito = 0
    total_saque = 0
    usuarios = []
    contas = []


    while True:
        
        opcao = menu()

        if opcao == "d":
            if contas == []:
                print("\nÉ necessário primeiramente criar usuário e abrir uma conta\n")
            
            else:       
                valor = float(input("Informe o valor a ser depositado: "))
                saldo, extrato, total_deposito = depositar(saldo, valor, extrato, total_deposito)
            
        elif opcao == "s":
            if contas == []:
                print("\nÉ necessário primeiramente criar usuário e abrir uma conta\n")
            
            else:       
                valor = float(input("Informe o valor a ser sacado: "))
                saldo, extrato, total_saque = sacar(
                    saldo=saldo, 
                    valor=valor, 
                    extrato=extrato, 
                    LIMITE_SAQUE=LIMITE_SAQUE,
                    numero_saque=numero_saque, 
                    LIMITE_NUMERO_SAQUE=LIMITE_NUMERO_SAQUE, 
                    total_saque=total_saque
                    )

        elif opcao == "e":
            extrato_conta(saldo, total_deposito, total_saque, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)
        
        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break
        
        else:
            print("Opção inválida, tente novamente ou entre em contato no atendimento via app")


main()