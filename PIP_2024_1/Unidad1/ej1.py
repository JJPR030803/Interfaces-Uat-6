
def bono():
 ingMens = int(input("Ingrese el promedio mensual"))
 numHorasFin = int(input("Ingrese el numero de horas trabajadas en fin de semana"))
 print("El bono es de :"+str(ingMens*0.01*numHorasFin))
 
bono()