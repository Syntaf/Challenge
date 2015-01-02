#program to map specific directories to other directories

filename = input("Enter filename: ")

#get data into string
with open(filename) as f:
		content = f.read().split()

#the first line of our file is how many lines we need to read in
num = content[0]
del content[0]

print(content)
