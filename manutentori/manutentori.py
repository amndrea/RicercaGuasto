from tool import tool as t

# ----------------------------------------------------------------------------------------- #
class Manutentore:
    def __init__(self, nome, password):
        self.nome = nome
        self.password = password

class ListaManutentori:
    def __init__(self):
        self.Listamanutentori = []
# ----------------------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------------------- #
def is_presente(funz):
    """metodo decoratore che controlla che un manutentore non sia gia presente all'interno
    della lista dei manutentori, se non è gia presente lo aggiunge chiamando la funzione funz
    che è la funzione aggiungi_manutentore
    args[0] = lista di manutentori
    args[1] = nome del manutentore
    args[2] = password del manutentore """

    def wrapper(*args, **kwargs):
        lista = args[0]
        presente = False
        for elemento in lista:
            if str(elemento.nome).lower() == str(args[1]).lower():
                print("elemento con lo stesso nome trovato")
                presente = True
        if not presente:
            print("non presente, lo aggiungo")
            funz(*args, **kwargs)
        else:
            print("Manutentore gia presente all'interno della lista")
            return None
    return wrapper


@is_presente
def aggiungi_manutentore(L, user, password):
    """
    Metodo che crea un oggetto della classe manutentore e lo aggiunge alla lista
    :param L: lista di manutentori
    :param user: username del nuovo manutentore
    :param password: password del nuovo manutentore
    :return: None
    """
    nuovo_manutentore = Manutentore(user, password)
    L.append(nuovo_manutentore)


def carica_lista_manutentori(L):
    """
    Metodo che utilizzo per caricare la lista di manutentori da un file testuale
    Su ogni riga leggo un nome o una password, creo un oggetto della classe manutentore
    e lo aggiungo alla lista
    :param L: Lista di manutentori da caricare
    :return: Lista dei manutentori letta dal file
    """
    caporeparto = Manutentore("caporeparto", "caporeparto123")
    L.append(caporeparto)

    nome_file = t.create_path("lista_manutentori.txt")
    try:
        fd = open(nome_file, 'r')
        text = fd.readlines()
        i = 0
        j = len(text)
        while i < j:
            username = text[i].rstrip()
            password = text[i+1].rstrip()
            # manutentore_letto = Manutentore(username,password)
            aggiungi_manutentore(L, username,password)
            i = i + 2
    except FileNotFoundError:
        print("file non trovato il lettura, lo creo vuoto")
        fd = open(nome_file,'w')
        fd.close()
    except EOFError:
        print("generata eccezzione")
    except Exception:
        pass
# ----------------------------------------------------------------------------------------- #