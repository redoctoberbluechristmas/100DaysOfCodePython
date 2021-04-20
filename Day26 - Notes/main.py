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