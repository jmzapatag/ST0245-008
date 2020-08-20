import sys

def  pascal(row, column):
    if row < 0 and column < 0:
        return 0
    elif row == 0 and column == 0:
        return 1
    else:
        return pascal(row-1,column-1) + pascal(row-1,column)

def sol(num):
    for c in range(num):
        for f in range(c+1):
            sys.stdout.write(str(pascal(f,c))+" ")
        print('\n')
num=int(input("Ingrese el numero de filas del triangulo: "))
print(sol(num+1))
