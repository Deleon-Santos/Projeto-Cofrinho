class Moeda:
    def __init__(self, tipo, valor):
        self.valor = valor
        self.tipo = tipo

    def info(self):
        print(f"{self.tipo}: {self.valor}")

    def converter(self):
        # Implementação da lógica de conversão aqui
        # Exemplo simplificado:
        taxas = {
                 'Real': {'Dolar': 5.2, 'Euro': 6.18}}
        return self.valor * taxas[self.tipo]
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
    pass

class Euro(Moeda):
    pass

class Real(Moeda):
    pass

#Função criar moeda 
def criar_moeda():
    tipo_moeda = input("Selecione o tipo de Moeda \n1-Real\n2-Dolar\n3-Euro: ")
    while tipo_moeda not in ('1', '2', '3'): #trata os valores digitados
        print("Opção inválida. Por favor, selecione 1, 2 ou 3.")
        tipo_moeda = input("Selecione o tipo de Moeda \n11-Real\n2-Dolar\n3-Euro: ")

    tipos = {1: 'Real', 2: 'Dolar', 3: 'Euro'}# Valida o tipo de moeda sem usar os if e else
    
    valor = float(input("Digite o valor da moeda: "))

    return tipos[int(tipo_moeda)], valor #retorna o tipo e o valor da moeda criada

def main():
    cofrinho = Cofrinho()

    while True:
        print("\nOpcoes:")
        print("1. Adicionar moeda")
        print("2. Listar moedas")
        print("3. Converter total")
        print("4. Sair")
        opcao = input("Escolha uma opcao: ")

        if opcao == '1':
            tipo, valor = criar_moeda() #abre a funciao criar e retorna o tipo e o valor
            moeda = Moeda(tipo, valor)
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