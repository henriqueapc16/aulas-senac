usuario = (input("Digite o modelo do seu carro:\n"))
carros =["uno","posher","cromos","cross"]

def veiculo (dados):
  if usuario in dados:
      print("carro em estoque")
  else:
      print( "não temos o modelo do seu carro")



veiculo(carros)