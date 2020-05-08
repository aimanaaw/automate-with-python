# Writing code that applies to an entire folder
import os

folderPath = os.path.abspath('folder1')
# print(folderPath)

# os.walk(folderPath) returns a value used in for loops

for folderName,subfolders, filenames in os.walk(folderPath):
	# You can run further loops inside for each array of subfolders, filenames
	# You can perform operations like check if exists, delete, move
	print('The folder is ' + folderName)
	print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
	print('The filenames in ' + folderName + ' are: ' + str(filenames))
	print()