import random
from art import logo, vs
from game_data import data

print(logo)


def create_option(compare):
    compare_name = compare['name']
    compare_description = compare['description']
    compare_country = compare['country']
    return f"{compare_name}, a {compare_description}, from {compare_country}. "


game_is_running = True
compareB = random.choice(data)
score = 0
while game_is_running:
    compareA = compareB
    compareB = random.choice(data)
    if compareA == compareB:
        compareB = random.choice(data)
    print(f"Compare A: {create_option(compareA)}")
    print(vs)
    print(f"Compare B: {create_option(compareB)}")

    user_input = input("Who has more followers? Type 'A' or 'B' ").lower()
    if compareA['follower_count'] > compareB['follower_count'] and user_input == 'a':
        score += 1
        print(f"Your current score is {score}")
    elif compareB['follower_count'] > compareA['follower_count'] and user_input == 'b':
        score += 1
        print(f"Your current score is {score}")
    elif compareA['follower_count'] < compareB['follower_count'] and user_input == 'a':
        game_is_running = False
        print(f"Your final score is {score}")
    elif compareB['follower_count'] < compareA['follower_count'] and user_input == 'b':
        game_is_running = False
        print(f"Your final score is {score}")


