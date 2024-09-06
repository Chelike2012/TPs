import os.path
from Envio import Envio






#Metodos para validar direccion

def determina_tipo_envio(envios):
    vector_envios = 7 * [0]
    control=determina_control()
    if control == 'Hard Control':
        for i in range(len(envios)):
            direccion = envios[i].direccion
            if validez_direccion_hc(direccion):
                vector_envios[envios[i].tipo_envio] += 1
    else:
        for i in range(len(envios)):
            direccion = envios[i].direccion
            if validez_direccion_sc(direccion):
                vector_envios[envios[i].tipo_envio] += 1
    print(vector_envios)
def determina_control():
    texto=open("envios-tp3.txt","rt")
    linea = texto.readline()

    aparece_h = False
    aparece_s = False
    for c in linea:
        c = c.upper()
        if c == 'H':
            aparece_h = True
        else:
            if aparece_h and c == 'C':
                return 'Hard Control'
            else:
                aparece_h = False
        if c == 'S':
            aparece_s = True
        else:
            if aparece_s and c == 'C':
                return 'Soft Control'
            else:
                aparece_s = False
    return 'Soft Control'

def es_digito(caracter):
    car = ord(caracter)
    if 48 <= car <= 57:
        return True
    else:
        return False

def es_mayuscula(caracter):
    car = ord(caracter)
    if 65 <= car <= 90:
        return True
    else:
        return False
def es_minuscula(caracter):
    car = ord(caracter)
    if 97 <= car <= 122:
        return True
    else:
        return False

def validez_direccion_hc(direccion):
    encontre_mayuscula = False
    direccion_valida = False
    palabra_con_solo_digitos = True
    contiene_solo_digitos = False
    letras = 0
    for car in direccion:
        if car == '.' or car == ' ':
            if letras > 0 and contiene_solo_digitos:
                palabra_con_solo_digitos = True
            if car == '.' and palabra_con_solo_digitos and direccion_valida:
                return True
            encontre_mayuscula = False
            palabra_con_solo_digitos = True
            contiene_solo_digitos = False
            letras = 0

        else:
            letras += 1
            if es_digito(car) == False and palabra_con_solo_digitos:
                palabra_con_solo_digitos = False
            if es_mayuscula(car):
                if encontre_mayuscula:
                    return False
                else:
                    encontre_mayuscula = True
            else:
                encontre_mayuscula = False
            if es_mayuscula(car) or es_minuscula(car) or es_digito(car):
                direccion_valida = True
            else:
                return False

def validez_direccion_sc(direccion):
    if direccion:
        return True
    else:
        return False


#Metodos para clasificacion de envios

def define_pais(codigo_postal):
    cp=len(codigo_postal)
    if cp < 4 or cp > 9:
        return "Otro"
    if cp == 4 and codigo_postal.isdigit():
        return "Bolivia"
    if cp == 5 and codigo_postal.isdigit():
        return "Uruguay"
    if cp == 6 and codigo_postal.isdigit():
        return "Paraguay"
    if cp == 7 and codigo_postal.isdigit():
        return "Chile"
    if cp == 8:
        if cp[0].isalpha() and cp[0] not in 'IO' and cp[1:5].isdigit() and cp[5:8].isalpha():
            return 'Argentina'
        else:
            return 'Otro'
    if cp == 9:
        if cp[0:5].isdigit() and cp[5] == '-' and cp[6:9].isdigit():
            return 'Brasil'
        else:
            return 'Otro'

    return 'Otro'

def calcula_tipo_envio(tipo_envio):
    precios_base=[1100,1800,2450,8300,10900,14300,17900]
    precio=precios_base[tipo_envio]
    return precio


def monto_final_envio(codigo_postal, pais, precio_base, forma_pago):


    if pais == 'Argentina':
        total = precio_base
    else:
        if pais == 'Bolivia' or pais == 'Paraguay' or (pais == 'Uruguay' and codigo_postal[0] == '1'):
            total = int(precio_base * 1.20)
        elif pais == 'Chile' or (pais == 'Uruguay' and codigo_postal[0] != '1'):
            total = int(precio_base * 1.25)
        elif pais == 'Brasil':
            if codigo_postal[0] == '8' or codigo_postal[0] == '9':
                total = int(precio_base * 1.20)
            else:
                if codigo_postal[0] == '0' or codigo_postal[0] == '1' or codigo_postal[0] == '2' or codigo_postal[0] == '3':
                    total = int(precio_base * 1.25)
                else:
                    total = int(precio_base * 1.30)
        else:
            total = int(precio_base * 1.50)

    precio_final = total

    if forma_pago == 1:
        precio_final = int(0.9 * precio_base)
    return precio_final


def determina_tipo_envio(envios):
    vector_envios = 7 * [0]
    control=determina_control()
    if control == 'Hard Control':
        for i in range(len(envios)):
            direccion = envios[i].direccion
            if validez_direccion_hc(direccion):
                vector_envios[envios[i].tipo_envio] += 1
    else:
        for i in range(len(envios)):
            direccion = envios[i].direccion
            if validez_direccion_sc(direccion):
                vector_envios[envios[i].tipo_envio] += 1
    print(vector_envios)

# Metodos para realizar las validaciones

def valida_codigo_postal():
    cp=str(input("Ingrese el codigo postal (maximo 9 caracteres): "))
    while len(cp) > 9:
        print("El codigo postal es muy largo")
        cp = str(input("Ingrese el codigo postal (maximo 9 caracteres): "))
    return cp
def valida_direccion():
    direc=str(input("Ingrese la direccion (maximo 20 caracteres): "))
    while len(direc) > 20:
        print("La direccion es muy larga")
        direc = str(input("Ingrese la direccion (maximo 20 caracteres): "))
    return direc

def valida_tipo_envio():
    tipo = int(input("Ingrese el tipo de envio (entre 0 y 6): "))
    while tipo < 0 or tipo > 6:
        print("Tipo de envio incorrecto")
        tipo = int(input("Ingrese el tipo de envio (entre 0 y 6): "))
    return tipo

def valida_forma_pago():
    pago = int(input("Ingrese la forma de pago (1(efectivo) 2(credito) ): "))
    while pago < 1 or pago >2:
        print("Forma de pago incorrecta")
        pago = int(input("Ingrese la forma de pago (1(efectivo) 2(credito) ): "))
    return pago

#Metodos para listar

def listar_envios(envios):
    print("Desea listar ¿Todos los envios o una cantidad definida?")
    opcion = int(input("Seleccione (1.Todos o 2.Cantidad definida) : "))
    while opcion < 0 or opcion > 2:
        print("Opcion incorrecta")
        opcion = int(input("Seleccione (1.Todos o 2.Cantidad definida) : "))
    if opcion == 1:
        listar(envios)
    else:
        cantidad=int(input("Ingrese la cantidad de registros a visualizar : "))
        listar_por_cantidad(envios,cantidad)

def listar(vector):
    print("-" * 47)
    for x in vector:
        print(x)
    print("-" * 47)

def listar_por_cantidad(envios,cantidad):
    n=cantidad
    if len(envios) < n:
        n=len(envios)
    print("-" * 47)
    for x in range(n):
        print(envios[x])
    print("-" * 47)


#Metodos de ordenamiento
def ordenar_codigo_postal(envios):
    n = len(envios)
    for i in range(n-1):
        for j in range(i+1, n):
            if envios[i].codigo_postal > envios[j].codigo_postal:
                envios[i], envios[j] = envios[j], envios[i]


#Metodos de busqueda
def busqueda_direccion_tipo(envios):
    direccion = valida_direccion()
    tipo_envio = valida_tipo_envio()
    resultado=buscar_direccion_tipo_envio(envios,direccion,tipo_envio)
    print(resultado)


def buscar_direccion_tipo_envio(envios,direccion,tipo_envio ):

 for i in range(len(envios)):
    if envios[i].direccion == direccion:
        if envios[i].tipo_envio == tipo_envio:
            return envios[i]
 return "No existe ningun envio con esa direccion y tipo de envio."

def busqueda_cp_cambia_forma_pago(envios):
    codigo_postal = valida_codigo_postal()
    resultado,envios=buscar_cp_cambia_forma_pago(envios,codigo_postal)
    print(resultado)
    return envios


def buscar_cp_cambia_forma_pago(envios,codigo_postal):

    for i in range(len(envios)):
       if envios[i].codigo_postal == codigo_postal:
           if envios[i].forma_pago == 1:
               envios[i].forma_pago = 2
           elif envios[i].forma_pago == 2:
               envios[i].forma_pago = 1
           return envios[i],envios
    return "El codigo postal no existe",envios


#Metodos para carga de datos en arreglos
def cargar_objetos_txt(archivo):
    envios = []
    texto=open(archivo,"rt")
    linea = texto.readline()
    while True:
        linea = texto.readline()

        if linea == '':
            break

        if linea[-1] == "\n":
            linea = linea[0:-1]

        codigo_postal = linea[0:9].strip().upper()
        direccion = linea[9:29].strip()
        tipo_envio = int(linea[29])
        forma_pago = int(linea[30])

        envio = Envio(codigo_postal, direccion, tipo_envio, forma_pago)
        envios.append(envio)
        print(envio)
    texto.close()
    return envios

def carga_arreglo(envios):
    opcion = 0
    archivo = "envios-tp3.txt"

    if not os.path.exists(archivo):
        print("El archivo no se encuentra cargado. Revise e ingrese nuevamente a esta opcion")
    else:
        print ("Se realizará la carga de datos en el arreglo \nSi tiene datos antiguos será borrados ")
        opcion = int(input("¿Desea continuar? \nIngrese 1(Sí) o 2(No) : "))
        if opcion == 1:
            print("Se comienza con la carga.....")
            envios=cargar_objetos_txt(archivo)
            listar(envios)
            return envios
        else:
            pass


def carga_envio_manual(envios):
    codigo_postal = valida_codigo_postal()
    direccion = valida_direccion()
    tipo_envio = valida_tipo_envio()
    forma_pago = valida_forma_pago()
    envio = Envio(codigo_postal, direccion, tipo_envio, forma_pago)
    envios.append(envio)
    return envios





def principal():
    opcion=1
    envios=[]

    while opcion!= 11:
        print("\n***************************************************\n")
        print("Menu de opciones: ")
        print("1. Cargar envios por txt")
        print("2. Cargar envios por teclado")
        print("3 . Ordenar por codigo postal y listar")
        print("4 . Buscar por direccion y tipo de envio")
        print("5 . Buscar por codigo postal y cambia forma de pago")
        print("6 . Determinar cantidad de envios de direcciones validas ")
        print("10. Listar")



        opcion=int(input("Seleccione una opcion: "))

        if opcion == 1:
            envios=carga_arreglo(envios)
        if opcion == 2:
            envios=carga_envio_manual(envios)
        if opcion == 3:
            ordenar_codigo_postal(envios)
            listar_envios(envios)
        if opcion == 4:
            busqueda_direccion_tipo(envios)
        if opcion == 5:
            envios=busqueda_cp_cambia_forma_pago(envios)
        if opcion == 6:
            determina_tipo_envio(envios)
        if opcion == 10:
            listar(envios)

    print("El programa ha terminado")

if __name__ == '__main__':
    principal()