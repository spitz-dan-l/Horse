
import random

help = ("Acceptable answers are 'yes', 'yeah', and 'fuck yeah'.")
gtfo = ("If you don't like it then 'quit'.")
insults = ["Wrong answer you great idiot, try again. ", "N00b.  Try again.", "What's wrong with you?  Try again. ", "Could you be any lamer? Try again. ", "How does it feel to be so wrong?  Try again. "]

def correctness(herds):
	if herds == "yes":
		return "correct"
	elif herds == "yeah":
		return "correct"
	elif herds == "fuck yeah":
		return "correct"
	else:
		return "failure"


def main():
	print "So, do you love horses?"
	
	only_answer = raw_input("Do you? ")
	
	try:
		only_answer = only_answer.lower()
	
	except:
		print "  "
		print "That's not a word, bozo.  Try again."
		print "  "
		print "You can also type 'help' or 'quit', I guess."
		print "  "
		main()
	
	finally:
		if correctness(only_answer) == str("correct"):
			print "  "
			print "Good choice. "
			print "  "
			print "Horse" * 1000
			print "  "
			print "Now again!"
			print "  "
			print "You can also type 'help' or 'quit', I guess."
			print "  "
			main()
		
		elif only_answer == str("help"):
			print "  "
			print help
			print gtfo
			print "  "
			main()

		elif only_answer == str("quit"):
			quit
		

		else:
			print "  "
			print random.choice(insults)
			print "  "
			print "You can also type 'help' or 'quit', I guess."
			print "  "
			main()


main()