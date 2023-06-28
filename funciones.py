import os
import time 
import numpy

lisRut =[1111111]
lisNombre= ["pepe"]
lisIdentificador= [1]
lisNombreM =["julieta"]
cantDias= [5]


def find():
    ver= lisRut.index()
    print(lisNombre(ver))
    print(lisIdentificador(ver))
    print(lisNombreM(ver))
    cantDias(ver)


#guarderia= numpy.zeros (int(6,2))

def menu ():
    print ("""\t*MENU*
    1.Grabar 
    2.Buscar
    3.Retirarse
    4.Salir    
    """)
    opc = validar_opcion()
    return opc
def validar_opcion():
        while True:
            try:
                opcion = int(input("Ingrese opción: "))
                if opcion >= 1 and opcion <= 4:
                    return opcion
                else:
                    print("¡ERROR! ¡OPCIÓN INCORRECTA!")
            except:
                print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_rut():
    while True:      
        try:
            rut = input("Ingrese su RUT sin puntos ni dígito verificador: ")
            if len(str(rut)) == 7  or len(str(rut)) == 8:
                lisRut.append(rut)
                return rut
            else:
                print("¡ERROR! ¡INGRESE UN RUT VÁLIDO!")
        except:
            print("¡ERROR")
def validar_nombre():
    while True:
        x= 0
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha() and not nombre.isspace():
            lisNombre.append(nombre)
            lisIdentificador.append(x+1)
            print (lisIdentificador)
            return nombre
            os.system('cls')
        elif len (nombre.strip()) <3 and nombre.isalpha:
            print("Error ! El nombre debe contener como minimo 3 letras")
        else:
            print("ERROR!! contiene caracteres no validos!")
def validar_nombreMascota():
    while True:
        nombreM= input("Ingrese su nombre de la mascota: ")
        if len(nombreM.strip()) >= 3 and nombreM.isalpha() and not nombreM.isspace():
            lisNombreM.append(nombreM)
            return nombreM
            os.system('cls')
        elif len (nombreM.strip()) <3 and nombreM.isalpha:
            print("Error ! El nombre debe contener como minimo 3 letras")
        else:
            print("ERROR!! contiene caracteres no validos!")

def validar_identificar():
    while True:
        try:
            identificador = int(input("Ingrese su RUT sin puntos ni dígito verificador: "))
            if len(str(identificador)) == 1:
                identificador.append(identificador)
                return identificador
            else:
                print("¡ERROR! ¡INGRESE UN RUT VÁLIDO!")
        except:
            print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def CantDias():
    while True:
        try:
            dias = int(input("ingrese la cantidad de dias:"))
            if dias>0:
                cantDias.append(dias)
                return dias
            else:
                ("ERROR! respueta valida de 1 dia en adelante")
        except:
            print("ERROR!!respuesta no valida")

def retirarse():
    rutkill = validar_rut()
    indice = lisRut.index(rutkill)
    Ind= indice-1
    print(Ind)
    time.sleep(2)
    pago = cantDias(rutkill)
    lisRut.pop(Ind)
    lisNombre.pop(Ind)
    lisNombreM.pop(Ind)
    lisIdentificador.pop(Ind)
    print(pago)
