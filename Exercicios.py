class Exercicios:
    def __init__(self):
        # Construtor
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
        self.tabNum1 = ""
        self.tabNum2 = ""

    def somar(self):
        return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"

    def subtrair(self):
        return f"{self.num1} - {self.num2} = {self.num1 - self.num2}"

    def dividir(self):
        if(self.num2 == 0):
            return "Indivisível por zero!"
        else:
            return f"{self.num1} / {self.num2} = {self.num1 / self.num2}"

    def multiplicar(self):
        return f"{self.num1} * {self.num2} = {self.num1 * self.num2}"

    def tabuada(self):
        for i in range(0, 11, 1):
            self.tabNum1 += f"{self.num1} * {i} = {self.num1 * i}\n"
            self.tabNum2 += f"{self.num2} * {i} = {self.num2 * i}\n"
        return f"Tabuada de {self.num1}:\n{self.tabNum1}\nTabuada de {self.num2}:\n{self.tabNum2}"

    def EX1(self):
        for i in range(1, 11, 1):
            print(i)

    def EX2(self):
        for i in range(1, 21, 1):
            if i % 2 == 0:
                print(i)

    def EX3(self):
        total = 0
        for i in range(1, 101, 1):
            total += i
        print(f"{total}")

    def EX4(self):
        for i in range(1, 51, 1):
            if i % 5 == 0:
                print(i)

    def EX5(self):
        self.num1 = int(input("Informe um número: "))
        if self.num1 % 2 == 0:
            print(f"{self.num1} Par!")
        else:
            print(f"{self.num1} Impar!")

    def EX6(self):
        self.num1 = int(input("Informe um número: "))
        if self.num1 > 0:
            print(f"Positivo!")
        elif self.num1 < 0:
            print(f"Negativo!")
        else:
            print (f"Zero!")

    def EX7(self):
        num1 = int(input("Informe um número: "))
        print({num1})
        for i in range(0, 11, 1):
            print(f"{num1} x {i} = {num1 * i}")

    def EX8(self):
        num1 = int(input("Informe um número: "))
        print(f"{num1}")
        for i in range(1, num1 + 1):
            print(i)

    def EX9(self):
        num1 = int(input("Informe um número: "))
        soma = 0
        for i in range(1, num1 + 1, 1):
            soma += i
        print(f"{soma}")

    def EX10(self):
        num1 = ""
        for i in range(2, 21, 1):
            if (i == 2 or i == 3 or i == 5 or i == 7 or i == 11 or i == 13 or i == 17 or i == 19):
                num1 += f"{i} "
        return num1

    def EX11(self):
        num1 = int(input("Informe um número: "))
        if num1 % 2 != 0 and num1 % 3 != 0 and num1 % 5 != 0 and num1 % 7 != 0:
            print(f"Primo!")
        else:
            print(f"Não primo!")

    def EX12(self):
        num1 = int(input("Informe um número: "))
        fatorial = 1
        for i in range(1, num1 + 1, 1):
            fatorial *= i
        print(f"{fatorial}")

    def EX13(self):
        num1 = 1
        num2 = 1
        proximo = "1, 1, "
        for i in range(3, 11, 1):
            fib = num1 + num2
            num1 = num2
            num2 = fib
            proximo += f"{fib}, "
        return proximo
    def EX14(self):
        self.num1 = self.num3 - 2
        self.num2 = self.num3 - 1
        self.num3 = int(input("Informe um número: "))
        if self.num3 != self.num1 + self.num2:
            print(f"Fibonacci!")
        else:
            print(f"Não fibonacc!")


































































