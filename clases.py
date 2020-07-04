class Animal(object):
    def __init__(self, raza):
        self.raza = raza
    def idioma(self):
        print("idioma de comunicacion")
    
    def raza(self):
        print("esta es la raza", raza)
        return self.raza

    def set_raza(self, val):
        self.raza = val

class Perro(Animal):
    def __init__(self, raza, nombre):
        Animal.__init__(self, raza)
        self.nombre = nombre
    def idioma(self):
        print("ladrar")

class Gato(Animal):
    def __init__(self, raza, nombre):
        Animal.__init__(self, raza)
        self.nombre = nombre


class Persona(object):
    def __init__(self,nombre):
        self.nombre = nombre
        self.pet = None


class Animal2: 
	def __init__(self): 
		self._raza = "pastor"
	@property
	def raza(self): 
		print("getter method called") 
		return self._raza 
	
	# a setter function 
	@raza.setter 
	def raza(self, a): 
		self._raza = a 



def decora(func):
    def wrapper():
        print("antes de llamar a funcion ")
        func()
        print("despues de llamar a funcion")
    return wrapper

@decora
def saludo():
    print("en saludo")



def decora2(func):
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        if val == "jorge":
            return func(*args, **kwargs)
        else:
            raise Exception("no eres jorge")
    return wrapper


@decora2
def saludo2(nombre):
    return (nombre)







class Animal(object):
  def __init__(self, color, edad):
    self.color = color
    self.edad = edad
  
  def saludo(self):
    print("hola saludo desde clase padre")

  def dame_color(self):
    print("clase soy color {}".format(self.color))
    return self.color
  
  def dame_edad(self):
    return self.edad

  def actualiza_edad(self, edad):
    self.edad = edad
  
  
  def es_mayor_de_edad(self):
    if self.edad > 18:
      return True
    else:
      return False



class Perro(Animal):
  def __init__(self, nombre, color, edad):
    self.nombre = nombre
    self.habitad = "casa hogar"
    Animal.__init__(self, color, edad)
  
  def dame_nombre(self):
    print("mi nombre es {}".format(self.nombre))
  
  def dame_habitad(self):
    print("mi habitad es {}".format(self.habitad))
  
  def saludo(self):
    print("ladrar")

class Gato(Animal):
  def __init__(self, nombre, color, edad):
    self.nombre = nombre
    self.habitad = "casa hogar"
    Animal.__init__(self, color, edad)
  
  def saludo(self):
    print("mauyar")

goliat = Perro("goliat", "negro", 10)
joaquin = Perro("joaquin", "blanco", 20)

kitty = Gato("kitty", "negro", 10)


print(goliat.dame_edad())
#goliat.es_mayor_de_edad()
#goliat.dame_color()
#goliat.dame_nombre()
#goliat.dame_habitad()
goliat.actualiza_edad(20)
print("cambiando")
print(goliat.dame_edad())
#goliat.es_mayor_de_edad()
#goliat.saludo()
#kitty.saludo()

print("\n")
#joaquin.dame_nombre()
#edad =joaquin.dame_edad()
#color = joaquin.dame_color()
#print("desde la variable color ", color)
#es_mayor = joaquin.es_mayor_de_edad()

#if es_mayor:
#  print("si es mayor desde variable")
#else:
#  print("es menor desde variable")


class Persona:
    def __init__(self,nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
      self.__nombre = nombre


rodolfo = Persona("rodolfo")

print(rodolfo.nombre)
print("cambiando")
rodolfo.nombre = "jorge"
print(rodolfo.nombre)

print(isinstance(rodolfo, Persona))
