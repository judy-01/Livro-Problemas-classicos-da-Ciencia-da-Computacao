n =int(input('digite qual o numero da sequência fibonacci, deseja saber : '))

def fibonacci2 (n : int)-> int :
    
    if n < 2 :
        return n
    return fibonacci2( n - 1) + fibonacci2( n - 2) 
if __name__=='__main__':
    print(fibonacci2(n))

