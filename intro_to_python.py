nba_teams = ["Lakers", "Nuggets", "Celtics"]
len(nba_teams)

nba_teams.append("Clippers")
nba_teams
len(nba_teams)

arr_of_numbers = [1] * 3
arr_of_numbers

nba_teams[0]
nba_teams

nba_teams[-1]
nba_teams[-2]

one_through_ten = list(range(10))
one_through_ten

random_numbers = [2,65,5,6,4,2,2]
random_numbers

random_numbers.sort()
random_numbers

random_numbers[::-1]

random_numbers.pop()
random_numbers

# print(random_numbers)

# help(nba_teams)

dog = {
    "name": "Rocco",
    "age": "7",
    "location": "Los Angeles"
}

dog["name"]
dog["sleep_alot"] = True
dog

##### type conversion #####

int("5")
str(5)
float(99)

bool("Rome")
bool(0)
bool("0")

##### string interpolation #####

# my_message = f"{dog["name"]} lives in {dog["location"]}."
my_message = f"{dog['name']} lives in {dog['location']}."
print(my_message)

another_message = f"I predict the {nba_teams[0]} to win it all."
print(another_message)

print("I predict the {} to win it all.".format(nba_teams[0]))

print("I predict the {} and {} in the Western Conference Finals." .format(nba_teams[0], nba_teams[3]))

##### functions #####

def add_numbers(num1, num2):
    result = num1 + num2
    return result
add_numbers(5, 5)

def print_this():
    print("Hello, my name is ...")
print_this()

def josh_prediction(team1, team2):
    return "I predict the {} and {} in the Western Conference Finals.".format(team1, team2)
josh_prediction(nba_teams[0], nba_teams[3])

def legal_age(age):
    if (age < 21):
        return "Sorry, you're too young."
    elif (age == 21):
        return "You made it. Welcome to adulthood"
    else:
        return "You're free to pass. Enjoy!"

legal_age(32)
legal_age(21)
legal_age(20)

vip = True
food_place = "busy"
def the_spot(vip, food_place, location="Bay Area"):
    if (food_place == "full" and not vip):
        print("Sorry, we have no room tonight at this {} location".format(location))
    elif (food_place == "busy" and not vip):
        print("Please wait 30 minutes for a table at this {} location".format(location))
    else:
        print("Welcome! Come sit down right away")

the_spot(vip, food_place)
the_spot(False, food_place)
the_spot(False, food_place, "Los Angeles")

##### loops #####
number = 0
while number < 10:
    print(number)
    number += 1

for i in range(len(nba_teams)):
    each_team = nba_teams[i]
    print(each_team)

teams = ["Patriots", "Dolphins", "Falcons"]
teams[0]

teams[0] = "Seahawks"
