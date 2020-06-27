print("hola")
print("hola")

# este es mi comentario
# tipos de datos
# tipo int
variable_int = 1

#tipo char
variable_char = "c"
# tipo string
variable_string = "hola"
# tipo folat
variable_float = 1.5
# tipo list
variable_list = [1,2,3,4] + [1,2,3]
# tipo dict
variable_diccionario = {"nombre": "jorge", "apellido":"rios"}
# tipo set
variable_set = set([1,2,3])

variable_int_string = "11111"

variable_string_float = "1.5"

#print(variable_string + variable_int_string)

#print(variable_int + float(variable_string_float))

#print(variable_list)

#print(variable_list[0])
#print(variable_list[6])

#personas = [{"nombre":"jorge", "apellido":"rios", "direcciones": [{"calle":"tonala"}], "tt":[{},{}]}, {"nombre":"carlos", "apellido":"beltran"}]

#print(variable_diccionario)
#print(variable_diccionario["nombre"])

#print(personas[0]["nombre"], personas[0]["direcciones"][0]["calle"] , personas[1]["nombre"])



# print(dir(variable_list))
# print(type(variable_int), type(variable_string), type(variable_list), type(variable_diccionario),type(variable_set))


#print(1+1)
#print(2-1)
#print(2/1)
#print(2*3)
#print(5%2)

#operadores logicos True, False, or, and, <, >, <>, != 

#return False
print(1 > 4)

#return True
print(4 > 1 and 5 > 3)
#return True
print(True or False)
#return True
print(False or True)

#return False
print(False or False)

#return False
print(False and False)

print(1<3)

print(1!=2)


a = input("dame tu edad")
b = "jorge"
saludo = "hola {} tienes {} años {} {}".format(b, a, "sale", 1)
print(saludo)




#if, else, elif, for, while




# este es mi comentario
# tipos de datos
# tipo int
variable_int = 1

#tipo char
variable_char = "c"
# tipo string
variable_string = "hola"
# tipo folat
variable_float = 1.5
# tipo list
variable_list = [1,2,3,4] + [1,2,3]
# tipo dict
variable_diccionario = {"nombre": "jorge", "apellido":"rios"}
# tipo set
variable_set = set([1,2,3])

variable_int_string = "11111"

variable_string_float = "1.5"

#print(variable_string + variable_int_string)

#print(variable_int + float(variable_string_float))

#print(variable_list)

#print(variable_list[0])
#print(variable_list[6])

#personas = [{"nombre":"jorge", "apellido":"rios", "direcciones": [{"calle":"tonala"}], "tt":[{},{}]}, {"nombre":"carlos", "apellido":"beltran"}]

#print(variable_diccionario)
#print(variable_diccionario["nombre"])

#print(personas[0]["nombre"], personas[0]["direcciones"][0]["calle"] , personas[1]["nombre"])



# print(dir(variable_list))
# print(type(variable_int), type(variable_string), type(variable_list), type(variable_diccionario),type(variable_set))


#print(1+1)
#print(2-1)
#print(2/1)
#print(2*3)
#print(5%2)

#operadores logicos True, False, or, and, <, >, <>, != 

#return False
print(1 > 4)

#return True
print(4 > 1 and 5 > 3)
#return True
print(True or False)
#return True
print(False or True)

#return False
print(False or False)

#return False
print(False and False)

print(1<3)

print(1!=2)


#a = input("dame tu edad")
#b = "jorge"
#saludo = "hola {} tienes {} años {} {}".format(b, a, #"sale", 1)
#print(saludo)




#if, else, elif, break
#for, while

#lista = [1,2,3,4,5]
#valor_buscado = 0
#for v in lista:
#  print("viend item", v+1)


#print(valor_buscado)


#tope = 0

#while(tope <= 10):
#  tope = tope + 1
#  print("el de tope", tope)


#tupla = (1,2,3)
#lista_x = [1,2,3]
#personas2 = [{"apellid":"rios", "nombre":"jorge"}, #{"nombre":"ana"}]
#personas = [("rios", "jorge"), ("ana", "monte")]
#for persona in personas:
#  print(persona[0])

#for persona in personas2:
#  print(persona["nombre"])



#print(personas[0][0])
#print(lista_x + [20])

def mandar_imprimir(mensaje = "valor default", nombre = "nombre devaul"):
  print(mensaje, nombre)

def operacion_aritmetica(operador, valor1, valor2):
  if operador == "+":
    return  valor1 +valor2


#def obtener_saludo_nombre():
#  nombre = input("dame nombre\n")
#  apellido = input("dame apellido\n")
#  saludo = input("saludo\n")
#  mandar_imprimir(nombre, saludo)
#  mandar_imprimir()


#obtener_saludo_nombre()


#valor_regreso = operacion_aritmetica("+", 2, 2)
#print("el valor es", valor_regreso)
#valor_regreso = valor_regreso + operacion_aritmetica("+", 1,1)

#print("el valor es", valor_regreso)

archivo = "hola mundo\n como estas?"

#metodo lectura archivo
#with open("archivo.txt", "r") as f:
#  lineas = f.readlines()
#  print(lineas)

#metodo escritura archivo
#with open("archivo.txt", "w") as f:
  # lineas = f.readlines()
  #lineas[0] = "remplazar texto"
  # f.writelines(lineas)
  #for line in f:
    #print(line)
lista = [10, 1,2,3,4,5]


#map = mutar
#filter = filtrado

lista2 = list(filter(lambda x: x > 2, lista))

print("esta es la lista", lista2)

