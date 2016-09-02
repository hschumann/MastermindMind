import random
import csv

reps = int(raw_input("How many repetitions do you want to do? : "))

fo = open('GuessesAndWords650.csv','a')

for y in range(reps):
	all_words = []
	master_list = []

	with open('FourLetterUse.csv', 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			all_words.append(row)
			master_list.append(row)
		all_words.pop(0)
		master_list.pop(0)

	my_word = "".join(all_words[random.randrange(len(all_words))])
	letters = list(my_word)

	num_guesses = 0
	while True:
		num_guesses += 1
		"""
		if num_guesses < 3:
			index = random.randrange(len(master_list))
			cpuGuess = "".join(master_list[index])
			guess_letters = list(cpuGuess)
		"""
		if len(all_words) > 650:
			index = random.randrange(len(master_list))
			cpuGuess = "".join(master_list[index])
			guess_letters = list(cpuGuess)
		
		else:
			index = random.randrange(len(all_words))
			cpuGuess = "".join(all_words[index])
			guess_letters = list(cpuGuess)
			all_words.pop(index)

		if cpuGuess == my_word:
			break
		
		lets = 0
		for l in guess_letters:
			if l in letters:
				lets += 1

		if lets == 0:
			x = 0
			while x < len(all_words):
				l = list(str(all_words[x]))
				in_ = False
				for char in guess_letters:
					if char in l:
						in_ = True
				if in_ == True:
					all_words.pop(x)
				else:
					x += 1

		else:
			x = 0
			while x < len(all_words):
				l = list(str(all_words[x]))
				in_ = 0
				for char in guess_letters:
					if char in l:
						in_ += 1
				if in_ < lets:
					all_words.pop(x)
				elif in_ > lets:
					all_words.pop(x)
				else:
					x += 1
	"""
	print "It took " + str(num_guesses) + " guesses. The word was " + my_word
	"""
	fo.write(str(num_guesses) + "," + my_word + "\n")

fo.close()
