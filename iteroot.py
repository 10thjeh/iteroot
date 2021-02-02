import function

def newton(x1, iter, showIter):
    root=0
    if showIter:
        print("n\t\tx")
    for n in range(iter):
        fx1 = function.f(x1)
        dfx1 = function.df(x1)
        x2 = x1-(fx1/dfx1)
        if showIter:
            print(str(n)+"\t\t"+str(x2))
        x1 = x2
        root = x1
    if not showIter:
        return root
