print("\n\n")
print("Agência de viagem" )
valor = float(input("digite o valor disponivel para viagem (r$):"))
regiao = str(input("digite a cidade de origem:"))


destinos = ["Recife (PE)","Porto de Galinha(PE)","RIO de Janeiro","Gramado"]

for i in (destinos):
    print("opçoes de destinos disponiveis:")
    primeiro_destino = destinos [0]
    print(f"1:{primeiro_destino}")
    segundo_destino = destinos [1]
    print(f"2:{segundo_destino}")
    terceiro_destino = destinos [2]
    print(f"3:{terceiro_destino}")
    quarto_destino = destinos [3]
    print(f"4:{quarto_destino}")
    
    break

escolha_destino = int(input("escolha o destino (0,1,2,3,4):"))

opc_transporte = [f"ônibus (R$ 155)", "carona( R$ 110)","avião (R$ 500)"]

# falta concluir

