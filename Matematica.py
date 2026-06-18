class Matematica:

    def somar(self, a: float, b: float) -> float:
        return a + b

    def subtrair(self, a: float, b: float) -> float:
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        return a * b

    def dividir(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b

    def potencia(self, base: float, expoente: float) -> float:
        return base ** expoente

    def raiz_quadrada(self, numero: float) -> float:
        if numero < 0:
            raise ValueError("Não é possível calcular raiz quadrada de número negativo.")
        return numero ** 0.5

    def media(self, *numeros: float) -> float:
        if not numeros:
            raise ValueError("Informe ao menos um número.")
        return sum(numeros) / len(numeros)
