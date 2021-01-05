#Functions with outputs

f_name = input("What is your first name? ")
l_name = input("What is your last name? ")

def format_name(f_name, l_name):
    f_name.lower()
    f_name[0].upper()

    l_name.lower()
    f_name[0].upper()

normalized_names = format_name

print(normalized_names)
