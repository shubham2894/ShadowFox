total_jumping_jacks = 100
completed = 0

for _ in range(10):  # 10 sets of 10 jumping jacks
    completed += 10
    remaining = total_jumping_jacks - completed

    print("You did 10 jumping jacks.")

    if completed == total_jumping_jacks:
        print("Congratulations! You completed the workout")
        break

    tired = input("Are you tired? (yes/y or no/n): ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip == "yes" or skip == "y":
            print("You completed a total of", completed, "jumping jacks.")
            break
    else:
        print(remaining, "jumping jacks remaining.")
