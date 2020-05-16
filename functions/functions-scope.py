# spam = 42

# def eggs():
# 	spam = 5
# 	print('spam inside eggs()', spam)
# 	return spam

# print(spam)
# print(eggs())
# print(spam)

# Global variables do not have access to a functions local scope
# Local variables have access to the global scope
# One functions local scope variables does not have access to another functions local scope variables
# You can use the same name for different variables if they are in different scopes

# def spam():
# 	eggs = 99
# 	chicken()
# 	print(eggs)

# def chicken():
# 	beef = 101
# 	eggs =  #chicken() eggs is separate to spam() eggs

# spam()

# def spam():
# 	eggs = 99 # if this local statement isn't present, python will use the global eggs variable
# 	print(eggs)

# eggs = 42
# spam()
# print(eggs)


# To assign a new value to a global variable from inside a function
def spam():
	global eggs #Tells python that the global variable will be used
	eggs = 99 
	print(eggs)

eggs = 42
spam()
print(eggs)