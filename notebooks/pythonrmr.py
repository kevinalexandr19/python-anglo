# RQD
def rqd(dato):
    if 90 < dato:
        return 20
    elif 75 < dato <= 90:
        return 17
    elif 50 < dato <= 75:
        return 13
    elif 25 < dato <= 50:
        return 8
    elif dato <= 25:
        return 3

# Espaciamiento
def espaciamiento(dato):
    if dato > 2000:
        return 20
    elif 600 < dato <= 2000:
        return 15
    elif 200 < dato <= 600:
        return 10
    elif 60 < dato <= 200:
        return 8
    elif dato <= 60:
        return 5    

# Resistencia
def resistencia(dato):
    if dato == "R6":
        return 15
    elif dato == "R5":
        return 12
    elif dato == "R4":
        return 7
    elif dato == "R3":
        return 4
    elif dato == "R2":
        return 2
    elif dato == "R1":
        return 1
    elif dato == "R0":
        return 0    
    
# Apertura
def apertura(dato):
    if dato == "A0":
        return 6
    elif dato == "A1":
        return 5
    elif dato == "A2":
        return 3
    elif dato == "A3":
        return 1
    elif dato == "A4":
        return 0    

# Rugosidad
def rugosidad(dato):
    if dato == "G1":
        return 6
    elif dato == "G2":
        return 5
    elif dato == "G3":
        return 3
    elif dato == "G4":
        return 1
    elif dato == "G5":
        return 0
    
# Relleno
def relleno(dato):
    if dato == "F0":
        return 6
    elif dato == "F1":
        return 4
    elif dato == "F2":
        return 2
    elif dato == "F3":
        return 1
    elif dato == "F4":
        return 0    
    
# Alteración
def alteracion(dato):
    if dato == "W0":
        return 6
    elif dato == "W1":
        return 5
    elif dato == "W2":
        return 3
    elif dato == "W3":
        return 1
    elif dato == "W4":
        return 0  
    
# Persistencia (promedio de apertura, rugosidad, relleno y alteración)

# Agua = 15

# Calidad RMR
def calidad(dato):
    if 80 < dato:
        return "Muy buena"
    elif 60 < dato <= 80:
        return "Buena"
    elif 40 < dato <= 60:
        return "Media"
    elif 20 < dato <= 40:
        return "Mala"
    elif dato <= 20:
        return "Muy mala"