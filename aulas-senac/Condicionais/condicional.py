usuario = str(input("cadastre seu nome: "))
nome= usuario
print(f"sejá bem vindo !, {nome}: ")
idade = int(input("idade:"))

if idade >= 20:
  print( " idade liberada:")

elif idade >= 60:
  print ("liberado para sala de domino")

else:
  print("você não está apto")
