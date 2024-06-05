class Fruta:
    def __init__(self, nome, preco_por_kg, quantidade_em_estoque):
        self.nome = nome
        self.preco_por_kg = preco_por_kg
        self.quantidade_em_estoque = quantidade_em_estoque

    def exibir_informacoes(self):
        print(f"Nome da Fruta: {self.nome}")
        print(f"Preço por Kg: R$ {self.preco_por_kg:.2f}")
        print(f"Quantidade em Estoque: {self.quantidade_em_estoque} kg")
        print("-" * 30)

# Criando algumas instâncias da classe Fruta
fruta1 = Fruta("Maçã", 5.99, 120)
fruta2 = Fruta("Banana", 3.49, 80)
fruta3 = Fruta("Laranja", 4.25, 150)
fruta4 = Fruta("Abacaxi", 6,80, 50)
fruta5 = Fruta("Abacate", 9,50 70)

# Exibindo as informações das frutas
fruta1.exibir_informacoes()
fruta2.exibir_informacoes()
fruta3.exibir_informacoes()

