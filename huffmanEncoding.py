import heapq
class Node:
    def __init__(self, data):
        self.data = data
        # Pointer to the left child node
        self.left = None
        # Pointer to the right child node
        self.right = None
    def __lt__(self, other):
            return self.data[1] < other.data[1]

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
        frequencyDic[word] = freq
    return frequencyDic
         
def makeTrie(freqD):
    heap = [] 
    for word in freqD:
        #add them to the priority queue
        tup = (word, freqD[word])
        element = Node(tup)
        print(element)
        heapq.heappush(heap, element)

    while len(heap) > 1:
        #create a tuple pair of the letter (frequency, letter pair), then add them back to the heap
        word1 = heapq.heappop(heap)
        word2 = heapq.heappop(heap)
        
        freq = word1.data[1] + word2.data[1]
        combinedWord = word1.data[0] + word2.data[0]
        tup = (combinedWord, freq)
        pair  = Node(tup)
        heapq.heappush(heap, pair)
        print(pair.data[0])



if __name__ == "__main__":
    # bookName = "books/" + input("Input Book.txt: ")
    bookName = "books/book1.txt"
    listOfChars, wcnt = wordCount(bookName) 
    print(listOfChars)
    print(wcnt)
    freqD = frequency(listOfChars, wcnt)
    print(freqD)
    makeTrie(freqD)


