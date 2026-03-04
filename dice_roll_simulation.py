import random

rolls = []
six_count = 0
one_count = 0
two_sixes_in_row = 0

previous_roll = None

# Roll the dice 20 times
for i in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)

    if roll == 6:
        six_count += 1
    if roll == 1:
        one_count += 1
    if roll == 6 and previous_roll == 6:
        two_sixes_in_row += 1

    previous_roll = roll

print("Dice rolls:", rolls)
print("Number of times rolled 6:", six_count)
print("Number of times rolled 1:", one_count)
print("Number of times rolled two 6s in a row:", two_sixes_in_row)
