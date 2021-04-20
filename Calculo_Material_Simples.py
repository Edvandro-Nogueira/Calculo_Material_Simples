#Autor: Edvandro Nogueira de Souza
#Este algoritmo simples faz o cálculo de barras necessárias dado n quantidade de peças.
#Não leva em consideração um aproveitamento sofisticado, ele apenas ordena os elementos de forma decrescente e tenta alocar na barra com a medida dada.

# Imports
from copy import deepcopy

#Endereço de entrada dos materiais .txt
ent = "/Lista_Material_IN.txt"

#Endereço de saída do relatório 2 .txt
end1 = "/Lista_Material_Simples.txt"

#Endereço de saída do relatório 2 .txt
end2 = "/Lista_Material.txt"

#Arquivo de Entrada
arquivoIN = open(ent, "r")

#Arquivo de saída
arquivo = open(end2, "w")
#Arquivo de saída 2
arquivo2 = open(end1, "w")

#Declaração de variaveis globais
lista_de_pecas = []
i = 1
totalBarra = []
pesoBarrasTotaisServico = 0.0
pesoPecasTotaisServico = 0.0

#Classe de cada material para calculo
class Mat:
    def __init__(self, material, medida_barra_geral, lista_de_pecas):
        self.material = material
        self.medida_barra_geral = medida_barra_geral
        self.lista_de_pecas = lista_de_pecas

#Função de alocação de iteração de duplicadas nas quantidades
def add_lista(qtd, medida):
    if qtd == 1:
        lista_de_pecas.append(medida)
        return lista_de_pecas
    else:
        lista_de_pecas.append(medida)
        add_lista((qtd - 1), medida)
        return lista_de_pecas

# Tabela de peso especifico por m2
peso = {"D-069": 0.950, "D-078": 0.795, "78-719": 1.555, "T-095": 0.210, "L-002": 0.076, "GS-034 - 78-1873C": 0.805,
        "GS-034 - 78-1958D": 0.795, "39-2072C": 0.145,
        "Cx. Al.": (3.386 + 1.398), "D-079": 0.564, "D-102": 0.625}

#Função de alocação
def calc2 (medida_barra, lista, i):
    nbarra = []
    lista.sort(reverse=True)
    lista_temp = deepcopy(lista)
    medida_barra_temp = deepcopy(medida_barra)
    for n in lista:
        if n <= medida_barra_temp:
            nbarra.append(n)
            lista_temp.remove(n)
            medida_barra_temp = medida_barra_temp - n
    totalBarra.append(nbarra)
    lista = deepcopy(lista_temp)
    if lista_temp != []:
        calc2(medida_barra, lista, i+1)
    return totalBarra

arquivo2.write("LISTA DE MATERIAL NECESSARIO:")
arquivo2.write("\n")

# Função principal
def calc(mat, medida_barra, lista, i):
    print('#' * 100)
    p = ('#' * 100)
    p = str(p)
    arquivo.write(p)
    arquivo.write("\n")
    print('Lista de barras de', mat, 'com', medida_barra, 'mm:')
    p = ('Lista de barras de', mat, 'com', medida_barra, 'mm:')
    p = str(p)
    p = p.replace("'", "").replace(",", "", 1).replace(",", "", 2).replace(",", "", -1).replace("(", "").replace(")","")
    arquivo.write(p)
    arquivo.write("\n")
    totalBarra = calc2(medida_barra, lista, i)
    if len(totalBarra) > 1:
        print("Total de barras necessárias:",len(totalBarra),"barras")
        p = ("Total de barras necessárias:",len(totalBarra),"barras")
        p2 = (len(totalBarra),"barras de",mat,"com",medida_barra,"mm |",round((peso[mat] * (len(totalBarra) * medida_barra) / 1000), 2),"Kg|")
        p = str(p)
        p2 = str(p2)
        p = p.replace("'", "").replace(",", "", 1).replace(",", "", 2).replace(",", "", -1).replace("(", "").replace(")", "")
        p2 = p2.replace("'", "").replace(",", "", 1).replace(",", "", 2).replace(",", "", -1).replace("(", "").replace(")", "")
        arquivo.write(p)
        arquivo2.write(p2)
        arquivo.write("\n")
        arquivo2.write("\n")
    else:
        print("Total de barras necessárias:", len(totalBarra), "barra")
        p = ("Total de barras necessárias:",len(totalBarra),"barras")
        p2 = (len(totalBarra), "barra de", mat, "com", medida_barra, "mm")
        p = str(p)
        p2 = str(p2)
        p = p.replace("'", "").replace(",", "", 1).replace(",", "", 2).replace(",", "", -1).replace("(", "").replace(")", "")
        p2 = p2.replace("'", "").replace(",", "", 1).replace(",", "", 2).replace(",", "", -1).replace("(", "").replace(")", "")
        arquivo.write(p)
        arquivo2.write(p2)
        arquivo.write("\n")
        arquivo2.write("\n")
    print('-' * 100)
    p = ('-' * 100)
    p = str(p)
    arquivo.write(p)
    arquivo.write("\n")
    print('CORTES:')
    arquivo.write("CORTES:")
    arquivo.write("\n")
    for n in range(len(totalBarra)):
        print("Barra",n+1,":", totalBarra[n], '| Sobra: ',(medida_barra-sum(totalBarra[n])))
        p = ("Barra",n+1,":", totalBarra[n], '| Sobra: ',(medida_barra-sum(totalBarra[n])))
        p = str(p)
        p = p.replace("'","").replace(",", "", 1).replace(",", "", 2).replace(",", "", -1).replace("(", "").replace(")", "")
        arquivo.write(p)
        arquivo.write("\n")
    print('-' * 100)
    p = ('-' * 100)
    p = str(p)
    arquivo.write(p)
    arquivo.write("\n")
    print("RELATÓRIO:")
    arquivo.write("RELATÓRIO:")
    arquivo.write("\n")
    sobraTotal = 0
    pecas_Totais = 0
    for n in range(len(totalBarra)):
        sobraTotal = sobraTotal + (medida_barra - sum(totalBarra[n]))
        pecas_Totais = pecas_Totais + sum(totalBarra[n])
    print("Aproveitamento:", round(100 - ((sobraTotal * 100) / (len(totalBarra) * medida_barra)), 2), "%")
    p = ("Aproveitamento:", round(100 - ((sobraTotal * 100) / (len(totalBarra) * medida_barra)), 2), "%")
    p = str(p)
    p = p.replace("'", "").replace(",", "", 1).replace(",", "", 2).replace(",", "", -1).replace("(", "").replace(")","")
    arquivo.write(p)
    arquivo.write("\n")
    print("Peso total das", len(totalBarra), "barras:", round((peso[mat] * (len(totalBarra) * medida_barra) / 1000), 2), "Kg")
    p = ("Peso total das", len(totalBarra), "barras:", round((peso[mat] * (len(totalBarra) * medida_barra) / 1000), 2), "Kg")
    p = str(p)
    p = p.replace("'", "").replace(",", "", 1).replace(",", "", 2).replace(",", "", -1).replace("(", "").replace(")","")
    arquivo.write(p)
    arquivo.write("\n")
    global pesoBarrasTotaisServico
    pesoBarrasTotaisServico = pesoBarrasTotaisServico + (peso[mat] * (len(totalBarra) * medida_barra) / 1000)
    print("Peso total das peças:", round((pecas_Totais / 1000) * peso[mat], 2), "Kg")
    p = ("Peso total das peças:", round((pecas_Totais / 1000) * peso[mat], 2), "Kg")
    p = str(p)
    p = p.replace("'", "").replace(",", "", 1).replace(",", "", 2).replace(",", "", -1).replace("(", "").replace(")","")
    arquivo.write(p)
    arquivo.write("\n")
    global pesoPecasTotaisServico
    pesoPecasTotaisServico = pesoPecasTotaisServico + ((pecas_Totais / 1000) * peso[mat])
    print(" ")
    arquivo.write("\n")

# Declarando as peças
lista_de_pecas = [] #Limpa a lista de peças
mat = "Cx. Al." #Material
mat = Mat(mat, 5000, add_lista(2, 2430))
mat.lista_de_pecas = add_lista(2, 2433)
calc(mat.material, mat.medida_barra_geral, mat.lista_de_pecas, i)
totalBarra = []

lista_de_pecas = [] #Limpa a lista de peças
mat = "D-069" #Material
mat = Mat(mat, 6000, add_lista(1, 110))
mat.lista_de_pecas = add_lista(2, 3325)
mat.lista_de_pecas = add_lista(2, 2738)
calc(mat.material, mat.medida_barra_geral, mat.lista_de_pecas, i)
totalBarra = []

lista_de_pecas = [] #Limpa a lista de peças
mat = "78-719" #Material
mat = Mat(mat, 6000, add_lista(2, 3252))
mat.lista_de_pecas = add_lista(2, 2256)
mat.lista_de_pecas = add_lista(2, 2665)
mat.lista_de_pecas = add_lista(2, 2253)
calc(mat.material, mat.medida_barra_geral, mat.lista_de_pecas, i)
totalBarra = []

lista_de_pecas = [] #Limpa a lista de peças
mat = "D-078" #Material
mat = Mat(mat, 6000, add_lista(1, 2151))
mat.lista_de_pecas = add_lista(1, 2033)
mat.lista_de_pecas = add_lista(2, 790)
mat.lista_de_pecas = add_lista(2, 2135)
calc(mat.material, mat.medida_barra_geral, mat.lista_de_pecas, i)
totalBarra = []

lista_de_pecas = [] #Limpa a lista de peças
mat = "T-095" #Material
mat = Mat(mat, 6000, add_lista(1, 2175))
mat.lista_de_pecas = add_lista(1, 1036)
mat.lista_de_pecas = add_lista(1, 1053)
mat.lista_de_pecas = add_lista(1, 143)
mat.lista_de_pecas = add_lista(1, 2135)
mat.lista_de_pecas = add_lista(2, 3174)
mat.lista_de_pecas = add_lista(2, 2178)
mat.lista_de_pecas = add_lista(2, 1730)
mat.lista_de_pecas = add_lista(2, 98)
mat.lista_de_pecas = add_lista(2, 479)
mat.lista_de_pecas = add_lista(4, 2057)
mat.lista_de_pecas = add_lista(2, 207)
calc(mat.material, mat.medida_barra_geral, mat.lista_de_pecas, i)
totalBarra = []

lista_de_pecas = [] #Limpa a lista de peças
mat = "L-002" #Material
mat = Mat(mat, 6000, add_lista(1, 2151))
mat.lista_de_pecas = add_lista(1, 1012)
mat.lista_de_pecas = add_lista(1, 1029)
mat.lista_de_pecas = add_lista(1, 143)
mat.lista_de_pecas = add_lista(2, 3150)
mat.lista_de_pecas = add_lista(2, 1706)
mat.lista_de_pecas = add_lista(2, 98)
mat.lista_de_pecas = add_lista(2, 455)
mat.lista_de_pecas = add_lista(4, 2033)
mat.lista_de_pecas = add_lista(2, 183)
calc(mat.material, mat.medida_barra_geral, mat.lista_de_pecas, i)
totalBarra = []

lista_de_pecas = [] #Limpa a lista de peças
mat = "GS-034 - 78-1873C" #Material
mat = Mat(mat, 6000, add_lista(17, 3150))
mat.lista_de_pecas = add_lista(17, 1706)
mat.lista_de_pecas = add_lista(16, 455)
calc(mat.material, mat.medida_barra_geral, mat.lista_de_pecas, i)
totalBarra = []

lista_de_pecas = [] #Limpa a lista de peças
mat = "GS-034 - 78-1958D" #Material
mat = Mat(mat, 6000, add_lista(4, 3150))
mat.lista_de_pecas = add_lista(4, 1706)
mat.lista_de_pecas = add_lista(4, 455)
calc(mat.material, mat.medida_barra_geral, mat.lista_de_pecas, i)
totalBarra = []
#Fim da declaração dos itens

#Término do relatório
print('#' * 100)
p = ('#' * 100)
p = str(p)
arquivo.write(p)
arquivo2.write(p)
arquivo.write("\n")
arquivo2.write("\n")
print("Peso total de todas as BARRAS do serviço:", round(pesoBarrasTotaisServico,2),"Kg")
p = ("Peso total de todas as BARRAS do serviço:", round(pesoBarrasTotaisServico,2),"Kg")
p = str(p)
p = p.replace("'", "").replace(",", "", 1).replace(",", "", 2).replace(",", "", -1).replace("(", "").replace(")","")
arquivo.write(p)
arquivo.write("\n")
print("Peso total de todas as PEÇAS do serviço:", round(pesoPecasTotaisServico,2),"Kg")
p = ("Peso total de todas as PEÇAS do serviço:", round(pesoPecasTotaisServico,2),"Kg")
p = str(p)
p = p.replace("'", "").replace(",", "", 1).replace(",", "", 2).replace(",", "", -1).replace("(", "").replace(")","")
arquivo.write(p)
arquivo.write("\n")
p2 = ("Peso total de todas as BARRAS do serviço:", round(pesoBarrasTotaisServico,2),"Kg")
p2 = str(p2)
p2 = p2.replace("'", "").replace(",", "", 1).replace(",", "", 2).replace(",", "", -1).replace("(", "").replace(")","")
arquivo2.write(p2)
arquivo2.write("\n")
#print("Peso todas das peças marcadas com M:")
arquivo.close()
