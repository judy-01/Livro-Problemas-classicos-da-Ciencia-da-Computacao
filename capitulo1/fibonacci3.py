
from typing import Dict

# Dicionário de memoização, inicializado com os dois primeiros números de Fibonacci.
memorizacao: Dict[int, int] = {0: 0, 1: 1}

def fibonacci3(n: int) -> int:
    if n not in memorizacao:  # Verifica se o valor já foi calculado
        memorizacao[n] = fibonacci3(n - 1) + fibonacci3(n - 2)
    return memorizacao[n]  #  retorna o valor calculado ou memorizado

if __name__ == "__main__":
    print(fibonacci3(20))  