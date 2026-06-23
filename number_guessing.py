import random
num = int(random.randint(1,100))
tries = 0
while True :
    try:
       guess = int(input('enter number guessed between 1 & 100 : '))
       tries += 1

       if guess == num :
        print("Congratulations! You guessed the number.")
        print(f"Number of tries: {tries}")
        break   
       
       elif guess < num :
            print("Too low. Try again.")
       
       elif guess > num :
            print("Too high. Try again.")
       
       else :
            print("Invalid input. Please enter a number between 1 and 100.")
           
       
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")
