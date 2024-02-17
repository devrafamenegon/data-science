from utils import *
from database import *

sintomas = []
lerSintomas = True

#LER SINTOMAS
while lerSintomas == True:
  sintomas.append({ "SINTOMA": indique_sintoma(), "GRAU": indique_grau() })

  lerSintomas = adicionar_sintoma()

#ZERAR VALORES DE OCORRÊNCIAS
zerar_ocorrencias()

#CALCULAR OCORRÊNCIAS
for pos, i in enumerate(BD):
  bdDoenca = i["DOENCA"]
  bdSintomas = i["SINTOMAS"]

  for pos, k in enumerate(sintomas):
    sintoma = k["SINTOMA"]
    grau = k["GRAU"]
    if (sintoma in bdSintomas): 
      print(sintoma, " É CARACTERÍSTICA DA DOENÇA: ", bdDoenca, " TENDO OUTROS SINTOMAS: ", bdSintomas)
      i["OCORRENCIAS"] += bdSintomas[sintoma] * (float(grau)/10)

#VERIFICAÇÃO DE MATCHING CONSIDERANDO O TOTAL DE SINTOMAS
print("\n*************************************")
print("\nRESULTADOS PARA OS SINTOMAS: ")

for pos, i in enumerate(sintomas):
  print(" - ", i["SINTOMA"])

print("\nPROBABILIDADE DE MATCHING CONSIDERANDO O TOTAL DE SINTOMAS: ")

for pos, i in enumerate(BD):
  bdDoenca = i["DOENCA"]
  bdSintomas = i["SINTOMAS"]

  total = sum(bdSintomas[k] for k in bdSintomas)

  BD[pos]["PERCENTUAL"] = float(i["OCORRENCIAS"])/total*100

  print(format(float(BD[pos]["PERCENTUAL"]),"5.2f"), "% = ", i["DOENCA"])

# SEPEARAR DOENCA E PERCENTURAL
aux = [[ v["PERCENTUAL"], v["DOENCA"]] for v in BD]
ordenado=sorted(aux,reverse=True)

print("\nVALORES ORDENADOS:")
for i in ordenado:
  percentual = format(i[0],"5.2f")

  print(percentual, "% = ", i[1])