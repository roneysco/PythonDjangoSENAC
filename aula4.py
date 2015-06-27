''' A1

file1 = open('numbers.txt', 'w')

for line in range(1, 101):
	file1.write('%d\n' % line)

file1.close()'''

''' A2
text = open('message.txt', 'r')
output = open('crypto.txt', 'w')

for line in text.readlines():
	for letter in line:
		if letter in 'aeiou':
			output.write('*')
		else:
			output.write(letter)

text.close()
output.close()'''

file2 = open("surf.txt", "r")
scores = {}

for line in file2:
	name, score = line.split()
	scores[float(score)] = name
file2.close()

scoreSum = 0
for score in sorted(scores, reverse=True): #sort by score
	scoreSum += score
	print("%s has score %4.2f" % (scores[score], score))

scoreAvg = scoreSum/len(scores)
print(scoreAvg)