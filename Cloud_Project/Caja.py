'''
Unidad 3: Programación Orientada a objetos
Tema: 1.1 Clases y objetos
Fecha: 28 de septiembre del 2022
Autor: Leonardo Martínez González

Clases y objetos en Python : https://www.youtube.com/watch?v=aj4PEXq0zuc
'''
import random

'''
Sumar y restar dias a la fecha: https://j2logo.com/operaciones-con-fechas-en-python/
Generar numeros aleatorios: https://j2logo.com/python/generar-numeros-aleatorios-en-python/
Código ASCII:  https://elcodigoascii.com.ar/
Convertir un INT a ASCII: https://www.delftstack.com/es/howto/python/python-int-to-ascii/
Descargue la libreria bcrypt con el comando: "pip install bcrypt"

Realizar una clase llamada Password que siga las siguientes condiciones:
▪ Que tenga los atributos longitud, contraseña y fecha_expiracion. Por defecto, la longitud sera de 8, la contraseña
  será los números del 1 al 8 y la fecha_expiración será de UN día.

▪ Un constructor con la contraseña y fecha_expiracion que nosotros le pasemos, se calculará la longitud de la contrasena

Generará una contraseña aleatoria con esa longitud.

▪ Los métodos que implementa serán:
▪ esFuerte(): devuelve un booleano si es fuerte o no, para que sea fuerte debe tener mas de 2 mayúsculas, al menos una
minúscula y al menos  1 caracter.

▪ generarPassword(): genera la contraseña del objeto con la longitud que tenga.

▪ cifraPassword(): cifra la contraseña del objeto.

▪ verificarClave: regresará verdadero si la contrasena es correcta.

▪ Método get para contraseña y longitud.

▪ Método set para longitud.

Ahora, crea una clase clase ejecutable(main):
▪ Crea un array de Passwords con el tamaño que tu le indiques por teclado.
▪ Crea un bucle que cree un objeto para cada posición del array.
▪ Indica también por teclado la longitud de los Passwords (antes de bucle).
▪ Crea otro array de booleanos donde se almacene si el password del array de Password es o no fuerte (usa el bucle anterior).
▪ Al final, muestra la contraseña y si es o no fuerte (usa el bucle anterior). Usa este simple formato:
contraseña1 valor_booleano1
contraseña2 valor_bololeano2
'''
import bcrypt
import  datetime
class Password:
    #Contructor
    def __init__(self, longitud=12, contrasena="1234567"):
        self.longitud=len(contrasena)
        self.contrasena=contrasena
        self.fecha_expiracion=datetime.timedelta(days=1)
        self.contrasena_sifrada=self.cifrar_contrasena(contrasena)
    def __str__(self):
        return f"Contraseña: {self.contrasena} Contraseña sifrada: {self.contrasena_sifrada}"
    def generar_password(self):
        clave=""
        print("Generar clave.............")
        for i in range(self.longitud):
#generara numeros aleatorio
            numero=random.randint(1,4)
            if numero==1:
                clave+=self.generara_mayuscula()
            elif numero==2:
                clave += self.generara_minusculas()
            elif numero==3:
                clave += str(self.generara_numeros())
            elif numero==4:
                clave += self.generara_caracteres()
            self.contrasena=clave
            self.contrasena_sifrada=self.cifrar_contrasena(clave)
    #generar letras mayusculas de forma aleatoria
    def generara_mayuscula(self):
        return  chr(random.randint(65,98))
    def generara_minusculas(self):
        return  chr(random.randint(97,122))
    def generara_numeros(self):
        return random.randint(0, 9)
    def generara_caracteres(self):
        list=['?','*','$','&','#','.','¡','%']
        return list[random.randint(0,7)]

    def cifrar_contrasena(self,contrasena):
        sal = bcrypt.gensalt()  # Default time 2 secons
        contrasena_sifrada = bcrypt.hashpw(contrasena.encode("utf-8"), sal)
        return contrasena_sifrada
    # def defifrar(self,claveS,claveN):
    #     return bcrypt.checkpw(claveN.encode("utf-8"),claveS)
        # Verificar la cuenta
    def autenticar_cuenta(self, clave):
        return bcrypt.checkpw(clave.encode('utf-8'), self.contrasena_cifrada)
    def es_fuerte(self):
        contador_mayuscula=0
        contador_minuscula=0
        contador_caracter=0
        contador_numero=0
        for car in self.contrasena:
            if ord(car)>=65 and ord(car)<=90: #letra matuscula
                contador_mayuscula+=1
            elif ord(car)>=97 and ord(car)<=122: #letra minuscula
                contador_minuscula+=1
            elif ord(car)>=48 and ord(car)<=57: #letra numero
                contador_numero+=1
            else:
                contador_caracter+=1
        if contador_mayuscula>=2 and contador_minuscula>=1 and contador_caracter>=1:
            return True
        return False

def app():
    pws=[]
    arr_fuertes=[]
    numero_de_elemetos=int(input("Dame cuantos elementos quieres: "))
    longitud = int(input("Dame la longuitud: "))
    for i in range(numero_de_elemetos):
        objPassword=Password()
        objPassword.longitud=longitud
        objPassword.generar_password()
        pws.append(objPassword)
        arr_fuertes.append(objPassword.es_fuerte())
    for i in range(numero_de_elemetos):
        print(pws[i].contrasena,arr_fuertes[i])
#app()
# objPassword=Password()
# print(objPassword)
# print(objPassword.es_fuerte())
# objPassword.generar_password()
# print(objPassword)
# print(objPassword.es_fuerte())

# print(objPassword.fecha_expiracion)
#
# print("la clave es : hola")
# clave=objPassword.cifrar_contrasena("hola")
# print(f"La clave sifrada es:{clave}")
# print(objPassword.defifrar(clave,"hola"))


