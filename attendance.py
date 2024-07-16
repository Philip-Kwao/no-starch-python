attendance = ["Philip", "James", "Paul"]

for attendee in attendance:
    print (f"{attendee}, You are invited to the party\n\n")

# cant__make_it = attendance.pop()

# print(f"{cant__make_it} can't make it")

attendance[2] = "Lord"

for attend in attendance:
    print(f"{attend}, Thanks for accepting invitation\n\n")

attendance.insert(0, "Kwesi")
for attend in attendance:
    print(f"{attend},\n\n")

attendance.insert(2, "John")
for attend in attendance:
    print(f"{attend},\n\n")

attendance.append("Abi")
for attend in attendance:
    print(f"{attend}, You can only bring two guests\n\n")