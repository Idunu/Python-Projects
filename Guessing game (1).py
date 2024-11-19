import random

while True:
    # Ask user to play
    play = input('Do you want to play a guessing game? (Y/N)')
    # If yes, Generate a random number
    if play == 'Y':
        random_num = random.randint(1,100)
        # Ask user to guess number
        print('Lets play!')
        try:
            guess = int(input('Guess a number between 1 to 100:'))  
            # if correct, print congrats message
            if guess == random_num:
                print ('Congratulations! The number is /random_num')
            # If too high, guess again
            elif guess > random_num:
                guess = input('Too high! Guess again:')
            # If too low, guess again    
            elif guess < random_num:
                guess = input('Too low! Guess again:')
            else:
                print ('Invalid Number')
        except ValueError:
            print('Enter a valid number:')

        print('Thanks for playing')
        break
    else:
        print ('Invalid Input!')