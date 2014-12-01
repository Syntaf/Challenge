# Given a dictionary file, find the word in the file which also contains
# the greatest number of words within that word

#trie tree impl
import marisa_trie

filename = "enable1.txt"

#get array of data
with open(filename) as f:
	content = f.read().splitlines()

#create trie
trie = marisa_trie.Trie(content)

#loop through content and find prefixes of word, keep track of biggest word
maxword = ""
maxcount = 0
for h in content:
    tmp = h
    pref = trie.prefixes(tmp)
    for i in range(len(h) - 1):
        tmp.remove(0)
        preftmp = trie.prefixes(tmp)
        pref.append(preftmp)
    count = len(pref)
    print(pref)
    if count > maxcount:
        maxcount = count
        maxword = h    

print(maxword)

