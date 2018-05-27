def SymbolToNumber(symbol):
    StN = {"A":0,"C":1,"G":2,"T":3}
    return StN[symbol]

def PatternToNumber(Pattern):
    if not Pattern:
        return 0
    symbol = Pattern[-1]
    prefix = Pattern[0:-1]
    return ((4*PatternToNumber(prefix))+SymbolToNumber(symbol))

def ComputingFrequencies(text,k):
    FrequencyArray =[]
    for i in range(0,((4**k))):
        FrequencyArray.append(0)
    for i in range(0,(len(text)-1)):
        pattern = text[i:(i+k)]
        j = PatternToNumber(pattern)
        FrequencyArray[j] = FrequencyArray[j]+1
    return FrequencyArray

FrequencyArray = ComputingFrequencies("ACGCGGCTCTGAAA",2)
print(FrequencyArray)