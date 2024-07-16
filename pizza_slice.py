my_pizza = ["Eddy","Cheezy","Dominos","Pizza Hut"]
my__friends_pizza = my_pizza[:]

if my_pizza == my__friends_pizza:
    print(True)

for me in my_pizza:
    print(f"My list: {me}")

for friend in my__friends_pizza:
    print(f"Friend list: {friend}")