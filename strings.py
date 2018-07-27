strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''
for i in strings:
	sentence = sentence + i + " "

print(sentence)
print(' '.join(strings))

