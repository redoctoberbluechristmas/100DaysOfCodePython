#Functions with outputs

# f_name = input("What is your first name? ")
# l_name = input("What is your last name? ")

def format_name(first_name, last_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if first_name == "" or last_name == "":
        return "Sorry, can't do it."
    
    formated_f_name = first_name.title()
    formated_l_name = last_name.title()

    # Use return keyword to specify what is returned by your function.
    # Everything after return keyword will replace where the function was called.
    return f"{formated_f_name} {formated_l_name}"


# Save the output of your function call in a variable.
# output_storing_variable = format_name(f_name, l_name)
output_storing_variable = format_name(input("What is your first name? "), input("What is your last name? "))
print(output_storing_variable)

OR
# 
#print(format_name(f_name, l_name))

#Var, which stores output    function, returns output           input
output =                      len                            ( "Hello" )




#Multiple return values

# return tells function that this is the end of function.


# Docstrings

# Create documentation as going along - intellisense.

def