from typing import Final
IDADE_MININA: Final = 18 
idade= int(input("digite sua idade"))
if idade >=18: 
    print("você é maior de idade")
elif idade >=60: 
    print(" você chegou na terceira idade")
else: print (" você é menor de idade")