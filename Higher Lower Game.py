import random
from Data import data

final_score = 0

def higher_lower():
    person_a = random.choice(data)
    global final_score
    continue_game = True
    
    while continue_game:
        person_b = random.choice(data)
        # If person_a and person_b become same, this method is used to avoid it
        while person_b == person_a:
            person_b = random.choice(data)
        
        print(f"Compare A: {person_a['name']}, a {person_a['occupation']}, from {person_a['country']}")
        print("\n" * 1)
        print(f"Against B: {person_b['name']}, a {person_b['occupation']}, from {person_b['country']}")

        answer = input("Who has more followers, Type 'A' or 'B': ").upper()
        if answer == 'A' and person_a['follower_count'] > person_b['follower_count'] or answer == 'B' and person_b['follower_count'] > person_a['follower_count']:
            final_score += 1
            print(f"Answer is correct, Final score: {final_score}")
            person_a = person_b
        else:
            print(f"Answer is Incorrect, Final score: {final_score}")
            continue_game = False
            break
higher_lower()
