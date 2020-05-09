import traceback

'''

*********
*		*
*		*
*		*
*********

'''

def boxPrint(symbol, width, height):
	if len(symbol) != 1:
		raise Exception('Symbol needs to be length 1')

	if (width < 2) or (height < 2):
		raise Exception('Width and height needs to be greater than 2')
	print(symbol * width)

	for i in range(height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)

	print(symbol * width)


# boxPrint('x', 1, 1)
# traceback.format_exc()
