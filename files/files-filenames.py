import os
# OS Module contains filepath related functions such as os.path.join()

# os.path.join('folder1', 'folder2', 'folder3', 'file.png')
# => 'folder1//folder2//folder3//file.png'

example = os.path.join('folder1', 'folder2', 'folder3', 'file.png')
print(example)
# folder1/folder2/folder3/file.png   => Output

getFilePath = os.getcwd()
print(getFilePath)