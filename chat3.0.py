lines = []
with open('3.txt','r') as f:
 for line in f:
 	lines.append(line)

for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print(name)