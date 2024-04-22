import csv
listaNombres = [
    ["Clemente",26],
    ["Cristobal",17],
    ["Ana",24],
    ["Rene",54],
    ["Orozco",36],
    ["Jorge",24],
    ["Aquino",66],
    ["Badillo",68],
    ["Segoviano",69],
    ["Salazar",45],
    ["Eduardo",10],
    ["Rodrigo",65],
    ["Miguel",90],
    ["Amando",82],
    ["Raul",12],
    ["Lexis",13],
    ["Mariana",17],
    ["Angel",84],
    ["Emmanuel",29],
    ["Isaac",39],
    ["Paniagua",99],
    ["Sheko",30]
]

    
    
def abrirArchivo(archivo):
    archivo = open("ejemplos.csv","r")
    for linea in archivo:
     print(linea)
    
def esccribirArchivo(archivo,lista):
    with open(archivo,'w',newline="\n") as file:
     for persona in lista:
        for caracteristica in persona:
            file.write(str(caracteristica)+"\n")
            
