import random
limit = 15
number = random.randint(1,limit)

player_name = input("Hello what is your name ? ")
number_of_guesses = 0
print('okay! ' + player_name + ' I am  guessing a number between 1 and ' + str(limit))

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses +=1
    if guess < number:
        print("Your guess is too low.")
    if guess > number:
        print("Your guess is too high.")
    if guess == number:
        break
if guess == number:
    print("You have guessed the number in " + str(number_of_guesses) + " tries")
elif guess == number and number_of_guesses ==1:
    print("You have guessed the number in " + str(number_of_guesses) + " try! WELDONE")
else:
    print("You did not guess the number, The number was " + str(number))    

