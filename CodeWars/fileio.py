# jabber = open("sample.txt",'r')

# for line in jabber:
# 	if 'jabberwock' in line.lower():
# 		print(line, end = '')

# jabber.close()

#Use of 'with' so if there is an error, the file closes

# with open("sample.txt", 'r') as jabber:
# 	for line in jabber:
# 		if 'JAB' in line.upper():
# 			print(line, end = "")

# with open('sample.txt', 'r') as jabber:
# 	 line = jabber.readline()
# 	 while line:
# 	 	print(line,end= '')
# 	 	line = jabber.readline()

with open('sample.txt', 'r') as jabber:
	 lines = jabber.readlines()
	 print(lines)

for line in lines:
	print(line, end = '')
