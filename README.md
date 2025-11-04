# cs2123-project4
[Instructions](Project4.pdf)

Python Example:
```
bookName = "somebook.txt"
with open(bookName) as f:
  D = {} #occurrences counting dictionary
  wcnt = 0 #total character
  while True:
    line = f.readline() #read in a line (newline char included)
    if len(line)==0: break #end of the book
    else:
    wcnt += len(line)
    for x in line: #extract each char and update counting
      if x in D: D[x]+=1
      else: D[x]=1

```
