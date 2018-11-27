# Write a program to append the times tables to our jabberwacky poem
# in simple.txt. We want the tables from 2 to 12 (similar to the output)
# from the For loops part 2 in section 61

# The first column of numbers should be right justified. As an example,
# the 2 times table should look like this:

	# 1 times 2 is 2
	# 2 times 2 is 4
	# 3 times 2 is 6
	# 4 times 2 is 8
	# 5 times 2 is 10
	# 6 times 2 is 12
	# 7 times 2 is 14
	# 8 times 2 is 16
	# 9 times 2 is 18
	# 10 times 2 is 20
	# 11 times 2 is 22
	# 12 times 2 is 24

lines = []
with open('sample.txt', 'a') as sample_file:
	for i in range(1,13):
		tv = i*2
		if(i < 10):
			print(" {0} times 2 is {1}".format(i, tv), file=sample_file)
		else:
			print("{0} times 2 is {1}".format(i, tv), file=sample_file)
