import xml.dom.minidom
from xml.dom import minidom
from xml.dom.minidom import Node
import os


class matriz():
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna


class datomatriz():
    def __init__(self, nombre, x, y, dato, n, m, binario):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.n = n
        self.m = m
        self.binario = binario
        self.dato = dato


class datofinal():
    def __init__(self, nombre, x, y, dato, binario):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.binario = binario
        self.dato = dato


class Nodo():
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class lista_circular():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def Agregarinicio(self, Nodo):
        if self.primero == None:
            self.primero = Nodo
            self.primero.siguiente = self.primero
        else:
            aux = self.primero
            while aux.siguiente is not self.primero:
                aux = aux.siguiente
            aux.siguiente = Nodo
            Nodo.siguiente = self.primero

    def agregarfinal(self, Nodo):
        if self.primero == None:
            self.primero = self.ultimo = Nodo
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo
            self.ultimo.siguiente = self.primero

    def Recorrer(self):
        aux = self.primero
        while aux:
            print(aux.nombre)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def buscar(self, data):
        aux = self.primero
        encontrado = False
        if self.primero == None:
            print("Vacio")
        while (True):
            if (aux.nombre == data):
                encontrado = True
                break
            aux = aux.siguiente
            if (aux == self.primero):
                break
        if (encontrado == True):
            print("Ya esta en la lista")
        else:
            print("No esta en la lista")
        return encontrado

    def display(self):
        curr = self.primero
        n = 1
        if self.primero is None:
            print("List is empty")
            return
        else:
            # Prints each node by incrementing pointer.
            print(n + "- " + curr.nombre)
            n = n + 1
            while (curr.siguiente != self.primero):
                curr = curr.siguiente
                print(n + "- " + curr.nombre)
                n = n + 1

    def borrar(self, dato):
        head = self.primero
        aux = None
        flag = False
        if (self.vacia()):
            print('vacia')
        else:
            if (self.primero == self.ultimo):
                self.primero = None
                self.ultimo = None
            else:
                while (head.siguiente != self.primero):
                    if (flag == False):
                        aux = head.siguiente
                        print(aux.nombre)
                        if (aux.nombre == dato):
                            flag = True
                        if (flag == False):
                            head = head.siguiente
                aux = head.siguiente
                if (aux.nombre == dato):
                    flag = True
                if (flag):
                    if (self.primero == self.primero.siguiente):
                        self.primero = None
                    else:
                        if (aux == self.primero):
                            self.primero = head
                        head.siguiente = aux.siguiente
                        aux = None
        return flag


# ______________________________________________________________________________________________
lista = lista_circular()
dimen = []
di = []
lista_temporal = []
lista_dato = []
n = ""
m = ""


def leerarchivo(document):
    global dimen
    global di
    global lista
    global lista_temporal
    global lista_dato
    global n
    global m
    lista_temporal = []
    TN = 0
    nm = 1
    nd = 0
    jk = 0
    bi = 0
    encontrado = False
    mat = ""
    doc = xml.dom.minidom.parseString(document)
    try:
        nombre = doc.getElementsByTagName("matrices")

        matris = doc.getElementsByTagName("matriz")
        for ma in matris:
            if (encontrado == False):
                print()
            else:
                di.append(matriz(mat, n, m))
                encontrado = False
                mat = ""
            nm = 1
            if lista.vacia():
                nombre = ma.getAttribute("nombre")
                name = Nodo(nombre)
                lista.Agregarinicio(name)
                n = ma.getAttribute("n")
                m = ma.getAttribute("m")
                TN = int(n) * int(m)
                print(nombre + " :" + n + " :" + m)
                mat = nombre
                nn = int(n)
                mm = int(m)
                dimen.append(nombre)
                dato = ma.getElementsByTagName("dato")
                for da in dato:
                    x = da.getAttribute("x")
                    y = da.getAttribute("y")
                    xx = int(x)
                    yy = int(y)
                    comp = int(da.firstChild.data)

                    if (comp == 0):
                        bi = 0
                    else:
                        bi = 1
                    if (xx <= nn):
                        if (yy <= mm):
                            lista_temporal.append(datomatriz(nombre, x, y, da.firstChild.data, n, m, str(bi)))
                            print(nombre, x, y, da.firstChild.data)




                        else:
                            print("Esta " + y + " es mayor a la dimensiones no se agurdara la matriz")
                            lista_temporal = []
                            lista.borrar(nombre)
                            dimen.remove(nombre)
                            di = []
                            nm = nm + 1
                            encontrado = False
                            break
                    else:
                        print("Esta " + x + " es mayor a la dimensiones no se agurdara la matriz")
                        lista_temporal = []
                        lista.borrar(nombre)
                        dimen.remove(nombre)
                        di = []
                        nm = nm + 1
                        encontrado = False
                        break

                    lista_dato.extend(lista_temporal)
                    lista_temporal = []
                    encontrado = True



            else:
                nombre = ma.getAttribute("nombre")
                print(nombre)
                if (lista.buscar(nombre) == True):
                    print("Ya esta: " + nombre)
                else:
                    name = Nodo(nombre)
                    lista.Agregarinicio(name)
                    dimen.append(nombre)
                    n = ma.getAttribute("n")
                    m = ma.getAttribute("m")
                    TN = int(n) * int(m)
                    mat = nombre
                    print(nombre + " :" + n + " :" + m)
                    nn = int(n)
                    mm = int(m)
                    dato = ma.getElementsByTagName("dato")
                    for da in dato:
                        x = da.getAttribute("x")
                        y = da.getAttribute("y")
                        xx = int(x)
                        yy = int(y)
                        comp = int(da.firstChild.data)
                        if (comp == 0):
                            bi = 0
                        else:
                            bi = 1
                        if (xx <= nn):
                            if (yy <= mm):
                                lista_temporal.append(datomatriz(nombre, x, y, da.firstChild.data, n, m, str(bi)))
                                print(nombre, x, y, da.firstChild.data)




                            else:
                                print("Esta " + y + " es mayor a la dimensiones no se agurdara la matriz")
                                lista_temporal = []
                                di = []
                                lista.borrar(nombre)
                                dimen.remove(nombre)
                                nm = nm + 1
                                encontrado = False
                                break
                        else:
                            print("Esta " + x + " es mayor a la dimensiones no se agurdara la matriz")
                            lista_temporal = []
                            di = []
                            lista.borrar(nombre)
                            dimen.remove(nombre)
                            nm = nm + 1
                            encontrado = False
                            break

                        lista_dato.extend(lista_temporal)
                        lista_temporal = []
                        encontrado = True


    except:
        print("")


def grafi():
    global di
    x = 1
    y = 1
    n = 1
    fila = ""
    columna = ""
    nombre = ""
    lis1 = 1
    quotes = '"'
    estado = 0
    pox = 1
    poy = 1
    anterior = ""
    st = True
    p = 1
    pp = 1
    nf = ""
    nc = ""
    jk = ""
    if (dimen == None):
        print("Haga la carga")
    else:
        for i in dimen:
            print(str(n) + "--" + i)
            n = n + 1
        try:
            opcion = str(input("Escoger : "))
            for i in di:
                if (opcion == i.nombre):
                    nombre = i.nombre
                    fila = i.fila
                    columna = i.columna
                    break
            nf = "n=" + fila
            nc = "m=" + columna
            fi = int(fila)
            co = int(columna)
            while st == True:
                if (x <= fi):
                    for gra in lista_dato:
                        pox = int(gra.x)
                        poy = int(gra.y)
                        jk = gra.binario
                        if (gra.nombre == nombre):
                            if (estado == 0):
                                MapaRuta = open(r"C:\Users\denni\OneDrive\Desktop\matriz" + str(lis1) + ".txt", 'w')
                                MapaRuta.write('digraph {' + "\n")
                                MapaRuta.write(("matrices->" + quotes + nombre + quotes + "\n"))
                                MapaRuta.write(quotes + nombre + quotes + "->" + quotes + nf + quotes + "\n")
                                MapaRuta.write(quotes + nombre + quotes + "->" + quotes + nc + quotes + "\n")
                                estado = 1
                                if (gra.nombre == nombre):
                                    if (poy == y and x == 1):
                                        MapaRuta.write(quotes + str(p) + quotes + "[label=" + gra.dato + "]" + "\n")
                                        print(quotes + str(p) + quotes + "[label=" + gra.dato + "]" + "\n")
                                        MapaRuta.write(
                                            quotes + nombre + quotes + "->" + quotes + str(p) + quotes + "\n")
                                        print(quotes + nombre + quotes + "->" + quotes + str(p) + quotes + "\n")
                                        anterior = gra.dato
                                        pp = p
                                        p = p + 1
                                        x = x + 1
                                        break
                                print()
                            elif (estado == 1):
                                print(str(pox), str(poy) + " b" + gra.dato + " o" + jk)
                                if (gra.nombre == nombre):
                                    if (poy == y and x == 1):
                                        MapaRuta.write(quotes + str(p) + quotes + "[label=" + gra.dato + "]" + "\n")
                                        print(quotes + str(p) + quotes + "[label=" + gra.dato + "]" + "\n")
                                        MapaRuta.write(
                                            quotes + nombre + quotes + "->" + quotes + str(p) + quotes + "\n")
                                        print(quotes + nombre + quotes + "->" + quotes + str(p) + quotes + "\n")
                                        anterior = gra.dato
                                        pp = p
                                        p = p + 1
                                        x = x + 1
                                        break
                                    if (poy == y):
                                        if (x == fi):
                                            if (y == co):
                                                MapaRuta.write(
                                                    quotes + str(p) + quotes + "[label=" + gra.dato + "]" + "\n")
                                                MapaRuta.write(
                                                    quotes + str(pp) + quotes + "->" + quotes + str(p) + quotes + "\n")
                                                MapaRuta.write('}')
                                                MapaRuta.close()
                                                os.system("dot -Tsvg "r"C:\Users\denni\OneDrive\Desktop\matriz" + str(
                                                    lis1) + ".txt -o "r"C:\Users\denni\OneDrive\Desktop\matriz" + str(
                                                    lis1) + ".svg")
                                                print("Grafica Completa")
                                                y = y + 1
                                                st = False
                                                break
                                            else:
                                                MapaRuta.write(
                                                    quotes + str(p) + quotes + "[label=" + gra.dato + "]" + "\n")
                                                print(quotes + str(p) + quotes + "[label=" + anterior + "]" + "\n")
                                                MapaRuta.write(
                                                    quotes + str(pp) + quotes + "->" + quotes + str(p) + quotes + "\n")
                                                print(
                                                    quotes + str(pp) + quotes + "->" + quotes + str(p) + quotes + "\n")
                                                anterior = gra.dato
                                                pp = p
                                                p = p + 1
                                                x = 1
                                                y = y + 1
                                                anterior = gra.dato
                                                break
                                        elif (pox == x):
                                            MapaRuta.write(quotes + str(p) + quotes + "[label=" + gra.dato + "]" + "\n")
                                            print(quotes + str(p) + quotes + "[label=" + anterior + "]" + "\n")
                                            MapaRuta.write(
                                                quotes + str(pp) + quotes + "->" + quotes + str(p) + quotes + "\n")
                                            print(quotes + str(pp) + quotes + "->" + quotes + str(p) + quotes + "\n")
                                            anterior = gra.dato
                                            pp = p
                                            p = p + 1
                                            x = x + 1
                                            anterior = gra.dato
                                            break



                                else:
                                    print()
                    else:

                        break


        except:
            main()


def ordernar():
    comparar = 1
    comp=0
    print()


def main():
    opcion = 0
    while (opcion != 7):
        print("  _______________________________________ ")
        print("|MENU PRINCIPAL                           |")
        print("| _______________________________________|")
        print("|                                        |")
        print("| 1) CARGAR ARCHIVO                      |")
        print("| 2) PROCESAR ARCHIVO                    |")
        print("| 3) ESCRIBIR ARCHIVO SALIDA             |")
        print("| 4) MOSTRAR DATOS ESTUDIANTES           |")
        print("| 5) GENERAR GRAFICA                     |")
        print("| 6) SALIR                               |")
        print("| >> ESCOGA OPCION                       |")
        print("| _______________________________________|")
        try:
            opcion = int(input("Opcion:"))
        except:
            main()

        if opcion == 1:  # CARGAR ARCHIVO
            mm = ""
            try:
                ruta = input("Ingrese Ruta:")
                archivo = open(ruta, "r", encoding='utf-8')  # Leer
                print(archivo)
                mm = archivo.read()
                leerarchivo(mm)
            except:
                print("Ruta no valida")


        elif opcion == 2:  # GRAFICAR ARCHIVO   <
            print("_______________________________________")



        elif opcion == 3:  # GRAFICAR ARCHIVO   <
            print("_______________________________________")
        elif opcion == 4:  # GRAFICAR ARCHIVO   <
            print("DENNIS ALEXANDER GAMBOA STOKES")
            print("201700747")
            print("INTRODUCCION A LA PROGRAMACION Y COMPUTACION 2 SECCION 'A' ")
            print("INGENIERIA EN CIENCIAS Y SISTEMAS")
            print("4TO SEMESTRE")

        elif opcion == 5:  # GRAFICAR ARCHIVO   <
            print("_______________________________________")
            grafi()





        elif opcion == 6:  # GRAFICAR ARCHIVO   <
            print("BYE")
            exit()
        else:
            print("Valor erroneo")
    # analizador("CARGAR archivo1, archivo_2, archivo3")


if __name__ == "__main__":
    main()