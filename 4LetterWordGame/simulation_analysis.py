import csv

all_nums = []
all_words = []
hard_nums = []
hard_words = []

with open('GuessesAndWords.csv','r') as csvfile:
	reader = csv.reader(csvfile, delimiter = ',')
	
	for row in reader:
		num = int("".join(row[0]))
		word = "".join(row[1])
		all_nums.append(num)
		all_words.append(word)

		if num > 10:
			hard_nums.append(num)
			hard_words.append(word)

### Finding the hardest letter combinations to guess

