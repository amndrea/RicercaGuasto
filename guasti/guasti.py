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


def check_Decorator(funz):
    """metodo decoratore che controlla che ci siano tutti gli attributi di un guasto
    prima di aggiungerlo alla lista dei guasti
    args[0] = lista di guasti
    args[1] = tupla contenente tutti i campi di un guasto"""
    def wrapper(*args, **kwargs):
        (data, turno, reparto, manutentore, descrizione_problema, risoluzione, is_risolto) = args[1]
        if not data and turno and reparto and manutentore and descrizione_problema and risoluzione:
            print("mancano degli attributi")
            return False
        if turno.lower() not in ("mattina", "pomeriggio", "notte","m","p","n"):
            print("turno errato")
            return False
        if reparto.lower() not in ("mulini","presse", "smalterie","forni","squadrature", "scelte", "generale"):
            print("reparto errato")
            return False
        if is_risolto not in ('0','1'):
            print("risoluzione incompleta")
            return False
        # se arrivo qui vuol dire che tutti gli attributi inseriti sono per lo meno verosimili
        funz(*args, **kwargs)
    return wrapper
    
@check_Decorator
def AggiungiGuasto(L,par):
        data, turno, reparto, manutentore, descrizione_problema, risoluzione, is_risolto = par
        guasto = Guasto(data,turno,reparto,manutentore,descrizione_problema,risoluzione,is_risolto)
        L.append(guasto)


        

def carica_lista_guasti(L):
    """Metodo che utilizzo per caricare la lista guasti da un file testale
    Su ogni riga vado a leggere un dato relativo ad un guasto
    Creo un oggetto di tipo Guasto e lo aggiungo alla lista
    : param L: Lista di guasti da caricare
    : return: Lista di guasti letta dal file 
    """
    nome_file = t.create_directory("Guasti")


# ----------------------------------------------------------------------------------------- #
