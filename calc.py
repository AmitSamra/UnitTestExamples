def add(x,y):
	return x+y

def subtract(x,y):
	return x-y

def multiply(x,y):
	return x*y

def divide(x,y):
	if y == 0:
		raise ValueError('Cannot devide by zero!')
	else:
		return x/y

def power(x,y):
	return x**y

def hello(name):
	print(f"Hello {name}")

