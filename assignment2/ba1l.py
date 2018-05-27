def SymbolToNumber(symbol):
    StN = {"A":0,"C":1,"G":2,"T":3}
    return StN[symbol]

def PatternToNumber(Pattern):
    if not Pattern:
        return 0
    symbol = Pattern[-1]
    prefix = Pattern[0:-1]
    return ((4*PatternToNumber(prefix))+SymbolToNumber(symbol))

print(PatternToNumber("CTTCTCACGTACAACAAAATC"))  