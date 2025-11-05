import heapq
def wordCount(bookName):
    with open(bookName, mode = 'r', encoding='utf-8-sig') as f:
        D = {} #occurrences counting dictionary
        wcnt = 0 #total character
        while True:
            line = f.readline() #read in a line (newline char included)
            if len(line)==0: return D, wcnt#end of the book
            else:
                wcnt += len(line)
                for x in line: #extract each char and update counting
                    if x in D: D[x]+=1
                    else: D[x]=1

def frequency(D, wcnt):
    frequencyDic = {}
    for word in D:
        freq = (D[word])/wcnt
        frequencyDic[freq] = word
    return frequencyDic
         
def makeTrie(freqD):
    heap = []
    trie = [] * len(freqD.keys()) #trie of the tuples,
    for freq in freqD:
        #add them to the priority queue
        letter = (freq, freqD[freq])
        heapq.heappush(heap, letter)
    while len(heap) > 1:
        #create a tuple pair of the letter (frequency, letter pair), then add them back to the heap
        letter1 = heapq.heappop(heap)
        letter2 = heapq.heappop(heap)
        pair = (letter1[0]+letter2[0], letter1[1]+letter2[1])
        heapq.heappush(heap, pair)
        print(pair)



if __name__ == "__main__":
    # bookName = "books/" + input("Input Book.txt: ")
    bookName = "books/book1.txt"
    listOfChars, wcnt = wordCount(bookName) 
    print(listOfChars)
    print(wcnt)
    freqD = frequency(listOfChars, wcnt)
    print(freqD)
    makeTrie(freqD)


