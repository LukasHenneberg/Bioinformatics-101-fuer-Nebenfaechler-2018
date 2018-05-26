def PatternCount(text, pattern):
    count = 0
    for i in range(0,len(text)-len(pattern) + 1):
         if text[i:i+len(pattern)] == pattern:
             count +=1
    return count

def FrequentWords(text, k):
    FrequentPatterns=[] # Ausgabeliste, alle Pattern mit maximalem count
    COUNT=[] # Speichert für jede Position wie oft das Pattern das an der Position beginnt im Text vorkommt
    for i in range(0, len(text) - k + 1):
            current_pattern = text[i:i+k]
            current_count = PatternCount(text,current_pattern)
            if len(COUNT)==0:
                FrequentPatterns.append(current_pattern)
                COUNT.append(current_count)
            elif current_count == max(COUNT):
                FrequentPatterns.append(current_pattern)
                COUNT.append(current_count)
            elif current_count > max(COUNT):
                FrequentPatterns=[]
                COUNT=[]      
                FrequentPatterns.append(current_pattern)
                COUNT.append(current_count)
    return list(set(FrequentPatterns))

DNA_string = input("Please enter your DNA sequence: ")
k = int(input("Please enter k: "))

print(FrequentWords(DNA_string,k))