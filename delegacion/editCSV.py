#Script para editar csv y crear otro con un formato determinado

import csv

filename = "AO.csv"
header = ("Dirección de correo electrónico", "Escoge 2 de estas asignaturas")

filename2 = "resultados.csv"
header3 = ("Algoritmos genéticos y evolutivos", "Análisis de datos", "Inteligencia artificial en industria de entretenimiento", "Prácticas externas", "Programación orientada a objetos", "Computación Ubicua", "Desarrollo de software de sistemas", "Informática forense", "Panorámica de las comunicaciones digitales", "Accesibilidad y diseño para todos en ingeniería del software", "Equipos virtuales", "Gestión del conocimiento organizativo", "Redes de neuronas artificiales (solo para Computadores y Sistemas de Información)")

header2 = ("AGE", "AD", "IAIE", "PPEE", "POO", "CU", "DSS", "IF", "PCCDD", "ADIS", "EEVV", "GCO", "RNA")
dicHeader2 = {"AGE": 0, "AD":1, "IAIE":2, "PPEE":3, "POO":4, "CU":5, "DSS":6, "IF":7, "PCCDD":8, "ADIS":9, "EEVV":10, "GCO":11, "RNA":12}

data = []

for i in range(40):
    data.append((0,0,0,0,0,0,0,0,0,0,0,0,0))


def updater(filename):
    with open(filename, newline= "") as file:
        readData = [row for row in csv.DictReader(file)]
        for fila in readData:
            separaComas = fila[header[1]].split(', ')
            for seleccionada in separaComas:
                for asigantura in header2:       
                    if (asigantura == seleccionada):
                        insertar(asigantura, fila[header[0]])
                        break

def insertar(asignatura, NIA):
    for posicion, editar in enumerate(data):
        if (editar[dicHeader2[asignatura]] == 0):
            paraEditar = list(editar)
            paraEditar[dicHeader2[asignatura]] = NIA
            data[posicion] = tuple(paraEditar)
            break


def writer(header, data, filename):
  with open (filename, "w", newline = "") as csvfile:
    movies = csv.writer(csvfile)
    movies.writerow(header)
    for x in data:
      movies.writerow(x)

updater(filename)
writer(header3, data, filename2)