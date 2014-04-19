# File handling: Most Common Syntax below
# with open("states.txt","r") as states_file: 
	# states=states_file.read()
# print states
	#with keyword similar to a conditional, file will be opened, commands run, file closed
	#open keyword tells python to open file--Argument I: The file you want to open, using relative paths
		# Relative Paths : pathway to your file relative to script you're running. EX. if you're in pyscripts, looks in pyscripts
	#Ways to open a file
		#r: read-only	
		#w: write mode = Watch Out!
			#overwrite the contents - doesn't matter what was there before - deletes old content	
		#a: append mode
			#if file exists, adds new information to the end
			#if doesn't exist, adds a new file
	#The as keyword is used to create a variable out of your file handler #WHAT IS FILE HANDLER
		#The variable in this example is states_file, but you could use any variable name you want.

"""with open("states.csv","r") as states_file: 
	states=states_file.read().split("\n") #states_file.read() together is a string, so you can use .split on it...since .split is a string method
	for index, state in enumerate(states): #first variable is ALWAYS the index value, second variable is ALWAYS the name of the individual string
		states[index]=state.split(",")
		print "{0}'s abbreviation is {1}".format(states[index][1],states[index][0])
"""


only_states=[]
only_abbreviations=[]

with open("states.csv","r") as states_file: 
	states=states_file.read().split("\n")
	for index, state in enumerate(states):
		states[index]=state.split(",") #better to split states into a 2-part list for each states [Abbreviation, Value]
		only_states.append(states[index][1]) #adds the second part (state name) to my list
		only_abbreviations.append(state[0:2]) #adds the first two characters (abbrevation) to my list, could also use the format above with the number 0 instead of 1
print only_states
print only_abbreviations

with open("states.html","w") as new_file:
	new_file.write(str(only_states))


#DICTIONARIES
#creating an empty dictionary
contacts = {}
#with items - items have a key and a value (name, phone)
# the comma tells where to stop, the colon breaks apart items in each list
# this is strings within lists, which are all within the dictionary
contacts = {
'Shannon': '202-555-1234', 'Bridgit': '703-555-9876', 'Christine': '510-666-5555'}
#dictionaries are weird exceptions where indentation is not as important

#reading part of a dictionary
# name[0:5] #Shann #reading strings
# attendees[:0] #Amy, Jen, Julie #reading lists
contacts['Shannon'] # 202-555-1234 #reading part of a dictionary

#adding to a dictionary
contacts['Mel']= '301-222-0101'

#reading from a dictionary (error prone)
#print contacts['Frankenstein'] #get error - "KeyError: 'Frankenstein'"
#let's try again
# print contacts.get['Frankenstein'] #no error - SUPPOSEDLY!

#Dictionaries can contain strings, lists, or other dictionaries.
#Dictionaries do NOT store order.

#phonebook['Mel'] = '301-333-1212' 

#dictionary within dictionary.
contacts = { 
'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner' },
'Anupama': {'phone': '410-333-9876', 'twitter': '@iamtheanupama', 'github': '@apillalamarri'} 
}

#print contacts['Shannon']['github'] #will this work? yes
"""
# Looping through contacts by keys:
for contact in contacts.keys():
	print contact #this prints the key name of each (in a list)
	print contacts[contact] #this prints the entire list for each contact/key

#If you want to sort
for contact in sorted(contacts.keys()): # sorted() is a built-in function that sorts a list.
	print contact
"""
"""
for contact_info in contacts.values(): # will give us a list of all values in that dictionary # in this case values ARE dictionary, so will print dictionary
	print contact_info
"""
#.items - best of both worlds! keys and values
for contact, info in contacts.items(): #.items() creates a nested list of the key and values of that dictionary, which you can then loop over
	print contact, info
	exercise 2 below:
print "{0}'s contact information is:\n\tPhone: {1}\n\tTwitter: {2}\n\tGithub: {3}".format(contact,info['phone'],info['twitter'],info['github'])

for contact in contacts:
	print "{0}'s contact information is:\n\tPhone: {1}\n\tTwitter: {2}\n\tGithub: {3}".format(contact,contacts[contact]['phone'],contacts[contact]['twitter'],contacts[contact]['github'])	
#can do it EITHER way. different ways to sort dictionaries