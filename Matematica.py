"""
Módulo de operações matemáticas básicas.
Criado para demonstrar o uso de submódulos Git.
"""


class Matematica:
    """Classe com operações matemáticas básicas."""

    def somar(self, a: float, b: float) -> float:
        """Retorna a soma de dois números."""
        return a + b

    def subtrair(self, a: float, b: float) -> float:
        """Retorna a subtração de dois números."""
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        """Retorna a multiplicação de dois números."""
        return a * b

    def dividir(self, a: float, b: float) -> float:
        """Retorna a divisão de dois números. Lança erro se dividir por zero."""
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b

    def potencia(self, base: float, expoente: float) -> float:
        """Retorna base elevada ao expoente."""
        return base ** expoente

    def raiz_quadrada(self, numero: float) -> float:
        """Retorna a raiz quadrada de um número. Lança erro para negativos."""
        if numero < 0:
            raise ValueError("Não é possível calcular raiz quadrada de número negativo.")
        return numero ** 0.5

    def media(self, *numeros: float) -> float:
        """Retorna a média aritmética de uma sequência de números."""
        if not numeros:
            raise ValueError("Informe ao menos um número.")
        return sum(numeros) / len(numeros)
