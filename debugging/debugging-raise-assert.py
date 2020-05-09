# import traceback

# '''

# *********
# *		*
# *		*
# *		*
# *********

# '''

# def boxPrint(symbol, width, height):
# 	if len(symbol) != 1:
# 		raise Exception('Symbol needs to be length 1')

# 	if (width < 2) or (height < 2):
# 		raise Exception('Width and height needs to be greater than 2')
# 	print(symbol * width)

# 	for i in range(height - 2):
# 		print(symbol + (' ' * (width - 2)) + symbol)

# 	print(symbol * width)


# # boxPrint('x', 1, 1)
# # traceback.format_exc()

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
	for key in stoplight.keys():
		if stoplight[key] == 'green':
			stoplight[key] = 'yellow'
		elif stoplight[key] == 'yellow':
			stoplight[key] = 'red'
		elif stoplight[key] == 'red':
			stoplight[key] = 'green'

	assert 'red' in stoplight.values(), 'Neither light is red' + str(stoplight)


print(market_2nd)
switchLights(market_2nd)
print(market_2nd)

print(mission_16th)
switchLights(mission_16th)
print(mission_16th)