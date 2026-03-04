# Initial Justice League list
justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

# 1. Number of members
print("1. Number of members:", len(justice_league))
print(justice_league)


# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\n2. After adding Batgirl and Nightwing:")
print(justice_league)


# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\n3. After making Wonder Woman the leader:")
print(justice_league)


# 4. Separate Aquaman and Flash
# Choosing "Green Lantern" to place between them
justice_league.remove("Green Lantern")

flash_index = justice_league.index("Flash")
justice_league.insert(flash_index + 1, "Green Lantern")
print("\n4. After separating Aquaman and Flash:")
print(justice_league)


# 5. Replace with new team
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]
print("\n5. New Justice League team:")
print(justice_league)


# 6. Sort alphabetically
justice_league.sort()
print("\n6. Sorted Justice League:")
print(justice_league)

# Bonus: New leader
print("\nBONUS: New Leader is:", justice_league[0])
