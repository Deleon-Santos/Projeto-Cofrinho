class Moeda:
    def __init__(self, tipo, valor):
        self.valor = valor
        self.tipo = tipo

    def info(self):
        print(f"{self.tipo}: {self.valor}")

    def converter(self,para):
        taxas = {
            'Real': 1,          # 1 Real equivale a 1 Real
            'Dolar': 5.2,       # 1 Dólar equivale a 5.2 Reais
            'Euro': 6.18        # 1 Euro equivale a 6.18 Reais
        }
        return self.valor * taxas[self.tipo]  # Converte o valor usando a taxa correspondente


class Cofrinho:
    def __init__(self):#construtor da class cofrinho  
        self.lista_moedas=[]#o inico atributo dessa class é a lista

    def adicionar(self, moeda):#metodo adicionar
        self.lista_moedas.append(moeda)

    def remover(self,moeda):
        self.lista_moedas.remove(moeda)
    
    def listar_moedas(self):
        for moeda in self.lista_moedas:
            moeda.info()#famada da class moeda e pelo metodo info

    def total_valor_convertido(self,para):
        total = 0
        for moeda in self.lista_moedas:
            total+=moeda.converter(para)
        return total

class Dolar(Moeda):
    pass

class Euro(Moeda):
    pass

class Real(Moeda):

    pass

#Função criar moeda 
def criar_moeda():
    tipo_moeda = input("Selecione o tipo de Moeda \n1-Real\n2-Dolar\n3-Euro:\n>> ")
    while tipo_moeda not in ('1', '2', '3'): #trata os valores digitados
        print("Opção inválida. Por favor, selecione 1, 2 ou 3.")
        tipo_moeda = input("Selecione o tipo de Moeda \n1-Real\n2-Dolar\n3-Euro:\n>> ")

    tipos = {1: 'Real', 2: 'Dolar', 3: 'Euro'}# Valida o tipo de moeda sem usar os if e else
    valor = float(input("Digite o valor da moeda: "))
    return tipos[int(tipo_moeda)], valor #retorna o tipo e o valor da moeda criada

def main():
    cofrinho = Cofrinho()#instanciando o cofrinho
    while True:
        print("\nOpcoes:")
        print("1. Adicionar moeda")
        print("2. Listar moedas")
        print("3. Converter total")
        print("4. Sair")
        opcao = input("Escolha uma opcao: ")

        if opcao == '1':
            tipo, valor = criar_moeda() #abre a funciao criar e retorna o tipo e o valor
            moeda = Moeda(tipo, valor)# instanciando a class moeda
            cofrinho.adicionar(moeda)
        elif opcao == '2':
            cofrinho.listar_moedas()
        elif opcao == '3':
            para = Real
            total = cofrinho.total_valor_convertido(para)
            print(f"Total em Real: {total}")
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()