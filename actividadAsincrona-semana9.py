# mensaje de bien venida

print('''\nhola bien venido a nuestro programa
      
A continuacion te pediremos que ingreses unos datos favor de ingrsar los datos como sele piden ''')

#extracion de datos 
nombre = input("\npor favor ingrese su nombre: \n")
apellido = input("\npor favor ingrese su apellido: \n")
edad = int(input("\npor favor ingrese su edad numerica mente ejemplo (1,2,3,4,5,6,7...): \n"))
sexo = input("\npor favor ingrese su sexo a continuacion precione F para femenino (mujer) O precione M para masculino (hombre): \n")
# si la opcion que escoja el usuario es F (femenino) se mostrara cualquiera de las siguientes respuestas 

if sexo == "F" or sexo == "f":
    if edad <= 2:
        print(nombre, apellido,"usted esta en la etapa de bebe")
    elif edad >= 3 and edad <= 5:
        print(nombre, apellido, "usted esta en la etapa de infancia")
    elif edad >= 6 and edad <= 11:
        print(nombre, apellido, "ud esta en la etapa de la niñes.")
    elif edad >= 12 and edad <= 18:
        print(nombre, apellido, "usted esta en la etapa de la adolescencia.")
    elif edad >= 19 and edad <= 26:
        print(nombre, apellido, "usted esta en la etapa de la juventud.")
    elif edad >= 27 and edad <= 40:
        print(nombre, apellido, "usted esta en la etapa de la adultez joven.")
    elif edad >= 41 and edad <= 55:
        print(nombre, apellido, "usted esta en la etapa de la adultez.")
    elif edad >= 56 and edad <= 65:
        print(nombre, apellido, "ud esta en la etapa de la persona mayor.")
    else:
        print(nombre, apellido, "usted esta en la etapa de la tercera edad y vejez.")
        
        # si la opcion del usuario es H (hombre) se mostrara cualquiera de las siguientes respuestas 
else:
    if edad <= 2:
        print(nombre, apellido, "usted esta en la etapa de bebe")
    elif edad >= 3 and edad <= 5:
        print(nombre, apellido, "usted esta en la etapa de la infancia.")
    elif edad >= 6 and edad <= 11:
        print(nombre, apellido, "usted esta en la etapa de la niñes.")
    elif edad >= 12 and edad <= 18:
        print(nombre, apellido, "usted esta en la etapa de la adolescencia.")
    elif edad >= 19 and edad <= 26:
        print(nombre, apellido, "usted esta en la etapa de la juventud.")
    elif edad >= 27 and edad <= 40:
        print(nombre, apellido, "usted esta en la etapa de la adultez joven.")
    elif edad >= 41 and edad <= 55:
        print(nombre, apellido, "usted esta en la etapa de la adultez.")
    elif edad >= 56 and edad <= 65:
        print(nombre, apellido, " usted esta en la etapa de la persona mayor")
        
       # si ingreso mal algun dato le sadra este mensaje al usuario 
    else:
        print("los datos que ingresastes nose encuentrar en el registro")
        
# aqui se calculara si la edad del usuario es par o es impar
Par = edad % 2

if Par == 0:
    print("\nSu edad es par")
else:
    print("\nSu edad es impar")
    # con este mensaje se da por finalisado el programa 
print("\nFin del programa muchas gracias",nombre, apellido, "por responder a todas las preguntas feliz dia")