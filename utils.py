def indique_sintoma():
  return input("INDIQUE O SINTOMA: ").upper()

def indique_grau():
  return input(" - INDIQUE O GRAU DO SINTOMA (0 a 10): ")

def adicionar_sintoma():
  respondeu = False

  while respondeu == False:
    continuar = input("\nQUER INDICAR OUTRO SINTOMA? [S] OU [N]: ").lower()

    if continuar == 's':
      respondeu = True
      return True
      
    if continuar == 'n':
      respondeu = True
      return False

    print("\nOPÇÃO INVÁLIDA")
