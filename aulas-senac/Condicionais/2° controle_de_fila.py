print("contrle de fila: \n")

checar_ingresso = input ("Digite o código do ingresso: \n")
ingressos_validos = ("1","2","3","4","5")
match  checar_ingresso in ingressos_validos:
  case ("1","2","3","4","5"):
    print("ingresso válidado ")
  case _:
    print("ingresso invalido")
    

     # não concluido