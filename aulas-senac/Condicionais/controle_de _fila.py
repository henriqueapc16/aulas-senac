"""controle de fila em um evento 
crie um algritmo para organizar a entrada de pessoa em um evento 
evintando  tumulto e garantindo a checagem de ingresso ."""

print("controle de fila do moto: \n")
 # variavel que recebe o valor digitado pelo usuário .
ingresso = input("Digite o código do seu ingresso: \n")
# ingressos validos disponivel 
ingressos_valido = ["001","002","003","004","005"]

ingressos_oculpados =[ "006","007","008","009","0010"]
# condicional, pega a variavel digitada pelo o usuário e compara com á variavel ingresso_valido . 
if ingresso in ingressos_valido:
# se for válido iprimir na tela.

        print("ingresso válido")

elif ingresso in ingressos_oculpados :
        
        print(" ingresso já está oculpado")

else:
         # se não  imprimar na tela .
         print("ingresso não é válido")

