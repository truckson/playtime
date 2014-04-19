# Challenge level: Beginner

# Scenario: You have two files containing a list of email addresses of people who attended your events.
# File 1: People who attended your Film Screening event
# https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/film_screening_attendees.txt
#
# File 2: People who attended your Happy hour
# https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/happy_hour_attendees.txt

# Note: You should create functions to accomplish your goals.
# Goal 1: You want to get a de-duplicated list of all of the people who have come to your events.
# Goal 2: Who came to *both* your Film Screening and your Happy hour?


with open('happy_hour_attendees.txt','r') as hh_file:
	hh_list=hh_file.read().split("\n")
with open('film_screening_attendees.txt','r') as fs_file:
	fs_list=fs_file.read().split("\n")

def de_duplicate(list1,list2):
	full_list=list1+list2
	unique_attendees=list(set(full_list))
	return unique_attendees
#print de_duplicate(hh_list,fs_list)
#GOAL 1 BABY!!!

def find_overlap(list1,list2):
	matches=[]
	match=[]
	for index, email in enumerate(list1):
		list1[index]=email
		if email in list2:
			match=email
		if match!=[]:
			matches.append(match)
	for index, email in enumerate(list2):
		list2[index]=email
		if email in list1:
			match=email
		if match!=[]:
			matches.append(match)
	matches =list(set(matches))
	print matches

find_overlap(fs_list,hh_list)




