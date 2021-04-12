def main():
    print(u(2, 0.5))


def u(x: int ,r: float):
    return (x**(1-r))/(1-r)


main()