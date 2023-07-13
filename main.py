# img_viewer.py
import tkinter as sg
# import PySimpleGUI as sg
import os
from tables import evaluateTables, loadDataTables, saveDataTables
import csv


saveDataTables(0, 15) # create file .data.csv with tables data
NT_BUSY, NT_FREE = loadDataTables() # load needed data from .data.csv

# check if file of booking already exists
def fileBookingExist():
    return os.path.exists("booking.csv")

if not fileBookingExist():
    with open('booking.csv','w'):
        pass

# load data from booking file
def loadBookingValues():
    values = []
    with open('booking.csv','r') as csvfile:
        #reader can iterate over lines of csv file
        csvreader = csv.reader(csvfile)
        #reading rows
        for row in csvreader:
                values.append(row)
    return values
    

file_list_column = [
    [
        sg.Text("Numero tavoli disponibili: 15"),
    ],
    [
        sg.Text("Numero persone"),
        sg.In(size=(15, 1), enable_events=True, key="-NP-"),
        sg.Button("CONTROLLA")
    ],
    [
        sg.Text("Numero tavoli occupati:{}".format(NT_BUSY), key="-NT_BUSY-"),
        sg.Text("Numero tavoli liberi:{}".format(NT_FREE), key="-NT_FREE-"),
    ],
    [
        sg.HSeparator(),
    ],
    [
        sg.Text("Numero persone"),
        sg.In(size=(15, 1), enable_events=True, key="-NP2-"),
        sg.Text("Ora"),
        sg.In(size=(15, 1), enable_events=True, key="-HOUR-"),
        sg.Text("Nome"),
        sg.In(size=(15, 1), enable_events=True, key="-NAME-"),
        sg.Text("Telefono"),
        sg.In(size=(15, 1), enable_events=True, key="-PHONE-"),
        sg.Button("INSERISCI"),
    ],
]


headings = ["Numero persone", "Orario", "Nome", "Telefono"]
valuesTable=loadBookingValues()

booking_column = [
    [
        sg.Table(values=valuesTable, headings=headings, key="-BOOKING_TABLE-")
    ]
]
    
# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(booking_column)
    ]
]

window = sg.Tk()
# window = sg.Window("Booking Tables App", layout)


# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-NP-":
        window['-NP2-'].update(values['-NP-'])
    if event == "CONTROLLA":
        NT_BUSY, NT_FREE = evaluateTables(int(values["-NP-"]))
        window['-NT_BUSY-'].update("Numero tavoli occupati:{}".format(NT_BUSY))
        window['-NT_FREE-'].update("Numero tavoli liberi:{}".format(NT_FREE))
    if event == "INSERISCI":
        NT_BUSY, NT_FREE = evaluateTables(int(values["-NP-"]), True)
        window['-NT_BUSY-'].update("Numero tavoli occupati:{}".format(NT_BUSY))
        window['-NT_FREE-'].update("Numero tavoli liberi:{}".format(NT_FREE))
        valuesTable.append([values["-NP-"], values["-HOUR-"], values["-NAME-"], values["-PHONE-"]])
        window['-BOOKING_TABLE-'].update(values=valuesTable)
        with open("booking.csv", 'a') as f:
            f.write("{},{},{}, {}\n".format(values["-NP-"], values["-HOUR-"], values["-NAME-"], values["-PHONE-"]))
window.close()