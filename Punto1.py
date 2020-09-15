def saberEdad(edad,anio):
    respueta=edad+(2070-anio)
    #print(f"{respueta}")
    return respueta
def main():
    print("Bienvenido al programa de la Edad")
    edad =-1
    while edad<0 or edad>105:
        edad=int(input("por favor ingrese su edad:  "))

    anio =-1
    while anio<0 or anio>2070:
        anio=int(input("por favor el año actual:  "))

    saberEdad(edad,anio)
if __name__ == '__main__':
    main()