# Import depedencies
import random
from replit import clear
from art import logo, vs
from game_data import data
#create the score variable and initialize to 0
score = 0
repeat = True
b = random.choice(data)

def check_answer(answer, follower_a, follower_b):
    """Check if the answer is correct or wrong"""
    if answer == "a":
        if follower_a > follower_b:
            return True
        else:
            return False
    elif answer == "b":
        if follower_b > follower_a:
            return True
        else:
            return False
    else:
        return False
        
# Print the game Logo
print(logo)

while(repeat):
    #Generate random characters from data
    a = b
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    
    # print character A details
    print(f"Compare A: {a.get('name')}, a {a.get('description')}, from {a.get('country')}.")
    # print Vs art
    print(vs)
    # print character B details
    print(f"Against B: {b.get('name')}, a {b.get('description')}, from {b.get('country')}.")
    
    # Ask the player who has more followers
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # Get the followers
    follower_a = a.get('follower_count')
    follower_b = b.get('follower_count')
    
    # Check if users answer is correct
    is_correct = check_answer(answer, follower_a, follower_b)
    # Clear the screen to avoid cluter
    clear()
    print(logo)
    # Give the user Feedback
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}.")
    else:
        repeat = False
        print(f"Sorry, thats wrong. Final score: {score}")