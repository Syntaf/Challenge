# checks a 10 digit number and tells the user whether the number is a 
# valid ISBN

raw_isbn = input("What is the ISBN? ")

# obtain just the digits
isbn = ''.join(i for i in raw_isbn if i.isdigit())

if len(isbn) != 10:
		print("Invalid length of ISBN")
		quit()

isbn_list = list(map(int, list(isbn)))

sum = 0
for i in range(10, 0, -1):
	sum += isbn_list[10-i] * i

if sum % 11 == 0:
	print("Valid ISBN!")
else:
	print("Invalid ISBN, remainder is not zero")
