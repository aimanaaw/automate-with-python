import logging

logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# If you want to write the logs to a file, add the filename parameter to the loggin.basicConfig function
# logging.basicConfig(filename='myProgramming.txt', level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# logging.disable(logging.CRITICAL)

# LOG LEVELS:
# debug(lowest)
# info
# warning
# error
# critical(highest)

logging.debug('Start a program')


def factorial(n):
	logging.debug('Start of factorial(%s)' % (n))
	total = 1
	for i in range(1, n + 1):
		total *= i
		logging.debug('i is %s, total is %s' % (i, total))
	logging.debug('Return value is %s' % (total))
	return total

print(factorial(5))

logging.debug('End of program')