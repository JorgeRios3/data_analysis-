import numpy as np
from matplotlib import pyplot as plt
# mensual ventas

def grfica_mensual(meses, ventas):
    plt.title("ventas del mes") 
    plt.xlabel("meses") 
    plt.ylabel("ventas") 
    plt.plot(meses,ventas, "ob") #formats "ob", "Dr"
    plt.show()

# 2 graficas mismo plot
def dos_graficas_ventas(meses, ventas, ventas2):
    #fig, (ax1, ax2, ax3) = plt.subplots(1, 3, constrained_layout=True)
    fig, plots = plt.subplots(2, 2, constrained_layout=True)
    ax1 = plots[0][0]
    ax2 = plots[0][1]
    ax3 = plots[1][0]
    ax4 = plots[1][1]
    ax1.plot(meses, ventas)
    ax1.set_title('ventas 2020')
    ax1.set_xlabel('meses')
    ax1.set_ylabel('ventas') 
    ax2.plot(meses, ventas2)
    ax2.set_title("ventas 2019")
    ax3.plot(meses, [5,6,7,8,12,56,12,3,4,5,12,11])
    ax4.plot([1,2,3,4,5,6], [2,4,5,6,7,6])
    plt.show()

def grafica_barras(ventas_enero, ventas_febrero):
    plt.bar(ventas_enero[0], ventas_enero[1],  align = 'center', color = 'b') 
    plt.bar(ventas_febrero[0], ventas_febrero[1], color = 'g', align = 'center')
    plt.xticks([1,2,3,4,5,6,7,8,9,10], ["ene 19", "ene 20", "feb 19", "feb 29", "mar 19", "mar 20", "abr 19", "abr 20", "may 19", "may 20"], rotation='vertical')
    plt.title('ventas')
    plt.ylabel('ventas') 
    plt.xlabel('meses')  
    plt.show()

def grafica_histograma(valores, tiempos):
    a = np.array(valores) 
    plt.hist(a, bins = tiempos) 
    plt.title("Histograma") 
    plt.show()
  

def main():
    vinos = np.genfromtxt("vinos.csv", delimiter=";")
    grfica_mensual([1,2,3,4,5,6,7,8,9,10,11,12],vinos[2])
    #dos_graficas_ventas([1,2,3,4,5,6,7,8,9,10,11,12],[1,1,1,1,1,12,14,16,18,20,22,24], [3,5,7,9,11,13,15,17,19,21,23,40])
    #grafica_barras([[1,3,5,7,9], [2,4,6,8,10]], [[1,1,1,1,1],[7,8,9,10,11]])
    #grafica_histograma([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27, 56], [0,20,40,60,80,100])


if __name__ == "__main__":
    main()
