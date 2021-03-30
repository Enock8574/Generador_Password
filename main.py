#Generador de contraseñas
import  random
print("----------*Enoc Carrera ©2021*---------")
#Arreglos con caracteres , numeros y simbolos
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
contra_array = []
contraseña = ""
#Comenzamos a solicitar datos al usuario
print(u"\U0001F512" "Generador de contraseñas "u"\U0001F512")
#Variables que luego almacenaremos en un arreglo
num_letras = int(input("Cuantas letras desea colocarle a su contraseña: \n"))
num_numeros = int(input(("Cuantos numeros le pondra a su contraseña: \n")))
num_simbolo = int(input(("Cuantos simbolos tendra su contraseña: \n")))
#Estos ciclo lo que van a hacer es añadir de manera dinamica la cantidad de letra,numero y simbolos que desee el usuario
#Esto se guardara en la variable contra_array[]
for i in range(1,num_letras,+1):
    contra_array += random.choice(letters)
for i in range(1,num_numeros,+1):
    contra_array += random.choice(numbers)
for i in range(1,num_simbolo,+1):
    contra_array += random.choice(symbols)
#Aqui mezclamos todos los caracteres del contra_array[] usando la funcion shuffle
random.shuffle(contra_array)
#Guardamos el contenido de contra_array en una variable para que muestra la contraseña del usuario en una cadena string
for caracter in contra_array:
    contraseña += caracter
#Imprimimos la contraseña del usuario
print(f"Su nueva contraseña es: {contraseña} por favor guarde bien su nueva contraseña")