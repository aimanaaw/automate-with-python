import shutil, os

test1 = os.path.abspath('testingCopy.py')
print(test1)
shutil.copy('/Users/aimanaaw/automate-with-python/files/folder1/testingCopy.py', './folder2/spam1.py')

# shutil.copytree will move a folder and all its content
# shutil.copytree('folder', 'new_folder')


shutil.move('./folder2/spam1.py', './folder1')