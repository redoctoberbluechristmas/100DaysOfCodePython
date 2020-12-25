# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

inputindices = list(position)

print(f"These are the {inputindices}")

row_coord = (int(inputindices[0]) - 1)
column_coord = (int(inputindices[1]) -1)

print(f"{row_coord} is row.")
print(f"{column_coord} is the column.")

map[column_coord][row_coord] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")