#!//anaconda/bin/python

from itertools import takewhile

def fizzbuzz(num):
	if num % 3 == 0 and num % 5 == 0:
		return "fizzbuzz"
	elif num % 3 == 0:
		return "fizz"
	elif num % 5 == 0:
		return "buzz"
	else:
		return str(num)

def generateList():
	num = 1
	while True:
		yield num
		num += 1

def main():
	num_seq = generateList()
	numbers = takewhile(lambda n: n < 100, num_seq)
#	numbers = takewhile(lambda n: n < 1000, num_seq)

	for i in list(numbers):
#		print(i)
		print(fizzbuzz(i))


if __name__ == "__main__":
	main()