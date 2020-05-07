import os
# OS Module contains filepath related functions such as os.path.join()

# os.path.join('folder1', 'folder2', 'folder3', 'file.png')
# => 'folder1//folder2//folder3//file.png'

example = os.path.join('folder1', 'folder2', 'folder3', 'file.png')
# print(example)
# folder1/folder2/folder3/file.png   => Output

getFilePath = os.getcwd()
# print(getFilePath)

#Absolute file path gives a complete file path including the root folder
# Relative file path do not include the root folder
# . stands for this folder
# .. stands for parent folder

# os.chdir(path) to change directory
absolutePath = os.path.abspath('files-filename.py')
# print(absolutePath)

checkAbsolute = os.path.isabs('/files-filename.py')
# print(checkAbsolute)

# relativePath = os.path('path1', 'path2')
# The output would be the path from path2(current directory) to path1(destination directory)
# os.path.dirname and os.path.basename
# os.path.exists(filepath) returns true if it exists

filesize = os.path.getsize('/Users/aimanaaw/automate-with-python/files/')
# print(filesize)

getFolderContents = os.listdir('/Users/aimanaaw/automate-with-python/files')
# print(getFolderContents)

totalSize = 0
pythonFolderSize = os.path.getsize('/Users/aimanaaw/Desktop/python')
# print(pythonFolderSize)

for filename in os.listdir('/Users/aimanaaw/Desktop/python'):
	if not os.path.isfile(os.path.join('/Users/aimanaaw/Desktop/python', filename)):
		totalSize = totalSize + os.path.getsize(os.path.join('/Users/aimanaaw/Desktop/python', filename))

print(totalSize)

# os.makedir('/User/delicious/walnut') it will make a folder called delicious and a folder inside it called walnut