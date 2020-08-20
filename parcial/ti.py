n = 5
def ident(n):
    if n == 1:
        print (n)
    else:
        print (n)
        n = n-1
        ident(n)
ident(n)  
