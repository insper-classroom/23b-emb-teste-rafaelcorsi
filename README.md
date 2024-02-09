# AV3 - SUB

- Você possui um total de 1h20 para realizar a avaliação, você pode decidir como usar o seu tempo.
- **Trabalhar sozinho**
- **1h20 min**
- **REALIZAR UM COMMIT (A CADA QUESTÃO) E DAR PUSH AO FINALIZAR**

Pontos:

| Tipo            | pts HW | pts SW |
|-----------------|--------|--------|
| Prática         | 0      | 30     |
| Papel           | 15     | 12     |

## Teórica

Papel

## Prática

Antes de começar execute: `telemetry auth` para autenticar.

### 1. (10 SW) Pseudo

| Arquivo: `nasm/pseudo.nasm` | pts HW | pts SW |
|-----------------------------|--------|--------|
| pytest -v -k pseudo         |        | 10      |

Implemente o pseudocódigo a seguir em assembly:

```py
i = 0
while i < RAM[0]:
    RAM[2] += 1
    i += 1
return RAM[2]
```
 
### 2. (10 SW) isqrt

| Arquivo: `nasm/sqrt.nasm` | pts HW | pts SW |
|---------------------------|--------|--------|
| `pytest -k sqrt_4`        |        |        |
| `pytest -k sqrt_rand`     |        | 10     |


Escreva um programa em assembly que calcula a raiz quadrada (inteira) de um número inteiro. O valor de input do programa está na RAM[0] e o resultado deve ser salvo na RAM[0].

``` python
RAM[0] = int(sqrt(RAM[0]))
```

Para realizar o cálculo utilize o algoritmo a seguir, que faz uma busca linear e usa apenas adicão:

``` py
def isqrt(y):
    L = 0
    a = 1
    d = 3
    
    while a <= y:
        a = a + d
        d = d + 2
        L = L + 1
        
    return L
```
 
### 3. (10 SW) Vector Min

| Arquivo: `nasm/vectorMin.nasm`          | pts HW | pts SW |
|-----------------------------------------|--------|--------|
| pytest -v -k vectorMin_exemplo          |        | 0      |
| pytest -v -k vectorMin_rand (aleatório) |        | 10      |

Dado um vetor de números inteiros armazenados sequencialmente na memória `RAM`, a partir do endereço `RAM[5]`, e sabendo que o tamanho desse vetor é armazenado em `RAM[4]`, crie um programa em assembly que encontra o menor valor e salva o resultado em `RAM[0]` .

Exemplo `-k vectorMin_example`:

```
RAM[0]:  
RAM[1]:  
RAM[4]:  4   (tamanho do vetor)
RAM[5]:  2   (primeiro elemento do vetor)
RAM[6]:  7
RAM[7]:  1
RAM[8]:  3   (último elemento do vetor)
```

Resultado: `RAM[0]=1`

