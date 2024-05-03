from Exercicios import Exercicios

class Control:
    def __init__(self):
        self.opcao = -1
        self.exer = Exercicios()

    def coletar(self):
        self.exer.num1 = int(input("Informe o primeiro número: "))
        self.exer.num2 = int(input("Informe o segundo número: "))

    def menu(self):
        self.opcao = int(input("-------Menu-------\n\n"+
              "\n0. Sair"             +
              "\n1. Somar"            +
              "\n2. Subtrair"         +
              "\n3. Dividir"          +
              "\n4. Multiplicar"      +
              "\n5. Tabuada"          +
              "\n6. EX1"              +
              "\n7. EX2"              +
              "\n8. EX3"              +
              "\n9. EX4"              +
              "\n10. EX5"             +
              "\n11. EX6"             +
              "\n12. EX7"             +
              "\n13. EX8"             +
              "\n14. EX9"             +
              "\n15. EX10"            +
              "\n16. EX11"            +
              "\n17. EX12"            +
              "\n18. EX13"            +
              "\n19. EX14"            +

              "\nEscolha uma das opções acima: "))

    def operacao(self):
        while(self.opcao !=0):
            self.menu() #Mostrando o menu
            if(self.opcao == 0):
                print("Obrigado!")
            elif(self.opcao == 1):
                self.coletar()
                print(self.exer.somar())
            elif(self.opcao == 2):
                self.coletar()
                print(self.exer.subtrair())
            elif (self.opcao == 3):
                self.coletar()
                print(self.exer.dividir())
            elif (self.opcao == 4):
                self.coletar()
                print(self.exer.multiplicar())
            elif (self.opcao == 5):
                self.coletar()
                print(self.exer.tabuada())
            elif (self.opcao == 6):
                print(self.exer.EX1())
            elif (self.opcao == 7):
                print(self.exer.EX2())
            elif (self.opcao == 8):
                print(self.exer.EX3())
            elif (self.opcao == 9):
                print(self.exer.EX4())
            elif (self.opcao == 10):
                print(self.exer.EX5())
            elif (self.opcao == 11):
                print(self.exer.EX6())
            elif (self.opcao == 12):
                print(self.exer.EX7())
            elif (self.opcao == 13):
                print(self.exer.EX8())
            elif (self.opcao == 14):
                print(self.exer.EX9())
            elif (self.opcao == 15):
                print(self.exer.EX10())
            elif (self.opcao == 16):
                print(self.exer.EX11())
            elif (self.opcao == 17):
                print(self.exer.EX12())
            elif (self.opcao == 18):
                print(self.exer.EX13())
            elif (self.opcao == 19):
                print(self.exer.EX14())

            else:
                print("Código escolhido não é válido!")

