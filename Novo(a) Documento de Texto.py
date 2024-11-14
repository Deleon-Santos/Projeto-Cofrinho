
class Moeda:
    def __init__(self, tipo,valor):
        self.valor=valor
        self.tipo=tipo

    def info(deslf):
        pass
    def converter(self, para):
        pass
class Cofrinho:
    def __init__(self):
        
        self.lista_moedas=[]

    def adicionar(self, moeda):
        self.lista_moedas.append(moeda)

    def remover(self,moeda):
        self.lista_moedas.remove(moeda)
    
    def listar_moedas(self):
        for moeda in self.lista_moedas:
            moeda.info()

    def total_valor_convertido(self, para):
        total = 0
        for moeda in self.lista_moedas:
            total+=moeda.converter(para)

class Dolar(Moeda):
    def info(self):
        print(f'Dolar: ${self.valor}')
    
    def converter(self, para):
        pass

class Euro(Moeda):
    def info(deslf):
        return super().info()
    
    def converter(self, para):
        return super().converter(para)
class Real(Moeda):
    def info(deslf):
        return super().info()

    def converter(self, para):
        return super().converter(para)

origem_moeda = input("Selecone o tipo de Moeda \n 1-Real 2-Dolar 3-Euro :")[0]
if origem_moeda in ('1','2','3'):
    if origem_moeda == "1":
        tipo = "Real"
    elif origem_moeda == "2":
        tipo = "Dolar"
    else:
        tipo="Euro"
else:
    print('escola uma das moeda para adicionar')

valor = float(input('coloque um valor em moeda'))
moeda = Moeda(tipo, valor)