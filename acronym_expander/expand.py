# program to expand any acronyms in a sentence, takes input file for key
# to determine what is an acronym or not

filename = "key.dat" 

#get array of data
with open(filename) as f:
		content = f.readlines()

keys = list(map(lambda s : s.strip('\n').split(':'), content))

sentence = input("What did they say? ")

for word in sentence.split():
		for i in keys:
				if word == i[0]:
						print(i[1], end=" ")
						break;
		else:
			print(word, end=" ")
