from tool import tool as t

class Guasto:
    def __init__(self, data, turno, reparto, manutentore, descrizione_problema, risoluzione, isrisolto):
        self.data = data
        self.turno = turno
        self.reparto = reparto
        self.manutentore = manutentore
        self.descrizione_problema = descrizione_problema
        self.risoluzione = risoluzione
        self.isrisolto = isrisolto

class ListaGuasti:
    def __init__(self):
        self.Listaguasti = []

# ----------------------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------------------- #
def check_attributi_guasto(data, turno, reparto, manutentore, descrizione_problema, risoluzione, isrisolto):
    presenti = data and turno and reparto and manutentore and descrizione_problema and risoluzione
    if not presenti:
        print("Non ci sono tutti gli attributi")
        return False
    if turno.lower() not in ("mattina", "pomeriggio", "notte"):
        print("Turno errato")
        return False
    if reparto.lower() not in ("mulini","presse", "smalterie","forni","squadrature", "scelte", "generale"):
        print("reparto errato")
        return False
    if isrisolto not in ('0','1'):
        print("risoluzione incompleta")
        return False
    return True

def carica_lista_guasti():
    nome_file = t.create_path("listaguasti.txt")

# ----------------------------------------------------------------------------------------- #
