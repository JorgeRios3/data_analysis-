import entradas as enters
import salidas
import arreglos
import os


def run_local_main():
    valor = input("quieres trabajar con entradas o con salidas")
    print(valor)
    if valor == "entradas":
        print(enters.menu())


def run_remoto_main():
    print("ejecucion remota")





if __name__ == "__main__":
    ejecucion = os.environ["local"]
    if ejecucion == "local":
        run_local_main()
    else:
        run_remoto_main()









