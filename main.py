from manutentori.manutentori import ListaManutentori as List_M
from manutentori.manutentori import aggiungi_manutentore as add
from manutentori.manutentori import carica_lista_manutentori as load_m
from guasti.guasti import ListaGuasti as Lista_G
from guasti.guasti import carica_lista_guasti as load_g
from guasti.guasti import AggiungiGuasto as add_g

if __name__ == '__main__':
    # creo una lista di manutentori
    lista_m = List_M()
    lista_g = Lista_G()

    # carico la lista di manutentori
    load_m(lista_m.Listamanutentori)
    load_g(lista_g.Listaguasti)

    add(lista_m.Listamanutentori,"andrea","bonfatti")
    add_g(lista_g.Listaguasti, ("11/10/2022","notte","presse","bonfi","non va un cazzo","spento e riacceso","1"))

    print(len(lista_m.Listamanutentori))
    print(len(lista_g.Listaguasti))

