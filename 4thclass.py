age=21
int(age)

# .get > looks for the key, if it doesn't find it, gives you error

"""
def something(parameters) # def > I want to define a function
...code
return  # tells code to stop using function

#EXAMPLE
#list() converts an item to a list
#set() converts to a set > set is similar to a list, but all values are unique
# converting list to a set removes all duplicate values. then we convert it back to a list since we like those

L = [1,2,3,4,5,2,6,5,7,8,9,10] #this is a list

def remove_duplicates(from_list): #this is you defining a function to remove duplicates, from_list is variable you put in
	from_list = list(set(from_list)) #converts your list to a set (of unique values) and back to a list
	return from_list #puts out and ends function

n = remove_duplicates(L)
print n
"""

#Create a function that will return a string containing 'Hello, <name>!' 
#So when you call the function like this: 
#print greeting('Shannon') 
#This should happen in response: 
#Hello, Shannon!
"""
name=raw_input('What is your name?')

def say_hello(input_name):
	#input_name="Hello, {0}!".format(input_name)
	#return input_name
	#OR
	#return "Hello, {0}!".format(input_name)
	#OR
	print "Hello, {0}!".format(input_name) # there is a hidden return at the end if you don't include it (return None)
say_hello(name)
"""
"""
def textfile_to_string(filename):
	with open(filename, "r") as text_file: 
 		text = text_file.read()
 	return text

contents=textfile_to_string('states.txt')
print contents


def open_csvfile(filename,delimiter='\t'): #open_csvfile assumes your values ar separated by tabs (could also be commas)
#if your function definition has default vaues, they must appear at the end!
def open_csv(delimiter=',''filename): #will not work
def scan_file(filename, deduplicate=True): #will work
def upload_events(events_file, location): # is right! whatever order you ddefine your parameters in, has to be in that or
upload_events (location, events_file) #wrong!
upload_events(location=location,events_file=events_file) #this is a way around it!! yay!
"""
#RETURN VALUE > syntax > return_value=function(parameter, other parameters)
#return does 2 things: gives value back, and ends the function
#can have multiple return values
#can have return value of None
"""
def product(x,y):
	return x*y

print product(8,6)
"""

def division(x, y):
    if y == 0:
        return # You can't divide by Zero! If you do, you'll get an error.
    return x/y # It's implied that this only happens when y != 0, since otherwise the function would have ended at line 3
print division (2,1.3)
#don't need ELSE, because function stops as SOON as you return


