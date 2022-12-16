from manutentori.manutentori import Manutentore as m
from manutentori.manutentori import ListaManutentori as List_M
from manutentori.manutentori import aggiungi_manutentore as add
from manutentori.manutentori import carica_lista_manutentori as load_m
from guasti.guasti import ListaGuasti as Lista_G
from guasti.guasti import carica_lista_guasti as load_g
from guasti.guasti import AggiungiGuasto as add_g
from gui.grafic import App

if __name__ == '__main__':
    # creo una lista di manutentori e di guasti
    lista_m = List_M()
    lista_g = Lista_G()

    # carico le liste di manutentori e guasti
    load_m(lista_m.Listamanutentori)
    load_g(lista_g.Listaguasti)

    App(lista_m, lista_g)
    

