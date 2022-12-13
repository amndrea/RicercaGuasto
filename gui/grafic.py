import PySimpleGUI as sg

layout_welcome=[[sg.Image(filename="logo.png")],
                [sg.Text("Effettuare il login ")],
                [sg.Text("Username"), sg.InputText(size=(65,10))],
                [sg.Text("Password"), sg.InputText(size=(65,10))],
                [sg.Button("Login")]
                ]

layout_loggato=[[sg.Image(filename="logo.png")],
                [sg.Text("Inserire un nuovo guasto                 "), sg.Button("Guasto")],
                [sg.Text("Ricerca tra i vecchi guasti              "), sg.Button("Ricerca")]
                ]

class gui:
    def __init__(self, tipo ):
        if tipo == "login":
            self.window = sg.Window("RicercaGuasto",layout_welcome,element_justification ='l', size=(740,680))
        if tipo == "utente_loggato":
            self.window = sg.Window("RicercaGuasto",layout_loggato,element_justification ='l', size=(740,680))
        