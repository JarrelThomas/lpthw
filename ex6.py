types_of_people = 10 #assigns the variable of types of people with the value of 10
x = f"There are {types_of_people} types of people." #assigns the variable of x formatting the string to insert the varible types of people into the value


binary = "binary" #assigns the variable binary with the value of the same name
do_not = "don't" #assigns the variable do not with value of don't
y = f"Those who know {binary} and those who {do_not}." #assigns the y varibale with a formatted string to include the previous two varibles

print(x) #prints x variable
print(y) #prints y variable

print(f"I said: {x}") #prints formatted string with the x variable
print(f"I also said: '{y}'") #prints formatted string with y variable

hilarious = False #assigns hilarious varible with False value
joke_evaluation = "Isn't that joke so funny?! {}" # Assigns joke_eva..... variable with string and empty variable to insert one in later

print(joke_evaluation.format(hilarious)) #prints variable joke with the format syntax in order to insert hilarious variable

w = "This is the left side of..." 
e = "a string with a right side."

print(w + e)