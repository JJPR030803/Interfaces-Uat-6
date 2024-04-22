class fileFunc:
    def prueba():
        print("hola mundo")
    def abrirArchivo(archivo):
       lista = []
       archivo = open("ejemplos.csv","r")
       for linea in archivo:
        lista.append(linea)
       return lista
    def escribirArchivo(archivo,lista):
        with open(archivo,'w',newline="\n") as file:
         for persona in lista:
            for caracteristica in persona:
                file.write(str(caracteristica)+"\n")