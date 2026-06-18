# lib-davi - Teste Davi

Módulo Python com operações matemáticas básicas, disponível para importação direta do GitHub via `httpimport` — sem necessidade de clonar o repositório.

---

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

---

## Como usar com `httpimport`

### 1. Crie um ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instale o `httpimport`

```bash
pip install httpimport
```

### 3. Importe a classe direto do GitHub

```python
import httpimport

with httpimport.github_repo('brunoacre', 'lib-davi'):
    from Matematica import Matematica

calc = Matematica()

print(calc.somar(10, 5))         
print(calc.subtrair(10, 3))      
print(calc.multiplicar(4, 6))    
print(calc.dividir(20, 4))       
print(calc.potencia(2, 8))       
print(calc.raiz_quadrada(81))    
print(calc.media(2, 4, 6, 8))    
```

> **Atenção:** é necessário conexão com a internet, pois o módulo é carregado diretamente do GitHub a cada execução.

---

## Tratamento de erros

A classe lança `ValueError` em dois casos:

```python
# Divisão por zero
try:
    calc.dividir(10, 0)
except ValueError as e:
    print(e)  # Não é possível dividir por zero.

# Raiz quadrada de número negativo
try:
    calc.raiz_quadrada(-9)
except ValueError as e:
    print(e)  # Não é possível calcular raiz quadrada de número negativo.
```

---

## Estrutura do repositório

```
lib-davi/
├── Matematica.py   # Classe principal
├── __init__.py     # Exportações do módulo
├── teste.py        # Exemplos de uso
└── README.md
```
