
import os
import time as t



class Cidade:
    def __init__(self, nome, distancia_objetivo):
        self.nome = nome  # Nome da cidade
        self.visitado = False  # Se o vértice (cidade) já foi visitado
        self.distancia_objetivo = distancia_objetivo  # Distância do vértice (cidade) para a cidade de objetivo
        self.adjacentes = []  # Lista de cidades adjacentes a esta cidade

    def adicionar_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostrar_adjacentes(self):
        for i in self.adjacentes:
            print(i)


class Adjacente:  # Cidades adjacentes
    def __init__(self, vertice, custo):
        self.vertice = vertice  # Objeto da cidade criado
        self.custo = custo  # Custo da cidade criada até esse vértice
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo  # Custo final do algoritmo A*


class Grafo:
    aveiro = Cidade('Aveiro', 366)
    braga = Cidade('Braga', 454)
    braganca = Cidade('Bragança', 487)
    beja = Cidade('Beja', 99)
    castelo_branco = Cidade('Castelo Branco', 280)
    coimbra = Cidade('Coimbra', 319)
    evora = Cidade('Évora', 157)
    faro = Cidade('Faro', 0)
    guarda = Cidade('Guarda', 352)
    leiria = Cidade('Leiria', 278)
    lisboa = Cidade('Lisboa', 195)
    portalegre = Cidade('Portalegre', 228)
    porto = Cidade('Porto', 418)
    santarem = Cidade('Santarém', 231)
    setubal = Cidade('Setúbal', 168)
    viana_do_castelo = Cidade('Viana', 473)
    vila_real = Cidade('Vila Real', 429)
    viseu = Cidade('Viseu', 363)

    # Aveiro
    aveiro.adicionar_adjacente(Adjacente(porto, 68))
    aveiro.adicionar_adjacente(Adjacente(viseu, 95))
    aveiro.adicionar_adjacente(Adjacente(coimbra, 68))
    aveiro.adicionar_adjacente(Adjacente(leiria, 115))

    # Braga
    braga.adicionar_adjacente(Adjacente(viana_do_castelo, 48))
    braga.adicionar_adjacente(Adjacente(vila_real, 106))
    braga.adicionar_adjacente(Adjacente(porto, 53))

    # Bragança
    braganca.adicionar_adjacente(Adjacente(vila_real, 137))
    braganca.adicionar_adjacente(Adjacente(guarda, 202))

    # Beja
    beja.adicionar_adjacente(Adjacente(evora, 78))
    beja.adicionar_adjacente(Adjacente(faro, 152))
    beja.adicionar_adjacente(Adjacente(setubal, 142))

    # Castelo Branco
    castelo_branco.adicionar_adjacente(Adjacente(coimbra, 159))
    castelo_branco.adicionar_adjacente(Adjacente(guarda, 106))
    castelo_branco.adicionar_adjacente(Adjacente(portalegre, 80))
    castelo_branco.adicionar_adjacente(Adjacente(evora, 203))

    # Coimbra
    coimbra.adicionar_adjacente(Adjacente(viseu, 96))
    coimbra.adicionar_adjacente(Adjacente(leiria, 67))
    coimbra.adicionar_adjacente(Adjacente(aveiro, 68))
    coimbra.adicionar_adjacente(Adjacente(castelo_branco, 159))

    # Évora
    evora.adicionar_adjacente(Adjacente(lisboa, 150))
    evora.adicionar_adjacente(Adjacente(santarem, 117))
    evora.adicionar_adjacente(Adjacente(portalegre, 131))
    evora.adicionar_adjacente(Adjacente(setubal, 103))
    evora.adicionar_adjacente(Adjacente(beja, 78))
    evora.adicionar_adjacente(Adjacente(castelo_branco, 203))

    # Faro
    faro.adicionar_adjacente(Adjacente(setubal, 249))
    faro.adicionar_adjacente(Adjacente(lisboa, 299))
    faro.adicionar_adjacente(Adjacente(beja, 152))

    # Guarda
    guarda.adicionar_adjacente(Adjacente(vila_real, 157))
    guarda.adicionar_adjacente(Adjacente(viseu, 85))
    guarda.adicionar_adjacente(Adjacente(braganca, 202))
    guarda.adicionar_adjacente(Adjacente(castelo_branco, 106))

    # Leiria
    leiria.adicionar_adjacente(Adjacente(lisboa, 129))
    leiria.adicionar_adjacente(Adjacente(santarem, 70))
    leiria.adicionar_adjacente(Adjacente(aveiro, 115))
    leiria.adicionar_adjacente(Adjacente(coimbra, 67))

    # Lisboa
    lisboa.adicionar_adjacente(Adjacente(santarem, 78))
    lisboa.adicionar_adjacente(Adjacente(setubal, 50))
    lisboa.adicionar_adjacente(Adjacente(evora, 150))
    lisboa.adicionar_adjacente(Adjacente(faro, 299))
    lisboa.adicionar_adjacente(Adjacente(leiria, 129))

    # Portalegre
    portalegre.adicionar_adjacente(Adjacente(castelo_branco, 80))
    portalegre.adicionar_adjacente(Adjacente(evora, 131))

    # Porto
    porto.adicionar_adjacente(Adjacente(viana_do_castelo, 71))
    porto.adicionar_adjacente(Adjacente(vila_real, 116))
    porto.adicionar_adjacente(Adjacente(viseu, 133))
    porto.adicionar_adjacente(Adjacente(aveiro, 68))
    porto.adicionar_adjacente(Adjacente(braga, 53))

    # Santarém
    santarem.adicionar_adjacente(Adjacente(evora, 117))
    santarem.adicionar_adjacente(Adjacente(leiria, 70))
    santarem.adicionar_adjacente(Adjacente(lisboa, 78))

    # Setúbal
    setubal.adicionar_adjacente(Adjacente(beja, 142))
    setubal.adicionar_adjacente(Adjacente(evora, 103))
    setubal.adicionar_adjacente(Adjacente(faro, 249))
    setubal.adicionar_adjacente(Adjacente(lisboa, 50))

    # Viana do Castelo
    viana_do_castelo.adicionar_adjacente(Adjacente(braga, 48))
    viana_do_castelo.adicionar_adjacente(Adjacente(porto, 71))

    # Vila Real
    vila_real.adicionar_adjacente(Adjacente(viseu, 110))
    vila_real.adicionar_adjacente(Adjacente(braga, 106))
    vila_real.adicionar_adjacente(Adjacente(braganca, 137))
    vila_real.adicionar_adjacente(Adjacente(guarda, 157))
    vila_real.adicionar_adjacente(Adjacente(porto, 116))

    # Viseu
    viseu.adicionar_adjacente(Adjacente(aveiro, 95))
    viseu.adicionar_adjacente(Adjacente(coimbra, 96))
    viseu.adicionar_adjacente(Adjacente(guarda, 85))
    viseu.adicionar_adjacente(Adjacente(porto, 133))
    viseu.adicionar_adjacente(Adjacente(vila_real, 110))

    cidades = {1: aveiro,
               2: braga,
               3: braganca,
               4: beja,
               5: castelo_branco,
               6: coimbra,
               7: evora,
               8: faro,
               9: guarda,
               10: leiria,
               11: lisboa,
               12: portalegre,
               13: porto,
               14: santarem,
               15: setubal,
               16: viana_do_castelo,
               17: vila_real,
               18: viseu
               }

    def mostrar_cidades(self):
        for key, cidade in self.cidades.items():
            print(f'{key} - {cidade.nome}')

    def validar_key(self, key):
        return key in self.cidades.keys()

    def get_cidade_using_key(self, key):
        return self.cidades[key]


def get_menor_custo(lista):
     if lista:
        menor = lista[0]
        for i in range(len(lista)):
            print(f'{lista[i].vertice.nome}, {lista[i].distancia_aestrela}', end=' ')
            lista[i].vertice.visitado = True  # então agora foi visitado 
            if lista[i].distancia_aestrela < menor.distancia_aestrela:
                menor = lista[i]
        return menor


class AEstrela:
    # Definir destino e objetivo do algoritmo
    def __init__(self, destino):
        self.destino = destino
        self.encontrado = False  # Se o objetivo já foi atingido

    def buscar(self, cidade_atual):  # Cidade Atual: classe cidade
        print('\n')
        print('-' * 100)
        t.sleep(2)
        print(f'Estamos em: {cidade_atual.nome}')

        if cidade_atual == "Faro":
            print('Chegamos ao destino!!')
            self.encontrado = True
        else:
            comparar = []
            for adjacente in cidade_atual.adjacentes:
                comparar.append(adjacente)

            menor = get_menor_custo(comparar)
            cidade_atual.visitado = True
            
            if menor:
                self.buscar(menor.vertice)
        