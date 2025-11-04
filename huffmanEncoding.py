def wordCount(bookName):
    with open(bookName) as f:
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


if __name__ == "__main__":
    bookName = "books/" + input("Input Book.txt: ")
    listOfChars, wcnt = wordCount(bookName) 
    print(listOfChars)
    print(wcnt)

