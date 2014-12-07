#program to generate box plots from a given set of data,
#then visually display box plot

from math import ceil

#function that accepts indices and splits the data accordingly
def partition(alist, indices):
		return [alist[i:j] for i, j in zip([0]+indices, indices+[None])]

def printBars(alist, indices):
		for i in range(0, len(alist)):
				num = int(alist[i])
				n = len(alist[i])
				if i in (indices[1]-1, indices[0]-1, indices[2]-1):
						print(" " * (n-1) + "|", end=" ")
				elif num < lowerbound:
						print(alist[i], end=" ")
				elif num > upperbound:
						print(alist[i], end= " ")
				else:
						print(" " * n, end=" ")
		print("")

def printBoxTop(alist, indices):
		for i in range(0, len(alist)):
				num = int(alist[i])
				n = len(alist[i])
				if num == int(alist[indices[0]-1]):
						print(" " * (n-1) + "_", end="_")
				elif num == int(alist[indices[2]-1]):
						print("_" * (n-1) + "_", end=" ")
				elif num > int(alist[indices[0]-1]):
						if num < int(alist[indices[2]-1]):
								print("_" * (n+1), end="")
				else:
						print(" " * n, end=" ")
		print("")


def printLowerBars(alist, indices):
		for i in range(0, len(alist)):
				num = int(alist[i])
				n = len(alist[i])
				if i == indices[0]-1:
						print(" " * (n-1) + "|", end="_")
				elif i == indices[1]-1:
						print("_" * (n-1) + "|", end="_")
				elif i == indices[2]-1:
						print("_" * (n-1) + "|", end=" ")
				elif num >= int(alist[indices[0]-1]):
						if num < int(alist[indices[2]-1]):
								print("_" * (n+1),end="")
				else:
						print(" " * n, end=" ")

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
print("")

printLowerBars(content, indices)
