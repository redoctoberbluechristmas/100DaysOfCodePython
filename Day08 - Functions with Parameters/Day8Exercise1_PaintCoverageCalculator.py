# Had to import math.ceil to round-up to nearest integer for can estimation.
import math

def paint_calc(height, width, cover):
    paint_needed = math.ceil((height * width) / cover)
    print(f"You'll need {paint_needed} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)