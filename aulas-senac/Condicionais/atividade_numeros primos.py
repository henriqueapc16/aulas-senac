"""n = int(input("Verificar numeros primos ate: "))
mult=0

for count in range(2,n):
    if (n % count == 0):
        print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print(" não é primo",n)
"""
# condicional
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Entrada do usuário
numero = int(input("Digite um número: "))

# Verificação
if eh_primo(numero):
    print(f"{numero} é primo ")
else:
    print(f"{numero} não é primo ")
  
  #concluido