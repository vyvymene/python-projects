import json
import os

arquivo = "gastos.json"

def carregar_gastos():
    if not os.path.exists(arquivo):
       return[]
    with open(arquivo, "r", encoding="utf-8") as f:
       return json.load(f)
def salvar_gastos(gastos):
   with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(gastos, f, indent=4, ensure_ascii=False)

def cadastrar_gastos():
    gastos = carregar_gastos()
    gasto = {
      "descricao": input("Informe a descrição: "),  
      "categoria": input("Informe a categoria: "),
      "quantidade": int(input("Informe a quantidade: ")),
      "valor_unitario": float(input("Informe o valor unitário: ")),
      "data": input("Informe a data: ")
    }   
    gasto["valor"] = gasto["quantidade"] * gasto["valor_unitario"]

    gastos.append(gasto)
    salvar_gastos(gastos)
    print("cadastro efetuado com sucesso!\n")

def listar_gastos():
    gastos = carregar_gastos()
    for i in gastos:
        print(f"1- descricao: {i['descricao']}")
        print(f"2- categoria: {i['categoria']}")
        print(f"3- quantidade: {i['quantidade']}")
        print(f"4- valor Unitário: {i['valor_unitario']}")
        print(f"5- valor total: {i['valor']}")
        print(f"6- data: {i['data']}")

def editar_gastos():
    gastos = carregar_gastos()
    for i, gasto in enumerate(gastos):
        print(f"{i} - {gasto['descricao']}")
    indice = int(input("Digite o número do gasto que quer editar: "))

    gastos[indice] = {
        "descricao": input("Nova descriçao: "),
        "categoria": input("Nova categoria: "),
        "quantidade": int(input("Nova quantidade: ")),
        "valor_unitario": float(input("Novo valor unitário: ")),
        "data": input("Nova data: ")
    }
    salvar_gastos(gastos)
    print("Gastos atualizados com sucesso! ")

def remover_gastos():
    gastos = carregar_gastos()
    for i, gasto in enumerate(gastos):
        print(f"{i} - {gasto['descricao']}")
    indice = int(input("Digite o número do gasto que quer remover: "))

    gastos.pop(indice)
    salvar_gastos(gastos)
    print("Gasto removido com sucesso! ")   

def total_gastos():
    gastos = carregar_gastos()
    total = sum(gasto["valor"] for gasto in gastos)
    print(f"Total gasto: R$ {total:.2f}")         


def menu():
    while True:
        print("\n --- CONTROLE DE GASTOS ---")   
        print("1 - Cadastrar gasto")   
        print("2 - Listar gastos") 
        print("3 - Editar gasto")  
        print("4 - Remover gasto") 
        print("5 - Total de gastos")
        print("0 - Sair")   

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_gastos()
        elif opcao == "2":
            listar_gastos()
        elif opcao == "3":  
            editar_gastos() 
        elif opcao == "4":
            remover_gastos()
        elif opcao == "5":
            total_gastos()    
        elif opcao == "0":
            break
        else:
            print("Opção inválida.\n")

menu()            
        

 

