import time
print("olá, quer saber como está o clima ? \n")
input("Qual sua cidade ? : \n")

# lista de condições climaticas

ceu = input("como está o céu ?: \n \n1-sol radiante \n2-poucas nuvens \n3-nublado \n\n digite de 1 a 2: \n ")
temperatura = input("como está a sensação térmica ? :\n1-quente \n2-moderada \n3-frio \n\ndigite de 1 a 2 :\n")
vento = input(" como está o vento ? :\n \n1-ventos fraco \n2-brisa suave  \n3-ventos muito forte :\n\ndigite de 1 a 3:\n")

# lista de verificação de condições climaticas

if ceu == "1" and  temperatura == "1" and vento == "1":
    time.sleep(3)
    print("Dia de sol , ótimo para ir a praia\n")

elif ceu == "2" and temperatura == "2" and vento  == "2" :
    time.sleep(3) 
    print ("A umidade do ar está ideal, 20% de chance de chuva. \n")

elif ceu == "3" and temperatura == "3" and vento  == "3":
    time.sleep(3)
    print("Alta possibilidade de chuva , leve Guarda-Chuva. \n ")

elif ceu == "1"and temperatura == "2" and vento  == "3":
    time.sleep(3)
    print("Dia com ventos forte e baixa probabilidade de chuva.")     
else:
    time.sleep(3)
    print("Falta de imformação para definir a previsão")
    print("\n\n")
    print(" Tenha um ótimo dia, obrigado por usar nosso serviço!")

    #CONCLUIDO