import csv
import random

all_words = []
master_list = []

with open('FourLetterUse.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		all_words.append(row)
		master_list.append(row)
	all_words.pop(0)
	master_list.pop(0)

print "Let's Begin a Game."

while True:
	resp = raw_input("Type 'a' to begin. Type '?' for the rules : ")
	if resp not in ('a','?'):
		print "I'm sorry, that is Invalid Input"
	if resp == '?':
		print "We will each guess a four letter word with no repeating letters.  After guessing, we will tell" \
			+ " each other how many letters were correct in that word.  We will alternate turns until there is a winner." \
			+ " Note that all guesses must be real words as well."
		print "\n"
	elif resp == 'a':
		break
	
print "Let's begin the game then."
print "You may go first. \n"

cpuWord = "".join(all_words[random.randrange(len(all_words))])
letters = list(cpuWord)

#guessed_words = []

while True:
	isAword = False
	while not isAword:
		guess = raw_input("What's your guess : ")
		guess = guess.upper()
		guess_letters = list(guess)

		n = 0
		while n < len(master_list):
			the_word = [guess]
			if the_word == master_list[n]:
				isAword = True
				break
			n += 1

		if not isAword:
			print "I'm sorry, that is not a valid word. Try again. \n"

	num_correct = 0
	for l in guess_letters:
		if l in letters:
			num_correct += 1

	print "You got " + str(num_correct) + " letters correct."

	if guess == cpuWord:
		print "CONGRATULATIONS YOU WIN!"
		break

	print "\n"
	"""
	if len(all_words) > 500:
		index = random.randrange(len(master_list))
		cpuGuess = "".join(master_list[index])
		guess_letters = list(cpuGuess)
	"""
	
	index = random.randrange(len(all_words))
	cpuGuess = "".join(all_words[index])
	all_words.pop(index)

	print "My guess is: " + cpuGuess
		
	cor = ""
	while True:
		cor = raw_input("Is that correct? (y/n) : ")
		cor = cor.upper()
		if cor in ('Y','N'):
			break
		print "I'm sorry, that is an invalid answer. \n"

	if cor == 'Y':
		print "YOU LOSE"
		print "My word was " + cpuWord
		break
	
	while True:
		try:
			lets = int(raw_input("How many letters were correct? : "))
			if not 0 <= lets <= 4:
				raise ValueError()
			break
		except ValueError:
			print "I'm sorry, the answer must be an answer between 0 and 4."


	print len(all_words)

	cpuGuess_letters = list(cpuGuess)

	if lets == 0:
		x = 0
		while x < len(all_words):
			l = list(str(all_words[x]))
			in_ = False
			for char in cpuGuess_letters:
				if char in l:
					in_ = True
			if in_:
				all_words.pop(x)
			else:
				x += 1

	else:
		x = 0
		while x < len(all_words):
			l = list(str(all_words[x]))
			in_ = 0
			for char in cpuGuess_letters:
				if char in l:
					in_ += 1
			if in_ < lets:
				all_words.pop(x)
			elif in_ > lets:
				all_words.pop(x)
			else:
				x += 1
	
	print len(all_words)
	print "\n"
