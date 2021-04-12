def main():
    print(Eu(2, 5, 0.5, 0.5))

def u(x: int ,r: float):
    return (x**(1-r))/(1-r)

def Eu(x1: int, x2: int, r: float, p: float):
    return p*u(x1,r)+(1-p)*u(x2,r)

main()