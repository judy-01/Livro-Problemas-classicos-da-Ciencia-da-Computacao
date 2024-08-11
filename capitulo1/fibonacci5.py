def fibonacci5(n: int) -> int :
    if n == 0 : return n # caso base
    antes: int = 0
    depois: int = 1

    for _ in range(1, n):
        antes, depois = depois, antes + depois
        return depois  # interrompe o loop. Para rodar corretamente o return depois precisa ficar fora do loop
if __name__ =="__main__":
    print(fibonacci5(5))
    print(fibonacci5(50))