# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:16:38 2023

@author: AM
"""

BD=[ {"DOENCA":"GRIPE","SINTOMAS": {"TOSSE":5,"FEBRE":7,"DOR GARGANTA":8,"CORIZA":6,"FADIGA":3},"OCORRENCIAS": 0,"PERCENTUAL":0},
     {"DOENCA":"DENGUE","SINTOMAS": {"FEBRE":9,"DOR CORPO":8,"MANCHAS CORPO":5},"OCORRENCIAS": 0,"PERCENTUAL":0},   
     {"DOENCA":"COVID","SINTOMAS": {"FEBRE":9,"TOSSE":9,"CORIZA":4,"CANSACO":8,"PERDA PALADAR":7},"OCORRENCIAS": 0,"PERCENTUAL":0},
     {"DOENCA":"DIABETES","SINTOMAS": {"DOR CORPO":5,"MANCHAS CORPO":3,"PERDA PESO":6,"SEDE":9,"FADIGA":8},"OCORRENCIAS": 0,"PERCENTUAL":0}
   ]

#LER 3 SINTOMAS E VERIFICAR DOENÇAS
sintoma1=input("INDIQUE O PRIMEIRO SINTOMA: ")
sintoma2=input("INDIQUE O SEGUNDO SINTOMA: ")
sintoma3=input("INDIQUE O TERCEIRO SINTOMA: ")

#ZERAR VALORES DE OCORRÊNCIAS
for i in BD:
  i["OCORRENCIAS"]=0
  i["PERCENTUAL"]=0


for pos,i in enumerate(BD):
  doenca=i["DOENCA"]
  sintomas=i["SINTOMAS"]
  if (sintoma1 in sintomas): 
    print("O SINTOMA: ",sintoma1," É CARACTERÍSTICA DA DOENÇA: ",doenca,"  TENDO OUTROS SINTOMAS: ",sintomas)
    i["OCORRENCIAS"]+=sintomas[sintoma1]
  if (sintoma2 in sintomas): 
    print("O SINTOMA: ",sintoma2," É CARACTERÍSTICA DA DOENÇA: ",doenca,"  TENDO OUTROS SINTOMAS: ",sintomas)
    i["OCORRENCIAS"]+=sintomas[sintoma2]
  if (sintoma3 in sintomas): 
    print("O SINTOMA: ",sintoma3," É CARACTERÍSTICA DA DOENÇA: ",doenca,"  TENDO OUTROS SINTOMAS: ",sintomas)
    i["OCORRENCIAS"]+=sintomas[sintoma3]

# VERIFICAÇÃO DE MATCHING CONSIDERANDO O TOTAL DE SINTOMAS
print("*************************************")
print("RESULTADOS PARA OS SINTOMAS: ")
print("    ",sintoma1)
print("    ",sintoma2)
print("    ",sintoma3)
print("    ")
print("PROBABILIDADE DE MATCHING CONSIDERANDO O TOTAL DE SINTOMAS: ")

for pos,i in enumerate(BD):
  doenca=i["DOENCA"]
  sintomas=i["SINTOMAS"]
  total=sum(sintomas[k] for k in sintomas)
  BD[pos]["PERCENTUAL"]=float(i["OCORRENCIAS"])/total*100
  print("DOENÇA: ",i["DOENCA"],"   = ", format(float(BD[pos]["PERCENTUAL"]),"5.2f")," %")


# SEPEARAR DOENCA E PERCENTURAL
aux=[ [v["PERCENTUAL"],v["DOENCA"]] for v in BD]
ordenado=sorted(aux,reverse=True)
ordenado
print("  ")
print("VALORES ORDENADOS:")
for i in ordenado:
 percentual=format(i[0],"5.2f")
 print("A DOENCA: ",i[1]," TEM  ",percentual," % DE PROBABILIDADE DE ATENDER AOS SINTOMAS ESPECIFICADOS")
 
 
 
 
 