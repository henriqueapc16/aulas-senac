"""controle de fila em um evento 
crie um algritmo para organizar a entrada de pessoa em um evento 
evintando  tumulto e garantindo a checagem de ingresso ."""
import time
print("controle de fila: \n")

#coleta de dados
codigo_digitado = (input("Por favor, digite o número do ingresso para checagem:")).strip().upper()
# lista opção de ingressos validos
ingressos_validos = ["001","002","003","004","005"]

if codigo_digitado in ingressos_validos:
            print("ingresso válidado entrada liberada")
else:
            print("ingresso invalido")























