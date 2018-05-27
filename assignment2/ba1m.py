def NumberToSymbol(number):
    StN = {0:"A",1:"C",2:"G",3:"T"}
    return StN[number]

def NumberToPattern(index,k):
    if k == 1:
        return NumberToSymbol(index)
    prefixIndex = int(index/4)
    r = index%4
    symbol = NumberToSymbol(r)
    PrefixPattern = NumberToPattern(prefixIndex,k-1)
    return PrefixPattern + symbol

print(NumberToPattern(5353,7))