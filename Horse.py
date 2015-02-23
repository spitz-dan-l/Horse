
import random

help = ("Acceptable answers are 'yes', 'yeah', and 'fuck yeah'.")
gtfo = ("If you don't like it then 'quit'.")
insults = ["Wrong answer you great idiot, try again. ", "N00b.  Try again.", "What's wrong with you?  Try again. ", "Could you be any lamer? Try again. ", "How does it feel to be so wrong?  Try again. "]

def is_correct(herds):
	return herds in ('yes', 'yeah', 'fuck yeah', 'yuss', 'yup')

def main():
	print "So, do you love horses?"
	
	only_answer = raw_input("Do you? ")
	
	only_answer = only_answer.lower()
	
	if is_correct(only_answer):
		print
		print "Good choice. "
		print
		print "Horse" * 1000
		print
		print "Now again!"
		print
		print "You can also type 'help' or 'quit', I guess."
		print
		main()
	
	elif only_answer == "help":
		print
		print help
		print gtfo
		print
		main()

	elif only_answer == "quit":
		quit

	else:
		print
		print random.choice(insults)
		print
		print "You can also type 'help' or 'quit', I guess."
		print
		main()

main()