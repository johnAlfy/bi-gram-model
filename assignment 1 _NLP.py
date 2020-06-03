import nltk
import re
from nltk.util import trigrams, bigrams
from collections import Counter
from nltk.corpus import stopwords
from operator import itemgetter

f = open("spacetoon.txt", encoding='utf-8')
d = f.read()
data = nltk.word_tokenize(d)

for d in range(len(data)):
    data[d] = re.sub("[A-Za-z0-9\[\]\<\>\s+\t+\n+]", "", data[d].strip())

sw = stopwords.words('arabic')

stopped_tokens =data# [i for i in data if not i in sw]
lst = []
for d in range(len(stopped_tokens)):
    if stopped_tokens[d] == "":
        continue
    else:
        lst.append(stopped_tokens[d])
print(lst)

wordsCount = list(Counter(lst).items())
wordsCount = sorted(wordsCount, key=lambda x: x[1])
wordsCount = [list(elem) for elem in wordsCount]
print(wordsCount)

bi_tokens = list(bigrams(lst))
#print(len(bi_tokens))
biTockensCount = list(Counter(bi_tokens).items())
biTockensCount = sorted(biTockensCount, key=lambda x: x[1])
biTockensCount = [list(elem) for elem in biTockensCount]
print(biTockensCount)

tri_tokens = list(trigrams(lst))
#print(len(tri_tokens))
triTockensCount = list(Counter(tri_tokens).items())
triTockensCount = sorted(triTockensCount, key=lambda x: x[1])
triTockensCount = [list(elem) for elem in triTockensCount]
print(triTockensCount)
def returnMeAcount(tuple, mylist):

    for g in mylist:
        if g[0] == tuple:
            return g[1]
    return 0
def guess(string ,bigrams,trigrams):
    lOfProb=[]
    for bi in bigrams:
        t=(string,bi[0][0],bi[0][1])
        probOfTri=returnMeAcount(t,trigrams)/len(trigrams)
        probOfBi=returnMeAcount(bi[0],bigrams)/len(bigrams)
        fProb=probOfTri/probOfBi
        lOfProb.append([t,fProb])
    lOfProb=sorted(lOfProb, key=itemgetter(1))
    lOfProb=lOfProb[::-1]
    return lOfProb[0:5]

def finalPrint():
    r = ""
    while True:
        r = r +" "+ str(input())
        print(r)
        g = r.split(" ")
        g = g[-1]

        l=guess(g,biTockensCount,triTockensCount)
        for i in l:
            print((i[0][1],i[0][2],i[1]))
finalPrint()