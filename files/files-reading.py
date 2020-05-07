# Plaintext files with no info of fonts, styles
import os, shelve
helloFile = open('/Users/aimanaaw/automate-with-python/files/hello.txt')
fileText = helloFile.read()
helloFile.close()
# print(fileText)


helloFile1 = open('/Users/aimanaaw/automate-with-python/files/hello.txt')
content = helloFile1.readlines()
# print(content)
helloFile1.close()

helloFile2 = open('/Users/aimanaaw/automate-with-python/files/hello.txt', 'w')
content2 = helloFile2.write('Hello!!!!!!!')
# print(content2)
helloFile2.close()

# print(os.getcwd())
chickenFile = open('chicken.txt', 'a')
chickenFile.write('\n\nChicken is delicious.')
chickenFile.close()

# Shelve module
# Shelve module allows you to add other data structures to files. You can treat a shelf file like a dictionary
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
# shelfFile.close()
print(list(shelfFile.keys()))
print(list(shelfFile.values()))