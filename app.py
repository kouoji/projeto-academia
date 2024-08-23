academias = {
    "1": {"nome": "Seu auge no topo", "avaliacao": 2.5, "preco": 75, "comentarios": []},
    "2": {"nome": "Max Power", "avaliacao": 4.7, "preco": 80, "comentarios": []},
    "3": {"nome": "Green fit", "avaliacao": 4.1, "preco": 120, "comentarios": []},
    "4": {"nome": "Iron High Performance", "avaliacao": 5, "preco": 150, "comentarios": []},
    "5": {"nome": "Ferro Bruto", "avaliacao": 3.5, "preco": 95, "comentarios": []},
}


def exibir_academias():
    print("\nAcademias proximas á você:")
    for key, value in academias.items():
        print(f"  {key}. {value['nome']}")

def exibir_info_academia(opcao):
    if opcao in academias:
        academia = academias[opcao]
        print(f"\nInformações da academia {academia['nome']}:")
        print(f"  Avaliação: {academia['avaliacao']}/5")
        print(f"  Preço: R${academia['preco']}")
        if academia['comentarios']:
            print("  Comentários:")
            for i, comentario in enumerate(academia['comentarios'], 1):
                print(f"    {i}. {comentario}")
        else:
            print("  Nenhum comentário")
    else:
        print("Opção inválida")

def adicionar_comentario(opcao):
    if opcao in academias:
        comentario = input("Digite seu comentário: ")
        academias[opcao]['comentarios'].append(comentario)
        print("Comentário adicionado com sucesso!")
    else:
        print("Opção inválida")




def main():
    while True:
        print("\n" + "=" * 30)
        print("  Academias Proximas á Você")
        print("=" * 30)
        exibir_academias()
        opcao = input("Digite o número da academia: ")
        exibir_info_academia(opcao)
        print("\nOpções:")
        print("  1. Adicionar comentário")
        print("  2. Continuar")
        print("  3. Sair")
        escolha = input("Digite sua escolha: ")
        if escolha == "1":
            adicionar_comentario(opcao)
        elif escolha == "2":
            continue
        elif escolha == "3":
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()


