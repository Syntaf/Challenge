# Given a dictionary file, find the word in the file which also contains
# the greatest number of words within that word

#trie tree impl
import marisa_trie

filename = input("Enter filename: ")

#get array of data
with open(filename) as f:
	content = f.read().splitlines()

#create trie
trie = marisa_trie.Trie(content)

maxword = ""
maxcount = 0

#loop through content and determine all prefixes present in word
for h in content:
    word = h
    pref = trie.prefixes(word)
    #loop through such that each character is considred the start
    #once 
    while len(word) > 1:
        word = word[1:]
        cutpref = trie.prefixes(word)
        pref.append(cutpref)    
    #replace new highest word if true
    count = len(pref)
    if count > maxcount:
        maxcount = count
        maxword = h    

print(maxword)

