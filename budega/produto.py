class Produto():
    def __init__(self, codigo, nome, preco, qtd=0):
        self.__nome = nome
        self.__codigo = codigo
        self.__qtd = qtd
        self.__preco = preco

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome


    def getPreco(self):
        return self.__preco

    def setPreco(self, preco):
        self.__preco = preco

    def getQtd(self):
        return self.__qtd

    def setQtd(self, qtd):
        self.__qtd = qtd

    def exibir(self):
        print('Código: %d' % self.__codigo)
        print('Nome: %s' % self.__nome)
        print('Preço: R$ %2.f' % self.__preco)
        print('Qtde em estoque: %d' % self.__qtd)

    codigo = property(fget = getCodigo)
    nome = property(fget = getNome, fset = setNome)
    qtd = property(fget = getQtd, fset = setQtd)
    preco = property(fget = getPreco, fset = setPreco)
