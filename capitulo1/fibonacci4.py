from functools import lru_cache


@lru_cache(maxsize=None) 
def fibonacci4(n:int) -> int:
    if n < 2 :
        return n
    return fibonacci4(n -2) + fibonacci4(n - 1)
if __name__== "__main__":
    print(fibonacci4(55))

''' A propriedade maxsize indica quantas chamadas mais recente da funcão devem ser amarzenadas em cache.
 Defini-la com NONE, significa que não há limites 
 '''
# functools -fornece funções de ordem superior, ou seja, funções que agem em outras funções

# lru cache - mantem um conjunto fixo de itens e descartar automaticamente os itens menos recentemente usados quando o cache atinge sua capacidade




