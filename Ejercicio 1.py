import os 
'''Una transportadora requiere el desarrollo de una aplicacion  que permita llevar un registro de los despachos
de sus vehiculos teniendo en cuenta lo siguiente placa del vehiculo
-descripcion
-nombre del conductor 
-contacto
-ruta 
-descripcion de la carga
;el numero de despacho se genera de forma automatuica, es decir una variable que incremente,dicha 
informacion debe quedar registrada en un diccionario:
registro de salida y mostrar salida'''
diccionario_carga= {}
despacho = 0
def fnt_selectorr(op):
    global control  
    if opcion == '0':
        control = False
    elif opcion == '1':
        fnt_despacho()
    elif opcion == '2':
        fnt_consutar(diccionario_carga)
def fnt_consutar(diccionario_carga):
    global despacho
    print('Registro actual')  
    print('Cantidad de despachos:',despacho)
    for key, value in diccionario_carga.items():
        print(f'Nombre del conductor: {key}')
        print(f'{value}')
    input('')
def fnt_despacho():
    global despacho
    fnt_pantalla()
    #Se le piden los datos al conductor 
    placa= input('Placa del vehiculo:')
    descripcion = input('Descripcion del vehiculo:')
    nombredelconductor = input('Nombre del conductor:')
    contacto=input('Contacto:')
    ruta = input('Ruta:')
    descripciondelacarga = input('Descripcion de la carga:')
    if placa =='' or descripcion ==''  or nombredelconductor == '' or contacto== '' or ruta== '' or descripciondelacarga  == '':
        input('Por favor rellene todos los datos corectamente')
    else:
        diccionario_carga [nombredelconductor] ={'Placa':placa,'Descripcion':descripcion,'Nombre del conductor':nombredelconductor,'Contacto':contacto,'Ruta':ruta,'Descripcion de la carga':descripciondelacarga}
        despacho += 1
    

def fnt_pantalla():
    os.system('cls')
   
control = True

while control == True:
    fnt_pantalla()
    print('<<<<<<<<<<<<<Registro de vehiculos>>>>>>>>>>>>>>>')
    opcion = input('Exportadora cargoBan \nMenu de opcioneS\nQue desea hacer?\n0.Salir\n1.Registrar\n2.Consultar\n---->:')
    fnt_selectorr(opcion)
    