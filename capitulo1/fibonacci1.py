def fibonacci1 (n : int)-> int :
    return fibonacci1(n -1) + fibonacci1(n-2)

if __name__=='__main__':
    print(fibonacci1(5))


'''
o códgo resulta em um erro de recursão infinita, 
conhecido como RecursionError, 
porque não foram definidos casos base para a função fibonacci1.
Esses casos base são necessários para interromper a recursão e evitar que a função continue chamando a si mesma indefinidamente.

 Python tem um limite de recursao, para evitar que
 o programa use toda memória, causando travamento.

'''