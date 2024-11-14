class Moeda:
    def __init__(self, tipo, valor):
        self.valor = valor
        self.tipo = tipo

    def info(self):
        print(f"{self.tipo}: {self.valor}")

    def converter(self, para):
        # Implementação da lógica de conversão aqui
        # Exemplo simplificado:
        taxas = {'Dolar': {'Real': 5.0, 'Euro': 0.9},
                 'Euro': {'Real': 5.5, 'Dolar': 1.1},
                 'Real': {'Dolar': 0.2, 'Euro': 0.18}}
        return self.valor * taxas[self.tipo][para]
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

def criar_moeda():
    tipo_moeda = input("Selecione o tipo de Moeda (1-Real, 2-Dolar, 3-Euro): ")
    while tipo_moeda not in ('1', '2', '3'):
        print("Opção inválida. Por favor, selecione 1, 2 ou 3.")
        tipo_moeda = input("Selecione o tipo de Moeda (1-Real, 2-Dolar, 3-Euro): ")

    tipos = {1: 'Real', 2: 'Dolar', 3: 'Euro'}
    valor = float(input("Digite o valor da moeda: "))
    return tipos[int(tipo_moeda)], valor

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
            tipo, valor = criar_moeda()
            moeda = Moeda(tipo, valor)
            cofrinho.adicionar(moeda)
        elif opcao == '2':
            cofrinho.listar_moedas()
        elif opcao == '3':
            para = input("Converter para (Real, Dolar ou Euro): ")
            total = cofrinho.total_valor_convertido(para)
            print(f"Total em {para}: {total}")
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()