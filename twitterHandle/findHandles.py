# program designed to find all viable twitter handles in text file

filename = input("Enter a file name: ")

#get array of data
print("Reading data...")
with open(filename) as f:
		content = f.readlines()
print("Done...\n")

#strip each line in content so it does not contain '\n'
content = map(lambda s: s.strip(), content)

#determining valid twitter handles...
for h in content:
		pos = h.find("at")
		if pos != -1:
				print("@".join(h.split("at")), end="")
				print(" : ", h)
