from budega.produto import Produto

class Estoque():
    def __init__(self):
        self.__produtos = {}
        self.__contador = 1

    def cadastrarProduto(self, nome, preco):
        p = Produto(self.__contador, nome, preco) 
        self.__produtos[self.__contador] = p
        self.__contador += 1
        return p.codigo


    def listarProduto(self):
        print("===== Produtos =====\n")
        for p in self.__produtos.values():
            print('%d\t%s\t%.2f' % (p.codigo, p.nome, p.preco))
    
    def excluirProduto(self, codigo):
        pass

    def obterProduto(self, codigo):
        if codigo in self.__produtos.keys():
            return self.__produtos[ codigo ]
        return None
    

    def buscarProduto(self, nome):
        for p in self.__produtos.values():
            if p.nome == nome:
                return p
        return None

    def atualizaProduto(self, codigo, valor):
        pass

    def entradaProduto(self, codigo, qtd):
        p = self.obterProduto( codigo )
        if p == None:
            return False
        else:
            p.setQtd( p.getQtd() + qtd)

            return True

    def saidaProduto(self, codigo, qtd):
        p = self.obterProduto( codigo )
        if p == None:
            return False
        else:
            p.setQtd( p.getQtd() - qtd)

            return True
