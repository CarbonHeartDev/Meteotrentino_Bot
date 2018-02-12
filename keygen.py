from moduli.GestioneUtenti import GestioneUtenti
import os


position = os.getcwd()
gu=GestioneUtenti(position + '\\Dati\\Attivi\\utenti.json', position + '\\Dati\\Attivi\\chiaviMonouso.json')
print(position + '\\Dati\\Attivi\\chiaviMonouso.json')
