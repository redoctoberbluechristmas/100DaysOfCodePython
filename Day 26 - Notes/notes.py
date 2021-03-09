


# Traditional way of iterating every list member
numbers = [1, 2, 3]
new_list = []

for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)

# List comprehension way to do the same thing.
# keyword method - type out keywords and replace.
# new_item is the code that you want to execute on all the list members.
new_list =[new_item for item in list]
new_list = [n + 1 for n in numbers]


# Use list comprehension on a range.
doubled_range = [num * 2 for num in range(1,5)]


# conditional list comprehension

new_list = [new_item for item in list if test]

even_numbers = [number for number in numbers if number % 2 == 0]

big_names = [name.upper() for name in names if len(name) > 4]



# Read/compare challenge

file1 = open("file1.txt", mode="r")
file1 = file1.readlines()
#print(file1)

file2 = open("file2.txt", mode="r")
file2 = file2.readlines()
#print(file2)

result = [int(n) for n in file1 and file2 if n in file1 and file2]


# Write your code above 👆
print(result)


# Read/compare challenge


with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()


result = [int(n) for n in file_1_data if n in file_2_data]

# Write your code above 👆
print(result)




