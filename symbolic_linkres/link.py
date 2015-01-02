#program to map specific directories to other directories

filename = input("Enter filename: ")

#get data into string
with open(filename) as f:
		content = f.readlines()

#the first line of our file is how many lines we need to read in
num = int(content[0])
#remove first element from content
del content[0]

#run the loop NUM times to create symbolic links
for i in range(0,num):
	dirs = content[i].strip('\n').split(':')
	print(dirs)
