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
		print(h," ", end="")
		pref = trie.prefixes(h)
		print(pref)

print(maxword)

