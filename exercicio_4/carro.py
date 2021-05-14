class Automovel():

    def __init__(self, capacidade, combustivel, consumo):
        self.cap_dep = capacidade
        self.quant_comb = combustivel
        self.consumo = consumo

    def combustivel(self):
        return self.quant_comb

    def autonomia(self):
        return (self.quant_comb/self.consumo)

    def abastece(self, intake):
        if intake + self.quant_comb <= self.cap_dep:
            self.quant_comb += intake
            print("Abastecido")
            return(self.autonomia())
        else:
            print("Demasiado combustivel")

    def percorre(self, distance):
        if distance * self.consumo <= self.quant_comb:
            self.quant_comb -= (distance * self.consumo)
            print("Vromm vroom")
            return(self.autonomia())
        else:
            print(f"Falta gota oh chefe, este rapazola consome {self.consumo}l por km")
            return(self.autonomia())



def main():
    carro = Automovel(60, 10, 15) #default car
    while True:
        print("""
        Escreva o comando que quer executar:
        -> carro: adiciona um carro novo (Caso não crie, o programa vai usar o carro default);
        -> combustivel: devolve a quantidade de combustível no depósito;
        -> autonomia: devolve o numero de Km que é possível percorrer com o combustível no depósito;
        -> abastece: abastece o depósito;
        -> percorre:  percorre os km pedidos apos seleção;
        -> -1: para sair do programa;
        """)
        comando = input("Escreva o comando: ")
        if comando == "combustivel":
            print(f"O carro tem {carro.combustivel()} litros")

        elif comando == "autonomia":
            print(f"O carro pode andar {carro.autonomia()} km")

        elif comando == "abastece":
            subComando = int(input("Quantos litros quer meter?"))
            print(f"Autonomia: {carro.abastece(subComando)}")

        elif comando == "percorre":
            subComando = int(input("Quantos kms quer percorrer?"))
            print(f"Autonomia: {carro.percorre(subComando)}")

        elif comando == "carro":
            capacidadeCarro = int(input("Quanta capacidade tem o carro? "))
            combustivelCarro = int(input("Quanta combustivel tem o carro? "))
            autonomiaCarro = int(input("Qual é a autonomia do carro? "))
            carro = Automovel(capacidadeCarro, combustivelCarro, autonomiaCarro)
            print("Carro Criado")

        elif comando == "-1":
            print("Adeus")
            break

        elif comando != "":
            print("Comando invalido")


if __name__ == "__main__":
    main()
