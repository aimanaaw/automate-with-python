def div42by(divideBy):
	try:
		return 42 / divideBy
	except ZeroDivisionError:
		# Specific to zero division error. If not specified, it will catch any error
		print('Error: you tried to divide by 0')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
