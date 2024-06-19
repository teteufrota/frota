registros = [
    {"cliente_nome": "Aldino Miller Ferreira Zanella Pereira de Souza Mattos Prazeres", "caso_num": 1,
     "valor_despesa": 4425.92, "valor_receita": 3575.72},
    {"cliente_nome": "Balbina Ambrosio Lobato Filgueira Aguilar Dourado Canuto", "caso_num": 2,
     "valor_despesa": 4130.07, "valor_receita": 4356.77},
    {"cliente_nome": "Cezar Favaro Prates de Sousa Eduardao Faustino", "caso_num": 3, "valor_despesa": 4845.62,
     "valor_receita": 4550.15},
    {"cliente_nome": "Cezar Favaro Prates de Sousa Eduardao Faustino", "caso_num": 4, "valor_despesa": 3771.99,
     "valor_receita": 1484.69},
    {"cliente_nome": "Danilo Pedrosa Cinta Sanchez", "caso_num": 5, "valor_despesa": 2876.89, "valor_receita": 4903.07},
    {"cliente_nome": "Dayne Caetano Borges Lira da Gloria", "caso_num": 6, "valor_despesa": 5936.37,
     "valor_receita": 5658.56},
    {"cliente_nome": "Deysiane Farias Gon Alves Rodrigues da Silva Gurgel Figueredo", "caso_num": 7,
     "valor_despesa": 1043.61, "valor_receita": 2342.36},
    {"cliente_nome": "Dorvalino Bacelar Bispo da Conceicao Cassiano das Merces da Costa", "caso_num": 8,
     "valor_despesa": 486.11, "valor_receita": 3751.12},
    {"cliente_nome": "Edilane de Melo Romero Blanco Frazao Juliao Galvao", "caso_num": 9, "valor_despesa": 1731.55,
     "valor_receita": 4459.17},
    {"cliente_nome": "Eloa Ladeira Macedo Lourenco da Mata", "caso_num": 10, "valor_despesa": 258.49,
     "valor_receita": 195.64},
    # Adicione mais registros conforme necessário...
]


def listar_clientes_por_nome(parte_nome):
    clientes = set()
    for entrada in registros:
        if parte_nome.lower() in entrada["cliente_nome"].lower():
            clientes.add(entrada["cliente_nome"])
    print("Clientes encontrados:", clientes)


def listar_casos_por_cliente(nome_completo):
    casos = []
    for entrada in registros:
        if entrada["cliente_nome"].lower() == nome_completo.lower():
            casos.append(entrada["caso_num"])
    print("Casos do cliente", nome_completo, ":", casos)


def detalhes_de_caso(num_caso):
    for entrada in registros:
        if entrada["caso_num"] == num_caso:
            diferenca_receita_despesa = entrada["valor_receita"] - entrada["valor_despesa"]
            print(
                f"Nome do cliente: {entrada['cliente_nome']}, Receita: {entrada['valor_receita']}, Despesa: {entrada['valor_despesa']}, Receita - Despesa: {diferenca_receita_despesa}")


def total_despesa():
    total = sum(entrada["valor_despesa"] for entrada in registros)
    print("Despesa total:", total)


def total_receita():
    total = sum(entrada["valor_receita"] for entrada in registros)
    print("Receita total:", total)


def caso_com_maior_despesa():
    caso = max(registros, key=lambda x: x["valor_despesa"])
    print(
        f"Nome do cliente: {caso['cliente_nome']}, Caso: {caso['caso_num']}, Receita: {caso['valor_receita']}, Despesa: {caso['valor_despesa']}")


def caso_com_maior_receita():
    caso = max(registros, key=lambda x: x["valor_receita"])
    print(
        f"Nome do cliente: {caso['cliente_nome']}, Caso: {caso['caso_num']}, Receita: {caso['valor_receita']}, Despesa: {caso['valor_despesa']}")


def salvar_detalhes_do_cliente(nome_completo):
    with open(f"{nome_completo}.txt", "w") as arquivo:
        total_receita = 0
        total_despesa = 0
        for entrada in registros:
            if entrada["cliente_nome"].lower() == nome_completo.lower():
                arquivo.write(
                    f"Caso: {entrada['caso_num']}, Receita: {entrada['valor_receita']}, Despesa: {entrada['valor_despesa']}\n")
                total_receita += entrada["valor_receita"]
                total_despesa += entrada["valor_despesa"]
        arquivo.write(
            f"Total Receita: {total_receita}, Total Despesa: {total_despesa}, Diferença: {total_receita - total_despesa}")


def menu():
    while True:
        print("\nMenu:")
        print("a. Listar clientes por nome")
        print("b. Listar casos por cliente")
        print("c. Detalhes de um caso")
        print("d. Despesa total")
        print("e. Receita total")
        print("f. Caso com maior despesa")
        print("g. Caso com maior receita")
        print("h. Salvar detalhes do cliente")
        print("i. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == 'a':
            parte_nome = input("Digite parte do nome do cliente: ")
            listar_clientes_por_nome(parte_nome)
        elif opcao == 'b':
            nome_completo = input("Digite o nome completo do cliente: ")
            listar_casos_por_cliente(nome_completo)
        elif opcao == 'c':
            num_caso = int(input("Digite o número do caso: "))
            detalhes_de_caso(num_caso)
        elif opcao == 'd':
            total_despesa()
        elif opcao == 'e':
            total_receita()
        elif opcao == 'f':
            caso_com_maior_despesa()
        elif opcao == 'g':
            caso_com_maior_receita()
        elif opcao == 'h':
            nome_completo = input("Digite o nome completo do cliente: ")
            salvar_detalhes_do_cliente(nome_completo)
        elif opcao == 'i':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
