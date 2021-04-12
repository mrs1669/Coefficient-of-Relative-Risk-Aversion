def main():
    #sympy.var('r')
    #print(sympy.solve(DEu(r, 0.1), r))
    print(DEu(-1.73, 0.1))

def u(x: int, r: float):
    return (x**(1-r))/(1-r)

def Eu(x1: int, x2: int, r: float, p: float):
    return p*u(x1,r)+(1-p)*u(x2,r)

def DEu(r: float, p: float):
    return Eu(200, 160, r, p)-Eu(385, 10, r, p)

def solve(r: float):
    min: float = -10.0
    max: float = 10.0
    return

main()