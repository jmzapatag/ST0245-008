def hanoi_rec(n, inicio, fin, aux):
    if n == 1:
        print("mover disco", n,  "de torre",inicio,  "a torre", fin)
        return
    else:
        hanoi_rec(n-1, inicio, aux, fin)
        print("mover disco", n, "de torre", inicio, "a torre", fin)
        hanoi_rec(n-1, aux, fin, inicio)

def hanoi(n):
    hanoi_rec(n, 1, 3, 2)


def hanoi_count(n):
    x = 2 ** (n) - 1
    return x

x = int(input("Escriba el número de discos: "))
hanoi(x)
count = hanoi_count(x)
print("Número de movimientos totales: ", count)