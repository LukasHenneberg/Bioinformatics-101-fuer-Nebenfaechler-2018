import math #needed for math.inf

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


print(DistanceBetweenPatternAndStrings("AAA", "TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT"))