##Basic function format reviewed.
##Always declare a function before using it, not after.
##Function parameters and arguments.

##Using keyword arguments to be specific.
##Functions ought to do one thing and do it well. It must 
# also be able to return values of the o/p.

#Exercise - Tesla 
def checkDriverAge():
    age = int(input("Please enter your age please:"), )

    if age < 18:
        print("Sorry, you are too young to drive this car. Powering off.")
    elif age > 18:
        print("Powering on. Enjoy the ride!")
    elif age == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge()

##Methods and Functions.
##Methods are declared using .method(arg) while functions are declared using function(arg)

##Docstrings
## Any info starting  with 3 single quotes and ''' 
# wrefsefawefragagr ''' that is, ending with 3 single quotes 
# is called docstrings
 