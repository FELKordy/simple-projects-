import random
while True :
    user=input('Rock, Paper, Scissors, Shoot! (r/p/s) : ').lower()
    choices = ['r', 'p', 's']
    computer = random.choice(choices)
    if user not in choices :
        print("Invalid choice. Please choose 'r', 'p', or 's'.")
    
    if user == 'r' and computer == 's' :
        print(f'you chose {user} ')
        print('🪨')
        print(f'computer chose {computer} ')
        print('✂️')
        print("You win! Rock crushes Scissors.")
    elif user == 'p' and computer == 'r' :
        print(f'you chose {user} ')
        print('📄')
        print(f'computer chose {computer} ')
        print('🪨')
        print("You win! Paper covers Rock.")
    elif user == 's' and computer == 'p' :
        print(f'you chose {user} ')
        print('✂️')
        print(f'computer chose {computer} ')
        print('📄')
        print("You win! Scissors cut Paper.")
    
    elif user == computer :
        print(f'you chose {user} ') 
        print('😐')
        print(f'computer chose {computer} ')
        print('😐')
        print("It's a tie!")
    
    else :
        print(f'you chose {user} ')
        print('😞')
        print(f'computer chose {computer} ')
        print('😞')
        print("Computer wins!")
        