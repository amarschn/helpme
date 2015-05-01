import time
import sys

def helpme():
	count = 0

	while True:
		time.sleep(1)
		if count / (25 * len("help me ")) == 0:
			sys.stdout.write("help me ")
			sys.stdout.flush()
		else:
			print ""
			count = 0
		count += len("help me ")


if __name__ == '__main__':
	helpme()