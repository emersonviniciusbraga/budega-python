
from budega.estoque import Estoque

estoque = Estoque()
menu = "===== MENU =====\n"
menu += "1 - Cadastrar produto\n"
menu += "2 - Listar produtos\n"
menu += "3 - Obter produto\n"
menu += "4 - Buscar produto\n"
menu += "5 - Atualizar estoque\n"
menu += "0 - Sair"

while True:
    print(menu)
    op = input("Opção: ")

    if op == '1':
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        cod = estoque.cadastrarProduto(nome, preco)
        print('Produto (cod = %d) cadastrado!' %cod)
        pass

    elif op == '2':
        estoque.listarProduto()

    elif op == '3':
        cod = int(input("Digite um código :"))
        p = estoque.obterProduto( cod )
        if p == None:
            print('Código Inválido!!!')
        else:
            p.exibir()

    elif op == '4':
        nome = input("Digite um nome :")     
        p = estoque.buscarProduto( nome )
        if p == None:
            print('Produto Inexistente!!!')
        else:
            p.exibir()

    elif op == '5':
        cod = int(input("Código do produto: "))
        qtde = int(input("Quantidade: "))
        ret = estoque.entradaProduto(cod, qtde)
        if ret:
            print('Estoque atualizado!')
        else:
            print('Erro ao atualizar o estoque!')
        
    
    elif op == '0':
        print('Volte sempre!')
        break
    
    else:
        print("Opção inválida!!!")
        
