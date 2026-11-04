beatles = []
print("Step 1:", beatles)


beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("\nStep 2:", beatles)

for i in range(2):
    while True:
        new_members = input(("\nEnter a new member(Stu Sutcliffe or Pete Best): "))
        if new_members == "Stu Sutcliffe" or new_members == "Pete Best":
            beatles.append(new_members)
            break
        else:
            print("Please try again.")

print("\nStep 3:", beatles)

del beatles[-1]
del beatles[-1]

print("\nStep 4:", beatles)

beatles.insert(0, "Ringo Starr")

print("\nStep 5:", beatles)


