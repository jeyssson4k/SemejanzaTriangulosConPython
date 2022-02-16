# algoritmo para solucion de triangulos por el metodo del teorema fundamental de la proporcionalidad

a1 = float(input("Ingrese el valor de a1, si no lo tienes, ingresa 0: \n"))
a2 = float(input("Ingrese el valor de a2, si no lo tienes, ingresa 0: \n"))
b1 = float(input("Ingrese el valor de b1, si no lo tienes, ingresa 0: \n"))
b2 = float(input("Ingrese el valor de b2, si no lo tienes, ingresa 0: \n"))
c1 = float(input("Ingrese el valor de c1, si no lo tienes, ingresa 0: \n"))
c2 = float(input("Ingrese el valor de c2, si no lo tienes, ingresa 0: \n"))

#condicion para a-b-c
if a1 != 0 and a2 != 0:

    if b1 != 0 and b2 != 0:
        if c1 != 0:
            c2 = (b2 * c1) / b1
        elif c2 != 0:
            c1 = (b1 * c2) / b2
    elif b1 != 0:
        b2 = (a2 * b1) / a1
        if c1 != 0:
            c2 = (a2 * c1) / a1
        elif c2 != 0:
            c1 = (a1 * c2) / a2
    elif b2 != 0:
        b1 = (a1 * b2) / a2
        if c1 != 0:
            c2 = (a2 * c1) / a1
        elif c2 != 0:
            c1 = (a1 * c2) / a2

    if c1 != 0 and c2 != 0:
        if b1 != 0:
            b2 = (b1 * c2) / c1
        elif b2 != 0:
            b1 = (c1 * b2) / c2
    elif c1 != 0:
        c2 = (c1 * a2) / a1
        if b1 != 0:
            b2 = (b1 * a2) / a1
        elif b2 != 0:
            b1 = (a1 * b2) / a2
    elif c2 != 0:
        c1 = (c2 * a1) / a2
        if b1 != 0:
            b2 = (b1 * a2) / a1
        elif b2 != 0:
            b1 = (a1 * b2) / a2

#condicional para b-c-a
if b1 != 0 and b2 != 0:

    if c1 != 0 and c2 != 0:
        if a1 != 0:
            a2 = (c2 * a1) / c1
        elif a2 != 0:
            a1 = (c1 * a2) / c2
    elif c1 != 0:
        c2 = (b2 * c1) / b1
        if a1 != 0:
            a2 = (b2 * a1) / b1
        elif a2 != 0:
            a1 = (b1 * a2) / b2
    elif c2 != 0:
        c1 = (b1 * c2) / b2
        if a1 != 0:
            a2 = (b2 * a1) / b1
        elif a2 != 0:
            a1 = (b1 * a2) / b2

    if a1 != 0 and a2 != 0:
        if c1 != 0:
            c2 = (c1 * a2) / a1
        elif c2 != 0:
            c1 = (a1 * c2) / a2
    elif a1 != 0:
        a2 = (a1 * b2) / b1
        if c1 != 0:
            c2 = (c1 * b2) / b1
        elif c2 != 0:
            c1 = (b1 * c2) / b2
    elif a2 != 0:
        a1 = (a2 * b1) / b2
        if c1 != 0:
            c2 = (c1 * b2) / b1
        elif c2 != 0:
            c1 = (b1 * c2) / b2

#condicional para c-a-b
if c1 != 0 and c2 != 0:

    if a1 != 0 and a2 != 0:
        if b1 != 0:
            b2 = (a2 * b1) / a1
        elif b2 != 0:
            b1 = (a1 * b2) / a2
    elif a1 != 0:
        a2 = (c2 * a1) / c1
        if b1 != 0:
            b2 = (c2 * b1) / c1
        elif b2 != 0:
            b1 = (c1 * b2) / c2
    elif a2 != 0:
        a1 = (c1 * a2) / c2
        if b1 != 0:
            b2 = (c2 * b1) / c1
        elif b2 != 0:
            b1 = (c1 * b2) / c2

    if b1 != 0 and b2 != 0:
        if a1 != 0:
            a2 = (a1 * b2) / b1
        elif a2 != 0:
            a1 = (b1 * a2) / b2
    elif b1 != 0:
        b2 = (b1 * c2) / c1
        if a1 != 0:
            a2 = (a1 * c2) / c1
        elif a2 != 0:
            a1 = (c1 * a2) / c2
    elif b2 != 0:
        b1 = (b2 * c1) / c2
        if a1 != 0:
            a2 = (a1 * c2) / c1
        elif a2 != 0:
            a1 = (c1 * a2) / c2

#imprimir los resultados
print("Los resultados son.... \n\n\n")

print("Primer triángulo: \n")
print("Lado a: ",a1)
print("Lado b: ",b1)
print("Lado c: ",c1)

print("\n\n")

print("Segundo triángulo: \n")
print("Lado a: ",a2)
print("Lado b: ",b2)
print("Lado c: ",c2)

























#ESTO ES PYTHON

