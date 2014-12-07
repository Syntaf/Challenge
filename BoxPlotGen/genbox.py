#program to generate box plots from a given set of data,
#then visually display box plot

from math import ceil

#function that accepts indices and splits the data accordingly
def partition(alist, indices):
		return [alist[i:j] for i, j in zip([0]+indices, indices+[None])]

def printBars(alist, indices):
		for i in range(0, len(content)):
				num = int(content[i])
				n = len(content[i])
				if i in(indices[1]-1, indices[0]-1, indices[2]-1):
						print(" " * (n-1) + "|", end=" ")
				elif num < lowerbound:
						print(content[i], end=" ")
				elif num > upperbound:
						print(content[i], end= " ")
				else:
						print(" " * n, end=" ")
		print("")

def printBoxTop(alist, indices):
		for i in range(0, len(content)):
				n = len(content[i])
				if content[i] > content[indices[0]-1]:
						if content[i] <= content[indices[2]-1]:
								print("_" * (n+1), end="")
				else:
						print(" " * n, end=" ")
		print("")

filename = input("Enter filename: ")
print("")

#get data into string
with open(filename) as f:
		content = f.read().split()
count = len(content)

#find indices for splitting array into quarters
indices = [
				int((ceil(count/4) * 4)/4), 
				int((ceil(count*2/4) * 4)/4),
				int((ceil(count*3/4) * 4)/4),
				int((ceil(count*4/4) * 4)/4)
			]

#split list into quartiles
chunks = partition(content, indices)

iqr = int(content[indices[2]-1]) - int(content[indices[0]-1])
lowerbound = int(content[indices[0]-1]) - 1.5*iqr
upperbound = int(content[indices[2]-1]) + 1.5*iqr

printBoxTop(content, indices)
printBars(content, indices)

for stringnum in content:
		num = int(stringnum)
		n = len(stringnum)
		if num < lowerbound:
				print("X"," " * (n-1),sep="",end=" ")
		elif num > upperbound:
				print("X"," " * (n-1),sep="",end=" ")
		else:
				print(num,end=" ")
