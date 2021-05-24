#Autor: Edvandro Nogueira de Souza
#Este algoritmo simples faz o cálculo de barras necessárias dado n quantidade de peças.
#Não leva em consideração um aproveitamento sofisticado, ele apenas ordena os elementos de forma decrescente e tenta alocar na barra com a medida dada.

# Imports
from copy import deepcopy

#arquivoIN = open("/Lista_Material_IN.txt", "r")

arquivo = open("/Lista_Corte.txt", "w")

#Arquivo de saída 2
arquivo2 = open("/Lista_Material_Simples.txt", "w")

#Arquivo de saída 3
arquivo3 = open("/Lista_Pecas.txt", "w")

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
        #print(self.material, self.medida_barra_geral, self.lista_de_pecas)

    def __del__(self):
       self.lista_de_pecas = []

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
        "Cx. Al.": (3.386 + 1.398), "D-079": 0.564, "D-102": 0.625, "TUB-4008": 0.386, "19-375": 0.919, "50-018": 0.263, "U-491": 0.093,
        "U-425": 0.145, "D-082": 0.349, "U-1048": 1.120, "U-990": 0.827, "VA-203A": 0.292, "Y-120": 0.247,
        "SU-279": 0.585, "SU-111": 0.620, "SU-108": 0.146, "TUB-4569": 0.595, "L-741": 0.161}

#Função de alocação
def calc2 (medida_barra, lista, i):
    medida_barra = int(medida_barra)
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
arquivo3.write("LISTA DE PEÇAS:")
arquivo3.write("\n")
arquivo3.write("\n")

# Função principal
def calc(mat, medida_barra, lista, i):
    medida_barra = int(medida_barra)
    mat = mat.split(':')
    mat = mat[1]
    print('#' * 100)
    p = ('#' * 100)
    p = str(p)
    arquivo.write(p)
    arquivo.write("\n")
    arquivo3.write(mat)
    arquivo3.write("\n")
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
        p2 = (len(totalBarra),"barras de",mat,"com",medida_barra,"mm |",round(float((peso[mat]) * (int(len(totalBarra)) * int(medida_barra)) / 1000), 2),"Kg|")
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
        p2 = (len(totalBarra), "barra de", mat, "com", medida_barra, "mm |",round((peso[mat] * (len(totalBarra) * medida_barra) / 1000), 2),"Kg|")
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
        p = ("Barra",n+1,":", totalBarra[n], '| Sobra:',(medida_barra-sum(totalBarra[n])))
        p = str(p)
        p = p.replace("'","").replace("(", "").replace(")", "")
        p = p.replace(",", "", -1)
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


def conta(lista):
    lista.sort(reverse=True)
    listaQualifica = []
    listaQtd = []
    qtd = 0
    for m in lista:
        for n in lista:
            if m == n & m not in listaQualifica:
                listaQualifica.append(m)
    for m in listaQualifica:
        for n in lista:
            if m == n:
                qtd = qtd + 1
        listaQtd.append(qtd)
        qtd = 0
    for m in range(len(listaQtd)):
        if listaQtd[m] > 1:
            p = listaQtd[m], "peças de", listaQualifica[m], "mm"
            p = str(p)
            p = p.replace("'", "").replace(",", "", 1).replace(",", "", 2).replace(",", "", -1).replace("(","").replace(")", "")
            arquivo3.write(p)
            arquivo3.write("\n")
            #print(m,"peças de",n,"mm")
        else:
            #print(m,"peça de",n,"mm")
            p = listaQtd[m], "peça de", listaQualifica[m], "mm"
            p = str(p)
            p = p.replace("'", "").replace(",", "", 1).replace(",", "", 2).replace(",", "", -1).replace("(","").replace(")", "")
            arquivo3.write(p)
            arquivo3.write("\n")
    arquivo3.write("\n")


'''
#Este trecho esta sendo substituido pela leitura de dos dados em um .txt
# Declarando as peças
lista_de_pecas = [] #Limpa a lista de peças
mat = "78-719" #Material
mat = Mat(mat, 6000, add_lista(1, 2575))
mat.lista_de_pecas = add_lista(1, 2493)
mat.lista_de_pecas = add_lista(4, 1834)
mat.lista_de_pecas = add_lista(4, 2419)
calc(mat.material, mat.medida_barra_geral, mat.lista_de_pecas, i)
conta(lista_de_pecas)
totalBarra = []

# Declarando as peças
lista_de_pecas = [] #Limpa a lista de peças
mat = "L-741" #Material
mat = Mat(mat, 6000, add_lista(2, 2419))
calc(mat.material, mat.medida_barra_geral, mat.lista_de_pecas, i)
conta(lista_de_pecas)
totalBarra = []
'''

lista = []
material = []

def gera2(rod, pos, m):
    mat = m
    print('alala',index[rod + 1] - index[rod] - 3)
    for m in range(index[rod + 1] - index[rod] - 3):
        ad = lista[pos + (m + 3)].split(',')
        mat.lista_de_pecas = add_lista(int(ad[0]),int(ad[1]))
        print('gera2',mat.lista_de_pecas)
        #ad = []

def gera(it, rod):
    if it > 0:
        pos = int(index[rod])
        #lista_de_pecas = []
        mat1 = lista[pos].split(':')
        mat = str(mat1[1])
        mat = str(mat)
        ad = lista[pos + 2].split(',')
        mat = Mat(mat, int(lista[pos + 1]), add_lista(int(ad[0]),int(ad[1])))
        print('gera', mat.lista_de_pecas)
        print('chamando a gera2', rod, pos, mat)
        gera2(rod, pos, mat)
        #A lista mat.lista_de_pecas não esta sendo apagada, com isso estou ficando com peças repetidas em outras listas
        #calc(mat.material, mat.medida_barra_geral, mat.lista_de_pecas, i)
        conta(mat.lista_de_pecas)
        del mat
        totalBarra = []
        gera(it - 1, rod + 1)

with open("/Users/edvandro/Downloads/Fabril - docs/Lista_Material_IN.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        lista.append(str(line))

for m in range(len(lista)):
    if "Mat" in lista[m]:
        l = lista[m].split(":")
        material.append(str(l[1]))

index = []
for x in range(len(lista)):
    if "Mat" in lista[x]:
        index.append(x)
    if "FIM" in lista[x]:
        index.append(x)

it = len(index)
gera(it - 1, 0)

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
