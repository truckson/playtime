# DONE # Peanut Butter Jelly Time!
# DONE # First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich
# DONE # Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make
# DONE # Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )
# DONE # Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches
# DONE # Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life. Wow, your program is kinda judgy.


# What are the step-by-steps to recreate this?
# First, you need variables to store your information. Remember, variables are just containers for your information that you give a name.

# You need three ingredients to make a PB&J, so you'll want three different variables:
#                 How much bread do you have? (make this a number that reflects how many slices of bread you have)
#                How much peanut butter do you have? (make this a number that reflects how many sandwiches-worth of peanut butter you have)
#                How much jelly do you have? (make this a number that reflects how many sandwiches-worth of jelly you have)

# For this exercise, we'll assume you have the requisite tools (plate, knife, etc)

# Once you've defined your variables that tell you how much of each ingredient you have, use conditionals to test whether you have the right amount of ingredients

# Based on the results of that conditional, display a message.

# To satisfy the first goal:
#                If you have enough bread (2 slices), peanut butter (1), and jelly (1), print a message like "I can make a peanut butter and jelly sandwich";
#                If you don't; print a message like "Looks like I don't have a lunch today"

bread=int(raw_input('How many slices of bread do you have?'))
peanut_butter=int(raw_input('How many peanut butters do you have?'))
jelly=int(raw_input('How many jellies do you have?'))
bread_number = (bread / 2)
peanut_butter_number = peanut_butter
jelly_number = jelly
sandwich_number=min(bread_number, peanut_butter_number, jelly_number)
# I want to find something that is odd
open_face_determinant=bread % 2
open_face_number = min(bread,peanut_butter_number,jelly_number)
max_sandwiches_possible = max(bread/2,peanut_butter_number,jelly_number)

if (max_sandwiches_possible - jelly_number) > 0:
	missing_jelly=(max_sandwiches_possible-jelly_number)
else:
	missing_jelly=0
if (max_sandwiches_possible - peanut_butter_number) > 0:
	missing_pb=(max_sandwiches_possible-peanut_butter_number)
else:
	missing_pb=0
if (max_sandwiches_possible - bread_number) > 0:
	missing_bread=(max_sandwiches_possible-bread_number)
else:
	missing_bread=0
more_sandwiches=max_sandwiches_possible-sandwich_number

if open_face_determinant == 1:
	print "I can make {0} open face sandwiches".format(open_face_number)
if sandwich_number >= 1:
	print "I could make {0} full peanut butter sandwiches!".format(sandwich_number)
else:
	if open_face_determinant == 1:
		print("But looks like I don't get any whole sandwiches of pb and j today")
	else:
		print("NO FOOD! for me")
print("And I am missing {0} slices of bread, {1} peanut butters, and {2} jellies to make {3} more whole sandwiches".format(missing_bread,missing_pb,missing_jelly,more_sandwiches))
if missing_bread == 0 and missing_pb == 0 and more_sandwiches > 0:
	print("You can make a peanut butter sandwich but you should take a hard, honest look at your life.")




# To satisfy the second goal:
#                Continue from the first goal, and add:
#                If you have enough bread (at least 2 slices), peanut butter (at least 1), and jelly (at least 1), print a message like "I can make this many sandwiches: " and then calculate the result.
#                If you don't; you can print the same message as before


# To satisfy the third goal:
#                Continue from the second goal, and add:
#                If you have an odd number of slices of bread* and odd amount of peanut butter and jelly, print a message like before, but mention that you can make an open-face sandwich, too.
#                If you don't have enough ingredients; still print the same message as before
#                * To calculate whether you have an odd number, see https://github.com/shannonturner/python-lessons/blob/master/section_01%20%28basics%29/simple_math.py

# To satisfy the fourth goal:
#                Continue from the third goal, but this time if you don't have enough ingredients, print a message that tells you which ones you're missing.

# To satisfy the fifth goal:
#                Continue from the fourth goal, but this time if you have enough bread and peanut butter but no jelly, print a message that tells you that you can make a peanut butter sandwich
#                Or if you have more peanut butter and bread than jelly, that you can make a certain number of peanut butter & jelly sandwiches and a certain number of peanut butter sandwiches

