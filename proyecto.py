# DEF DE LA COLA PRIORITARIA

class Carro:
    def __init__(self, placa, marca, modelo, llegada):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.llegada = llegada

    def __str__(self):
        return f"{self.placa} - {self.marca} {self.modelo}, llegada {self.llegada}"


class ColaPrioritaria:
    def __init__(self):
        self.lista = []

    def encolar(self, carro):
        self.lista.append(carro)

    def desencolar(self):
        if len(self.lista) == 0:
            return None

        mejor = self.lista[0]
        for f in self.lista:
            if f.llegada < mejor.llegada:
                mejor = f

        self.lista.remove(mejor)
        return mejor

    def ver_primero(self):
        if len(self.lista) == 0:
            return None

        mejor = self.lista[0]
        for f in self.lista:
            if f.llegada < mejor.llegada:
                mejor = f
        
        return mejor

    def esta_vacia(self):
        return len(self.lista) == 0










# QUE SE VALLAN APILANDO EN UN ARREGLO

class PilaCarros:
    def __init__(self):
        self.arreglo = []

    def apilar(self, carro):
        self.arreglo.append(carro)

    def desapilar(self):
        if not self.arreglo:
            return None
        return self.arreglo.pop()

    def ver_tope(self):
        if not self.arreglo:
            return None
        return self.arreglo[-1]

    def mostrar(self):
        return list(reversed(self.arreglo))







# ARBOL BINARIO

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def re_inorden(raiz):
    if raiz is None:
        return
    re_inorden(raiz.izquierda)
    print(raiz.valor, end=" | ")
    re_inorden(raiz.derecha)

def re_preorden(raiz):
    if raiz is None:
        return
    print(raiz.valor, end=" | ")
    re_preorden(raiz.izquierda)
    re_preorden(raiz.derecha)

def re_posorden(raiz):
    if raiz is None:
        return
    re_posorden(raiz.izquierda)
    re_posorden(raiz.derecha)
    print(raiz.valor, end=" | ")
    















    #PRUEBAS

cola = ColaPrioritaria()
pila = PilaCarros()
raiz = None

def insertar(raiz, carro):
    if raiz is None:
        return Nodo(carro)
    if carro.llegada < raiz.valor.llegada:
        raiz.izquierda = insertar(raiz.izquierda, carro)
    else:
        raiz.derecha = insertar(raiz.derecha, carro)
    return raiz

print("Ingresa carros así: placa marca modelo llegada")
print("Ejemplo: ABC-123 Toyota Corolla 1")
print("Escribe 'fin' para terminar.\n")

while True:
    linea = input("Ingresar texto >> ")

    if linea == "fin":
        break

    partes = linea.split()

    if len(partes) < 4:
        print("Debes ingresar 4 datos.")
        continue

    placa = partes[0]
    marca = partes[1]
    modelo = partes[2]
    llegada = int(partes[3])

    carro = Carro(placa, marca, modelo, llegada)

    cola.encolar(carro)
    pila.apilar(carro)
    raiz = insertar(raiz, carro)

    print("Carro agregado.")

print("\nPrimer carro en la cola:")
print(cola.ver_primero())

print("\nCarros en la pila (tope primero):")
for c in pila.mostrar():
    print(c)

print("\nÁrbol en inorden:")
re_inorden(raiz)
print()
print("\nÁrbol en preorden:")
re_preorden(raiz)
print()
print("\nÁrbol en posorden:")
re_posorden(raiz)
print()