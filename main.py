from manutentori.manutentori import ListaManutentori as List
from manutentori.manutentori import aggiungi_manutentore as add
from manutentori.manutentori import carica_lista_manutentori as load

if __name__ == '__main__':
    # creo una lista di manutentori
    lista = List()

    # carico la lista di manutentori
    load(lista.Listamanutentori)

    add(lista.Listamanutentori,"andrea","bonfatti")

    print(len(lista.Listamanutentori))


