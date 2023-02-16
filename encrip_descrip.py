from ast import Return


print("** ENCRIPTACION DE DESENCRIPTACION DE UN CARACTER **\n")
letras=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ")
letra=input("Ingresa la letra: ")
clave=int(input("Digita el parametro clave: "))
letra_mayus = letra.upper()

def encriptar_caracter(letra_mayus, clave):
    if letra_mayus in letras:
        ind=letras.index(letra_mayus)
        operacion=(ind+clave)%len(letras)
        letraConver=letras[operacion]
        return(letraConver)

print()
print("Caracter encriptado: ",encriptar_caracter(letra_mayus, clave))

caracter_encriptado=encriptar_caracter(letra_mayus, clave)
def desencriptar_caracter(caracter_encriptado,clave):
    if caracter_encriptado in letras:
        ind=letras.index(caracter_encriptado)
        operacion=(ind-clave)%len(letras)
        letra_desen=letras[operacion]
        return(letra_desen)

print("Caracter desencriptado: ",desencriptar_caracter(caracter_encriptado,clave))

# ------------------------------------------------------------------------
print()
print("** ENCRIPTACION DE DESENCRIPTACION DE UN MENSAJE **\n")
# ------------------------------------------------------------------------

mensaje=input("Digita un mensaje: ")
clave_B=int(input("Digita el parametro clave: "))
mensaje_mayus=mensaje.upper()
li=[]
mensaje_encriptado=[]
mensaje_desencriptado=[]

def encriptar(mensaje_mayus,clave_B):
    for i in range(0,len(mensaje_mayus)):
        li.append(mensaje_mayus[i])
        if li[i] in letras:
            ind=letras.index(mensaje_mayus[i])
            operacion=(ind+clave_B)%len(letras)
            mensaje_conver=letras[operacion]
            mensaje_encriptado.append(mensaje_conver)
    return(mensaje_encriptado)

print("Mensaje encriptado: ",encriptar(mensaje_mayus,clave_B))

def desencriptar(mensaje_encriptado,clave_B):
    for i in range(0,len(mensaje_encriptado)):
        li.append(mensaje_encriptado[i])
        if li[i] in letras:
            ind=letras.index(mensaje_encriptado[i])
            operacion=(ind-clave_B)%len(letras)
            mensaje_conver=letras[operacion]
            mensaje_desencriptado.append(mensaje_conver)
    return(mensaje_desencriptado)

print("Mensaje desencriptado: ",desencriptar(mensaje_encriptado,clave_B))