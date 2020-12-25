print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

love_score = 0

#Standardize name for count block
combined_name = name1 + name2
combined_name = combined_name.lower()

#TRUE Count Block
t_count = combined_name.count("t")
r_count = combined_name.count("r")
u_count = combined_name.count("u")
e_count = combined_name.count("e")

# Had to cast true as string in order to concatenate (rather than add) the two values
total_true = str(t_count + r_count + u_count + e_count)

#LOVE Count Block
l_count = combined_name.count("l")
o_count = combined_name.count("o")
v_count = combined_name.count("v")

# Had to cast love as string in order to concatenate (rather than add) the two values
total_love = str(l_count + o_count + v_count + e_count)

#Love Score Block
#Had to cast true and love back to int, in order to run comparisons.
love_score = int(total_true + total_love)

if((love_score < 10) or (love_score > 90)):
  print(f"Your score is {love_score}, you go together like coke and mentos.")

elif((love_score > 40) and (love_score < 50)):
  print(f"Your score is {love_score}, you are alright together.")

else:
  print(f"Your score is {love_score}.")