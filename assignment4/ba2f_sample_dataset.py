import random # needed to generate random numbers
import numpy as np
import math

# splits DNA at spaces
def prepareDNA(Dna):
    Dna = Dna.split(" ")
    return Dna

#calculates Profile from given Motifs by first calculating the frequencies for every positon
# and then the probability for everey position
def getProfile(Motifs):
    frequencies = np.ones((4,len(Motifs[0])), dtype=int) # apply Laplace’s Rule of Succession (pseudocounts)  
    #by creating array of ones for every posible position
    for i in range(len(Motifs)): # calulate frequncies by counting occurence of bases at every index
        for j in range(len(Motifs[i])):
            if Motifs[i][j] == "A":
                frequencies[0,j]+=1
            if Motifs[i][j] == "C":
                frequencies[1,j]+=1
            if Motifs[i][j] == "G":
                frequencies[2,j]+=1
            if Motifs[i][j] == "T":
                frequencies[3,j]+=1
    profile = np.zeros((4,len(Motifs[0])))
    for i in range(len(frequencies[0])): # create profile by calculating probabilities for one base at certain index
        total = sum(frequencies[:,i])
        for j in range(4):
            profile[j][i] = (frequencies[j][i]/total)
    return profile

# searches each strand in Dna for its best Motif (best alignment with profile / best Score / highest probability)
def getMotifs(Profile,Dna,k):
    Motifs = []
    totalScore=0
    for i in Dna:
        curMotif, curScore = find_most_probable_kmer(i,k,Profile)
        totalScore += curScore
        Motifs.append(curMotif)
    return Motifs, totalScore

#calculates Score for combined motifs using getScore, multiplies all probabilities for individual motifs
def getMotifsScore(Motifs,Profile):
    Score = getScore(Motifs[0],Profile)
    for i in Motifs[1:]:
        Score= Score* getScore(i,Profile)
    return Score
#calculates Score for one Motif using Profile, total probability is calculated by multiplying
#probabilities corresbonding to one base at one index in profile
def getScore(Motif,Profile):
    Score = 0
    for i in range(len(Motif)): # get first probability
        tempScore=0
        if Motif[0] == "A":
            tempScore+= Profile[0][0]
        if Motif[0] == "C":
            tempScore+= Profile[1][0]
        if Motif[0] == "G":
            tempScore+= Profile[2][0]
        if Motif[0] == "T":
            tempScore+= Profile[3][0]
        for j in range(1,len(Motif)): # get all following probabilites
            if Motif[j] == "A":
                tempScore= tempScore * Profile[0][j]
            if Motif[j] == "C":
                tempScore= tempScore * Profile[1][j]
            if Motif[j] == "G":
                tempScore= tempScore * Profile[2][j]
            if Motif[j] == "T":
                tempScore= tempScore * Profile[3][j]
        if tempScore > Score:
            Score = tempScore
    return Score

#finds k-mer with best fit to profile
def find_most_probable_kmer(Dna,k,Profile):
    Score = 0
    for i in range((len(Dna)-k)+1): #get all posible k-mers which are contained in Dna and check them for their score
        temp = Dna[i:i+k]
        tempScore = getScore(temp,Profile)
        if tempScore > Score:
            Motif = temp
            Score = tempScore
    return Motif, Score

#finds best Motif by random algorithm
#Motifs is at first created by randomly selecting k-mers --> create Profile from random Motifs
#Profile is used to select new Motifs --> modify profile using new Motifs, use new profile to find best motifs...
def RandomizedMotifSearch(Dna,k,t):
    Motifs = []
    Dna = prepareDNA(Dna)
    Dna_len = len(Dna[0])
    for i in range(t): #get random motifs
        ran_num = random.randint(0,(Dna_len-k))
        Motifs.append(Dna[i][ran_num:(ran_num+k)])
    BestMotifs = Motifs
    ScoreBestMotifs = 0
    while True: # search for new motifs as long as score improves
        Profile = getProfile(Motifs)
        if ScoreBestMotifs == 0:
            ScoreBestMotifs = getMotifsScore(BestMotifs,Profile)
        Motifs ,ScoreMotifs = getMotifs(Profile,Dna,k)
        ScoreMotifs = getMotifsScore(Motifs,Profile)
        if ScoreMotifs > ScoreBestMotifs:
            BestMotifs = Motifs
            ScoreBestMotifs = ScoreMotifs
        else: 
            return BestMotifs, ScoreBestMotifs
#executes RandomizedMotifSearch 1000 times and returns best RandomizedMotifSearch result       
def getCollectionBestMotifs(Dna,k,t):
    Score = 0
    Motifs = []
    for i in range(1000):
        tempMotifs,tempScore = RandomizedMotifSearch(Dna,k,t)
        if Score < tempScore:
            Score = tempScore
            Motifs = tempMotifs
    return Motifs,Score              


print(getCollectionBestMotifs("CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA", 8, 5))