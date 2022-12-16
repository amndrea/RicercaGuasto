import os
import platform



def create_path(nomefile):
    """
    Metodo che utilizzo per lavorare con file nella direcrtory corrente
    :param nomefile: file ca creare/cercare
    :return: percoso della directory corrente + nome del file
    """
    s = (os.path.realpath(__file__))
    i = len(s)
    sistem = platform.system()
    if sistem == "Linux":
        while s[i - 1] != '/': i = i - 1
    elif sistem == "Windows":
        while s[i - 1] != '\\': i = i -1
    s = s[0:i]
    return s + nomefile

def create_directory(nomedir):
    """
    Metodo che utilizzo per verificare l'esistenza o creare una directory contenente
    i file relativi ai guasti
    :param nomedir: nome della directory contenente i file relativi ai guasti
    """
    s = (os.path.realpath(__file__))
    i = len(s)
    sistem = platform.system()

    if sistem == "Linux":
            while s[i - 1] != '/': i = i - 1
    if sistem == "Windows":
         while s[i - 1] != '\\': i = i - 1
    s = s[0:i]
    s = s+nomedir

    # Se la directory non esiste la creo
    if not os.path.exists(s):
        os.makedirs(s)
    return s

    
    
