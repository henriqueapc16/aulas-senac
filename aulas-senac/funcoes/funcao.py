def cadastrar (dados):
  usuario =(input("Digite seu nome"))
  nomes =[ "Jose","Maria","Ana","João"]
  if usuario in nomes:
    print("você esta cadastrado")
  else:
    print( "vocÊ não esta no banco de dados")
    cadastrar(nomes)
