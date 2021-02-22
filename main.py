secret_num = 9
guesses = 0
guess_limit = 3

while guesses < guess_limit:
    guess = int(input('Guess a number: '))
    guesses += 1
    if guess == secret_num:
        print("you won")
        break
else:
    print("sorry you failed")


