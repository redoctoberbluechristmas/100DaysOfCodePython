# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Convert string input into simple, 2 index list.
inputindices = list(position)

# Cast input to int, so can be referenced in map below.
row_coord = int(inputindices[0])
column_coord = int(inputindices[1])

#Logging.
print(f"{row_coord} is row.")
print(f"{column_coord} is the column.")

map[row_coord][column_coord] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")