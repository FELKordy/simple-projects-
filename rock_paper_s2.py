import random
emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}
choices = ('r', 'p', 's')

def get_user_choice():
    user_choice = input('Rock, paper or scissors? (r/p/s): ').lower()
    if user_choice not in choices:
        print('Invalid choice')
        return None
    else:
        return user_choice

while True:
    user_choice = get_user_choice()
    if user_choice is None:
        continue
    computer_choice = random.choice(choices)
    print(f'You chose {emojis[user_choice]} and computer chose {emojis[computer_choice]}')
    break
