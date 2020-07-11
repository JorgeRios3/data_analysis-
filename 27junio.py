import csv
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#tamañano archivo
#os.path.getsize("vinos.csv")

#fechas
#x = datetime.datetime.now()
#x = datetime.datetime(2018, 6, 1)
#print(x.strftime("%B")) %c

#listar archivos
#for _file in os.listdir('.'):
#...   print("{:.<35}{:5}".format(_file, os.path.getsize(_file)))



#pandas
#content = pd.read_csv('vinos.csv')
ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000', periods=1000))
print(type(ts))
ts = ts.cumsum()
print(ts)



#np.random.rand(3,4)
#vinos = np.genfromtxt("vinos.csv", delimiter=";") #filling_values=-999  skip_header=1
#print(np.shape(vinos))
#np.savetxt('test.out', x, delimiter=',')

#qualities = [float(item[-1]) for item in vinos[1:]]
#sum(qualities) / len(qualities)


#operaciones matematicas
#+,-,*,/,%,sqrt(),sin(),cos()
#np.sin(x,y)



#leer archivo csv
#with open('personas.txt', 'r') as f:
#    personas = list(csv.reader(f, delimiter=','))
#    print(personas)

#moficar archivo csv
#with open("personas.txt", "w") as f:
#   for x in personas:
#     linea = "{}\n".format(",".join(x))
#
#      f.write(linea)




#personas = '[{"nombre":"jorge", "apellido":"rios", "edad":29}, {"nombre":"jair", "apellido":"beltran", "edad":22}]'

#personas_json = json.loads(personas)
#print(personas)
#print(json.dumps(personas_json))





#a=[None,None,None,None]

#numpy functiones
#y = np.random.random((3,4))
#y = np.zeros((3,4))
#y = np.ones((3,4))
#np.shape(y)
#y = np.random.random((5,1,4))
#+, -, *, / or %
#np.add(), np.subtract(), np.multiply(), np.divide() and np.remainder()
#b.median()


#arrays indexes
#lista=[1,2,3,4,5]
#ultimo valor lista[-1]
#ultimos 2 lista[-2:]
#primeros 2 lista[:2]
#valores de pocisiones lista[0:4]

#lista2= [[1,2,3], [4,5,6]]
#ultomo valor lista2[-1][-1]



#manejo de lista
#ordernar lista
#[1,3,3,2].sort()

#manejo de json

#convertir de string a json json.loads('[{"nombre":"apellid"}]')
#convertir de json a string json.dumps([{"nombre":"apellid"}])

#dicionario_anidado = [{"nombre":"jorge", "direcciones":[{"numero":1244},{"numero":234, "color":"blanco"}]}]
#dicionario_anidado[0]["direcciones"][1]["color"]


#order por tamaño dentro de lista con diccionarios
#import operator
#lista.sort(key=operator.itemgetter('size'))
