#program to count all word occurances in a file
filename = input("Enter filename: ")

with open(filename) as f:
    content = f.read().splitlines()

wordlist = []

for h in content:
    words = h.split()
    for j in words:
        if j in dict(wordlist):
            index = [i for i, v in enumerate(wordlist) if v[0] == j]
            wordlist[index[0]][1] += 1
        else:
            wordlist.append([j, 1])

#print out formatted list of words and their count
print("{",end="")
for h in wordlist:
    print("'",h[0],"'",":",h[1],",")
    if h == wordlist[-1]:
        print(h[0],":",h[1],"}")
