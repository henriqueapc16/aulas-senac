from typing import Final #"Essa variável/atributo é final (constante), não pode ser sobrescrita." importa class final para informa o fim da constante 
IDADE_MININA: Final = 18 
idade= int(input("digite sua idade: \n"))
if idade >= 60: 
         print(" você chegou na terceira idade ")

elif idade >= 18: 
        print("você é maior de idade ")
else:   
       print ("você é menor de idade")

    # falta concluir 