def main():
    print('選択肢Bにスイッチした組番号 高い賞金が当たる確率p 閾値相対的リスク回避度r')
    for p in range(1, 10, 1):
        print('            ', p+1, '            |        ', p/10, '        |         ', solve(p/10))

def u(x: int, r: float):
    return (x**(1-r))/(1-r)

def Eu(x1: int, x2: int, r: float, p: float):
    return p*u(x1,r)+(1-p)*u(x2,r)

def DEu(r: float, p: float):
    return Eu(200, 160, r, p)-Eu(385, 10, r, p)

def solve(p: float):
    min: float = -10.0
    max: float = 10.0
    count: int = 1000
    small: float = min
    large: float = max
    temp: float = 0
    while count > 0:
        mid = (small+large)/2
        if DEu(mid, p)>0:
            large = mid
        else:
            small = mid
        count-=1
    return round(mid, 2)

main()