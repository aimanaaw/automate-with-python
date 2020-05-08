import os, shutil, send2trash

# os.unlink('bike.py') to delete file

# os.rmdir('foldername') if the folder is empty
# shutil.rmtree('foldername') to delete a folder and all of its content

# os.chdir('filePath')

# for filename in os.listdir():
# 	if filename.endswith('.txt'):
		# os.unlink(filename)
# 		print(filename)

# Run the above loop to delete a file but comment out the delete(unlink) action
# This lets you check the file names on your console before deletion

# send2trash module
# Needs to be installed using the pip installer

# Send2Trash.send2trash()
filePath = os.path.abspath('folder1/spam.py')
print(filePath)
# send2trash.send2trash('/Users/aimanaaw/automate-with-python/files/folder1/spam1.py')