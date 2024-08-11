from typing import Generator
def fibonacci6 (n: int)-> Generator[int, None, None]:
    if n > 0 : yield 1
    antes: int = 0
    depois: int = 1

    for _ in range(1, n):
        antes, depois = depois, antes + depois
        yield depois

if __name__ =="__main__":
    for i in fibonacci6(50):
        print(i)


'''
A palavra-chave yield em Python é usada para criar geradores, permitindo que uma função produza uma sequência de valores para iteração12. Quando uma função contendo yield é chamada, ela retorna um objeto gerador que pode ser iterado para recuperar valores um de cada vez1. O yield pausa a execução da função e retorna um valor temporariamente, sem perder seu estado interno23.

'''