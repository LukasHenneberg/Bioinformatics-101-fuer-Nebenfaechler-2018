import math #needed for math.inf

# takes number from 0 to 3 and returns corresponding base
def NumberToSymbol(number):
    StN = {0:"A",1:"C",2:"G",3:"T"}
    return StN[number]


#used to generate all paterns with lenght k
def NumberToPattern(index,k):
    if k == 1:
        return NumberToSymbol(index)
    prefixIndex = int(index/4)
    r = index%4
    symbol = NumberToSymbol(r)
    PrefixPattern = NumberToPattern(prefixIndex,k-1)
    return PrefixPattern + symbol

# calculates HammingDistance by iterating over Dna and searching for mismatches between Pattern and Dna
# for every missmatch the HammingDistance gets incremented by 1
def getHammingDistance(Pattern,curPattern):
    HammingDistance = 0
    for i in range(len(Pattern)):
        if Pattern[i] != curPattern[i]:
            HammingDistance += 1
    return HammingDistance
        

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern) # set k to lenght of Pattern
    distance = 0
    splitDNA = Dna.split(" ") # seperate DNA string in this case by spaces
    for Text in splitDNA: # iterate over strings in Dna
        HammingDistance = math.inf # set HammingDistance to inf
        for i in range((len(Text)-k)+1): #iterate over every index of the substring of Dna
            temp = getHammingDistance(Pattern, Text[i:(i+k)]) # calculate HammingDistance for current substring pattern / reduces amount of times HammingDistance needs to be calculated
            if HammingDistance > temp: #HammingDistance gets set to current HammingDistance if it is smaller than the previous smalles HammingDistance
                HammingDistance = temp
        distance = distance + HammingDistance #adds HammingDistances for all substrings of Dna together to get true distance
    return distance

#generates all posible Patterns with lenght k and calculate HammingDistance for each pattern with every substring of Dna
# returns pattern which shows the lowest combined HammingDistance of all substrings of Dna
def MedianString(k,Dna):
    distance = math.inf
    for i in range(((4**k)-1)):
        Pattern = NumberToPattern(i,k)
        temp = DistanceBetweenPatternAndStrings(Pattern, Dna)
        if distance > temp:
            distance = temp
            Median = Pattern
    return Median
    
print(MedianString(6,"TGATGATAACGTGACGGGACTCAGCGGCGATGAAGGATGAGT CAGCGACAGACAATTTCAATAATATCCGCGGTAAGCGGCGTA TGCAGAGGTTGGTAACGCCGGCGACTCGGAGAGCTTTTCGCT TTTGTCATGAACTCAGATACCATAGAGCACCGGCGAGACTCA ACTGGGACTTCACATTAGGTTGAACCGCGAGCCAGGTGGGTG TTGCGGACGGGATACTCAATAACTAAGGTAGTTCAGCTGCGA TGGGAGGACACACATTTTCTTACCTCTTCCCAGCGAGATGGC GAAAAAACCTATAAAGTCCACTCTTTGCGGCGGCGAGCCATA CCACGTCCGTTACTCCGTCGCCGTCAGCGATAATGGGATGAG CCAAAGCTGCGAAATAACCATACTCTGCTCAGGAGCCCGATG"))

