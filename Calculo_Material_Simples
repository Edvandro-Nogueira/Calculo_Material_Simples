#Autor: Edvandro Nogueira de Souza
#Este algoritmo simples faz o cálculo de barras necessárias dado um n quantidade de peças.
#Não leva em consideração um aproveitamento sofisticado, ele apenas ordena os elementos de forma crescente e tenta alocar na barra com a medida dada.

#Imports
from copy import deepcopy

# Função para itens repetidos
def add_lista (qtd, medida):
  qtd = qtd
  medida = medida
  if qtd == 1:
    lista_de_pecas.append(medida)
  else:
    lista_de_pecas.append(medida)
    add_lista((qtd-1), medida)

#Função para otimização e aproveitamento
def otimiza (lista_de_pecas_temp):
    medida_barra = deepcopy(medida_barra_geral)
    barra = []
    lista_temp = deepcopy(lista_de_pecas_temp)
    for n in lista_de_pecas_temp:
        if n <= medida_barra:
            barra.append(n)
            lista_temp.remove(n)
            medida_barra = medida_barra-(n)

    lista_de_pecas_temp = lista_temp
    barras = deepcopy(barra)
    barras_totais.append(barras)
    if lista_de_pecas_temp != []:
        otimiza(lista_de_pecas_temp)
    barra.clear()

#Usar este metodo ou o proximo
'''
print('Desenvolvido por Edvandro, este algoritmo apenas pega as medidas passada, coloca em ordem e vai alocando na barra cadastrada')
material = input('Qual material esta calculando?')
medida_barra_geral = int(input('Qual a medida da barra?'))
try:
    lista_de_pecas = []
    while True:
        lista_de_pecas.append(int(input('Digite a medida da peça ou "f" para parar')))
except:
    pass
'''

#Tabela de peso especifico por m2
peso = {"D-069":0.950, "D-078":0.795, "78-719":1.555, "T-095":0.210, "L-002":0.076, "GS-034 - 78-1873C":0.805, "GS-034 - 78-1958D":0.795, "39-2072C":0.145,
        "Cx. Al.":(3.386+1.398), "D-079":0.564, "D-102":0.625}

#Este é o outro metodo de inserção
lista_de_pecas = []
material = '78-719'
medida_barra_geral = 6000
#lista_de_pecas = [110]
add_lista(2,3252)
add_lista(2,2256)
add_lista(2,2665)
add_lista(2,2253)

#Codigo principal
lista_de_pecas.sort(reverse=True)
barra = []
barras = []
barras_totais = []
lista_de_pecas_temp = deepcopy(lista_de_pecas)
otimiza(lista_de_pecas_temp)

print('-' * 100)
if len(barras_totais) == 1:
    print(len(barras_totais),'barra de', material, 'com', medida_barra_geral, 'mm')
else:
    print(len(barras_totais), 'barras de', material, 'com', medida_barra_geral, 'mm')
print('-' * 100)
print('Lista de barras de', material, 'com', medida_barra_geral, 'mm:')
if len(barras_totais) == 1:
  print('Total de barras necessárias:', len(barras_totais),'barra')
else:
  print('Total de barras necessárias:', len(barras_totais),'barras')
print('-' * 100)
print('CORTES:')
sobraTotal = 0
for n in range(len(barras_totais)):
    print('Barra',n+1,':',barras_totais[n], '| Sobra: ',(medida_barra_geral-sum(barras_totais[n])))
    sobraTotal = sobraTotal + (medida_barra_geral - sum(barras_totais[n]))

print('-' * 100)
print("RELATORIO")
print("Aproveitamento:",round(100-((sobraTotal*100)/(len(barras_totais)*medida_barra_geral)),2),"%")
print("Peso total das", len(barras_totais),"barras:", round((peso[material]*(len(barras_totais)*medida_barra_geral)/1000),2),"Kg")
print('-' * 100)
