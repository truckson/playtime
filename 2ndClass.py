# Class 2
# print """She said "Hello" when I asked her to speak 'something nice' in French"""
# print "What is new \nNot much"

# Lists - here is what they are
name1='Karin'
name2='Jen'
name3='Bob'
names=[name1,name2,name3]
# or
names2=['Karin','Jen','Bob'] # this is a list
# print names
# print names2
if names==names2:
	pass # this lets you pass by, you should delete it if you want to us the if statement again
	# print("they're equal!")
# print("an empty list looks like this")
nonames = []
# print(nonames)
# print(names[1:3]) #Jen #Bob
# print(names[2]) #Bob

# print len(names) #3
# number_of_names=len(names)
# print(number_of_names) #3

# names.append('Jimmy')
# print(names)

attendees_ages=[]
attendees_ages.append(28)
attendees_ages.append(29)
# print attendees_ages
# print attendees_ages[0]

days_of_week=['Monday','Tuesday']
days_of_week.append('Wednesday')
# print days_of_week
# print len(days_of_week)

day=days_of_week.pop(0) # pop takes off the last one, unless you specify: 0 specifies Monday
# print day
# print days_of_week

days_of_week.extend(['Wednesday','Thursday','Friday','Saturday','Sunday'])
# print days_of_week

days_of_week.insert(0,'No Day')
# print days_of_week

address = "1133 19th Street NW Washington, DC 20036"
address_as_list = address.split(" ")
# print address_as_list
# if 'Frankenstein' in 'python class':
	# print "true"
# else:
	# print "false"

Northwest=[]
Northeast=[]
Southeast=[]
Southwest=[]
Needs_Quadrant=[]

# user_address1=raw_input('Please type in your 1st address: ')
#user_address2=raw_input('Please type in your 2nd address: ')
#user_address3=raw_input('Please type in your 3rd address: ')

#addresses=[user_address1,user_address2,user_address3]

# raw_input # bread=raw_input("how many breads?")

"""for ind_number in ['1st','2nd','3rd']: #for loops are great. use it to run something several times
	ind_address=raw_input('Please type in your {0} address: '.format(ind_number))
	if 'NW' in ind_address:
		Northwest.append(ind_address)
	elif 'NE' in ind_address:
		Northeast.append(ind_address)
	elif 'SE' in ind_address:
		Southeast.append(ind_address)
	elif 'SW' in ind_address:
		Southwest.append(ind_address)
	else:
		Needs_Quadrant.append(ind_address)

print Northwest
print Northeast
print Southeast
print Southwest
print Needs_Quadrant"""

# lists: ranges of numbers
# Most common: range from 0 to range (5)
# most_common=range(0,5)
# print most_common
# most_common2=range(10)
# print most_common2
# for number in range(10):
# 	print number

len_of_each_day = []

for i_day in enumerate(days_of_week):
	if len(i_day) == 6:
		len_of_each_day.append(len(i_day))
	else:
		pass
		# days_of_week.replace(i_day,"snufflenufflegus")
print len_of_each_day
print days_of_week

for week in range(1,5):
	print "Week {0}".format(week)
for day in days_of_week:
	print day


