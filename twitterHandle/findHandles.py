# program designed to find all viable twitter handles in text file

filename = input("Enter a file name: ")

#get array of data
print("Reading data...")
with open(filename) as f:
		content = f.readlines()
print("Done...\n")

#strip each line in content so it does not contain '\n'
content = map(lambda s: s.strip(), content)
validhandles = [""]

print("Finding valid handles...")
#determining valid twitter handles...
for h in content:
		pos = h.find("at")
		#if the at symbol is found at the start of the word
		if pos == 0 and len(h) <= 15:
			validhandles.append(h)
print("done...")

validhandles.sort(key = lambda s: len(s))

f = open("out.txt", "w")

print("list of valid handles alphabetical order")
for h in validhandles:
	print("@".join(h.split("at")).ljust(15), end="")
	print((" : " + h))
	f.write("@".join(h.split("at")).ljust(15) + (" : " + h) + "\n")
print("done... out.txt")
f.close()
