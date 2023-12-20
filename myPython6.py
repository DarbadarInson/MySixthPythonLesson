#Random Module
import random
import my_module

random_integer = random.randint(1, 100)
print(random_integer)

print(my_module.pi)

#0.00000000 - 0.99999999
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

#Lists
#fruits = [item1, item2 ...]

states_of_america = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", 
    "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah Vermont", "Virginia", "Washington",
    "West Virginia", "Wisconsin", "Wyoming"
]

print(states_of_america[0])
print(states_of_america[-1])
print(states_of_america[1])

states_of_america[0] = "Uzbekistan"
print(states_of_america[0])

#Append
states_of_america.append("Angelaland")
print(states_of_america)

"""
.append(x)
.extend(iterable)
.insert(i, x)
.remove(x)
.pop(i)
.clear()
.index(x[, start[, end]])
.count(x)
.sort(key=None, reverse = False)
.reverse()
.copy()

"""

str_inp = "Hello, from, AskPython"
op = str_inp.split(",")
print(op)

names_strings = input("Give me everybody's names, seperated by a comma. ")
names = names_strings.split(",")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names(random_choice)
print(person_who_will_pay + "is going yo buy the meal today.")

person_who_will_pay = random.choice(names)
print(person_who_will_pay + "is going yo buy the meal today.")



states_of_america2 = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", 
    "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah Vermont", "Virginia", "Washington",
    "West Virginia", "Wisconsin", "Wyoming"
]

num_of_states = len(states_of_america2)
print(states_of_america2[num_of_states - 1])

vegetables = [
    "Carrot", "Tomato", "Broccoli", "Bell pepper", "Spinach", 
    "Potato", "Cucumber", "Zucchini", "Cauliflower", "Celery", 
    "Kale", "Asparagus", "Eggplant", "Green beans", "Radish", 
    "Cabbage", "Brussels sprouts", "Artichoke", "Peas", "Garlic"
]

fruits = [
    "Apple", "Banana", "Orange", "Strawberry", "Pineapple", 
    "Mango", "Watermelon", "Kiwi", "Pear", "Grapes", 
    "Peach", "Plum", "Cherry", "Blueberry", "Raspberry", 
    "Blackberry", "Lemon", "Lime", "Papaya", "Cranberry"
]

legumes = [
    "Lentils", "Chickpeas", "Black beans", "Kidney beans", "Pinto beans", 
    "Soybeans", "Mung beans", "Navy beans", "Lima beans", "Adzuki beans", 
    "Fava beans", "Black-eyed peas", "Split peas", "Green peas", "Cannellini beans", 
    "Garbanzo beans", "Peanuts", "Red beans", "White beans", "Broad beans"
]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

row1 = ["◻️", "◻️", "◻️"]
row2 = ["◻️", "◻️", "◻️"]
row3 = ["◻️", "◻️", "◻️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where are you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])
selected_row = map[vertical - 1]
selected_row[horizontal - 1]











