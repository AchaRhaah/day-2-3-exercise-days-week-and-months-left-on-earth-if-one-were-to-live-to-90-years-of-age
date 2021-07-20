# a program to calulate the days weeks and months left if one were to live to 90 years old
# age is a string
age = input("What is your current age?
#we have to type cast age to int to carry out this operation
weeksLeft=(90-int(age))*52
daysLeft=(90-int(age))*365
monthsLeft=(90-int(age))*12
# We use f strings to print a other data types in a string
message=f"you have {weeksLeft} weeksLeft,{daysLeft} daysLeft, {monthsLeft} month"
print(message)












