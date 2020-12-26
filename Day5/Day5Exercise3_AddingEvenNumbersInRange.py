
# By using modulo in conditional.
even_total = 0

for num in range(0, 101):
    if num % 2 == 0:
        even_total += num

print(even_total)


# By changing step-size in range function

even_total = 0

for num in range(0, 101, 2):
    even_total += num

print(even_total)