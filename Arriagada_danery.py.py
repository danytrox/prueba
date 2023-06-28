import funciones as fn



#MENU 
opc = fn.menu()
print (opc )
if opc == 1:
    fn.validar_rut() #segun ejercicio validar que sea entre 7 y 8 = 7.5 digitos
    fn.validar_nombre()
    fn.validar_nombreMascota()
    fn.CantDias()
if opc == 2:
    fn.validar_rut()
if opc == 3:
   fn.retirarse()
if opc == 4:
    exit
