import PySimpleGUI as sg
from manutentori.manutentori import Manutentore as m

layout_welcome=[[sg.Image (filename='logo.png')],
                [sg.Text("Effettuare il login ", font = 22)],
                [sg.Text("Username", font=16), sg.InputText(size=(65,2), font=16), ],
                [sg.Text("Password", font=16), sg.InputText(size=(65,2), font=16 , password_char='*')],
                [sg.Button("Login", font=16)]
                ]

layout_loggato=[[sg.Image(filename="logo.png")],
                [sg.Text("Inserire un nuovo guasto                 ", font=16), sg.Button("Guasto", font=16)],
                [sg.Text("Ricerca tra i vecchi guasti              ", font=16), sg.Button("Ricerca", font=16)]
                ]

layout_caporeparto=[[sg.Image(filename="logo.png")],
                [sg.Text("Inserire un nuovo guasto                 ", font=16), sg.Button("Guasto", font=16)],
                [sg.Text("Ricerca tra i vecchi guasti              ", font=16), sg.Button("Ricerca", font=16)],
                [sg.Text("Inserisci un nuovo manutentore           ", font=16), sg.Button("Inserisci",font=16)]
                ]


layout_Insert=[ [sg.Image(filename= "logo.png")],
                [sg.Text("Turno                ", font=16), sg.OptionMenu(('Mattina','Pomeriggio','Notte'),size=(12,3))],
                [sg.Text("Reparto del guasto   ", font=16), sg.OptionMenu(('Mulini','Presse', 'Smalterie','Forni','Squadrature', 'Scelte', 'Generale'),size=(12,3))], 
                [sg.Text("Descrizione Probelma ", font=16), sg.InputText(size=(65,2), font=16)],
                [sg.Text("Risoluzione Problema ", font=16), sg.InputText(size=(65,2), font=16)],
                [sg.Text("Problema risolto?    ", font=16), sg.OptionMenu(("Si","No"),size=(2,2))],
                [sg.Text("                      "), sg.Button("Insrisci",font=16)]
                ]
# layout_caporeparto = [[sg.image]]


class gui:
    def __init__(self, tipo ):
        if tipo == "login":
            self.window = sg.Window("RicercaGuasto",layout_welcome,element_justification ='l', size=(740,680))
        if tipo == "utente_loggato":
            self.window = sg.Window("RicercaGuasto",layout_loggato,element_justification ='l', size=(740,680))
        if tipo == "Aggiungi":
            self.window = sg.Window("Aggiunta guasti", layout_Insert,element_justification ='l', size=(740,680))
        if tipo == "Aggiungi":
            pass

        

def App( lista_m, lista_g):
    window = gui("login")
    while True:
        event, values = window.window.read()
        if event == sg.WIN_CLOSED: 
            break
        if event == "Login":
            (user, password) = values[1], values[2]

        # controllo che siano inseriti entrambi i campi
            if user == '' or password == '':
                sg.Popup("Inserire tutte le credenziali")
            
            # controllo che siano le credenziali del caporeparto
            if user == 'caporeparto':
                if password == 'caporeparto':
                    print("faccio il login da caporeparto")
                else:
                    sg.Popup()

            # controllo che sia un account esistente 
            if lista_m.esistente(user,password):
                    window2 = gui("utente_loggato")
                    window, window2 = window2, window
                    window2.window.close()
            else:
                sg.Popup("username o password errati")
        
        if event == "Guasto":
            window2 = gui("Aggiungi")
            window, window2 = window2, window
            window2.window.close()
            
        if event == "Insrisci":
            (turno, reparto,descrizione,risoluzione, risolto) = values[1],values[2],values[3],values[4],values[5]

            """ QUI TENTO DI AGGIUNGERE UN GUASTO ALLA LISTA E SALVO IL GUSTO SU UN FILE
            DEVO AGGIUNGERE ANCHE LA DATA ODIERNA E IL MANUTENTORE AL NOME DEL MANUTENTORE
            ATTUALE """ 
            print(turno)
            print(reparto)
            print(descrizione)
            print(risoluzione)
            print(risolto)
        
        if event == "Cerca":
            pass


        