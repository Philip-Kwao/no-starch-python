# This program is going to accept user input and manipulate them
# THEME is list attendance to a party

# Start
# Declare empty list
# Receive user input on how many attendants
# Save attendant to file
# Loop through the attendants
# Replace one attendant
# Insert attendants at the beginning, middle and the end of the list

attendance = []
print("\n\n PARTY LIST CREATOR \n\n")

def writeFile( attendName ):
    with open("attendance.txt", "a") as file:
            file.write(f"{attendName} \n")

def create_attendance():
    number__of_attendees = int(input("How many people are coming for the party: "))

    for attendee in range(number__of_attendees):
        attend_list = input(f"Enter Name ({attendee+1}): ")
        attendance.append(attend_list)

        # File input
        # writeFile(attendee, attend_list)

# read
def readAttendance():
    for attendor in attendance:
        print(f"Dear {attendor}, You are invited to our kick-ass party")

# Call Create Atendance Function
create_attendance()

# Adding items to existing list
attendance.insert(0, "Barbara")
attendance.insert(2,"Gyamfi")
attendance.append("Miller")

# Call read attendance function
readAttendance()

# Update File with updated list
for attend in attendance:
     writeFile(attend)

def readFile():
    with open("attendance.txt") as read_file:
        return(read_file.read())

print(readFile())