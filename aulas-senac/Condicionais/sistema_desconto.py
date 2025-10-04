#importa class final para informa o fim da constante 
from typing import Final
VALOR_MININO: Final =100 # constante 
valor= float(input("digite o valor")) # interação com o usuário, oelemento ( float) é usado para número decinais 
if valor >=100: # se  for maior ou iual a 100 imprimar 
    print("você ganhou desconto de 10%")
else: #se não  inprimar 
    print ("você não atigiu o valor minino")
