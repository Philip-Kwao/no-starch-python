# 1. Counting from 1-20
# for num in range(1,21):
#     print(num)

##
# 2. Make a list of 1-1million
# numbers=[]
# for num in range(1,1000001):
#     numbers.append(num)
# print(numbers, sep=", ", end="")
# print(f"Highest number: {max(numbers)}")
# print(f"Lowest number: {min(numbers)}")
# print(f"Total number: {sum(numbers)}")

# for number in numbers:
#     print(number, sep=", ", end="")

###
# 3. Odd Numbers from 1-20
# for num in range(1,21,2):
#     print (num, end=", ")

####
# 4
# multiples__of_three = []
# for num in range(3,31,3):
#     multiples__of_three.append(num)
# for mult in multiples__of_three:
#     print(mult, end=", ")

#####
# A list of cubes from 1 to 10
# cube_list = []
# for num in range(1,10):
#     cube_list.append(num**3)
# for cube_item in cube_list:
#     print(cube_item, end=", ")

######
# 6. List comprehension
print([item**3 for item in range(1,11)])