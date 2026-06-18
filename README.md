# matematica-modulo

Módulo Python com operações matemáticas básicas.  
Criado para demonstrar o uso de **submódulos Git**.

## Operações disponíveis

| Método | Descrição |
|---|---|
| `somar(a, b)` | Soma dois números |
| `subtrair(a, b)` | Subtrai dois números |
| `multiplicar(a, b)` | Multiplica dois números |
| `dividir(a, b)` | Divide dois números (erro se `b == 0`) |
| `potencia(base, exp)` | Calcula base elevada ao expoente |
| `raiz_quadrada(n)` | Raiz quadrada (erro se negativo) |
| `media(*nums)` | Média aritmética de N números |

## Uso básico

```python
from matematica import Matematica

calc = Matematica()

print(calc.somar(5, 3))         # 8
print(calc.dividir(10, 4))      # 2.5
print(calc.raiz_quadrada(144))  # 12.0
print(calc.media(2, 4, 6, 8))   # 5.0
```

## Estrutura

```
matematica-modulo/
├── matematica.py   # Classe principal
├── __init__.py     # Exportações do módulo
├── teste.py        # Exemplos de uso
└── README.md
```
