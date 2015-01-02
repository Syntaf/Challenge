#program to map specific directories to other directories

filename = input("Enter filename: ")

#get data into string, strip newline characters
with open(filename) as f:
		content = f.readlines()
content = list(map(lambda s : s.strip('\n'), content))

#the first line of our file is how many lines we need to read in
num = int(content[0])
del content[0]

#create list of links and names
links = list()
dirs = list()

#run the loop NUM times to create symbolic links
for i in range(0,num):
	tmp_dirs = content[i].split(':')
	#if not in your links ilst
	if not tmp_dirs[0] in dirs:
			dirs.append(tmp_dirs[0])
			links.append(tmp_dirs[1])
	#else update links
	else:
			for h in range(0,len(dirs)):
					if dirs[h] == tmp_dirs[0]:
							links[h] = tmp_dirs[1]

#get last element and print starting dir
dir = content[-1]
print(dir)
#loop through all of our possible directories, establish where
#our dir is and print the symbolic link
for r in range(0,len(dirs)):
		paths = dir[1:].split('/')
		for i in range(len(paths), 0, -1):
				if set(paths[:i]).issubset(dirs[r][1:].split('/')):
						last = links[r] + "/" + "".join(paths[i])
						break

print(last)
