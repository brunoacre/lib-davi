"""
Testes simples para demonstrar o uso da classe Matematica.
Execute com: python teste.py
"""

from matematica import Matematica

calc = Matematica()

print("=== Testes da classe Matematica ===\n")

print(f"Soma:            5 + 3 = {calc.somar(5, 3)}")
print(f"Subtração:       5 - 3 = {calc.subtrair(5, 3)}")
print(f"Multiplicação:   5 × 3 = {calc.multiplicar(5, 3)}")
print(f"Divisão:         10 ÷ 4 = {calc.dividir(10, 4)}")
print(f"Potência:        2 ^ 8 = {calc.potencia(2, 8)}")
print(f"Raiz quadrada:   √144  = {calc.raiz_quadrada(144)}")
print(f"Média:           média(2, 4, 6, 8) = {calc.media(2, 4, 6, 8)}")

print("\n=== Testando erros ===\n")

try:
    calc.dividir(10, 0)
except ValueError as e:
    print(f"Divisão por zero: {e}")

try:
    calc.raiz_quadrada(-9)
except ValueError as e:
    print(f"Raiz de negativo: {e}")
