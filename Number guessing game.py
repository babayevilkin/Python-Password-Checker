import random
print('Hi. Welcome to game. Please find the number between 1-10000')


guess = int(input('Guess a number: '))
correct = random.randint(1,10000)
guesses = 1

while guess != correct:
    guesses += 1
    if guess < correct:
        guess = int(input('Low. Go high. Guess a number: '))
    else:
        guess = int(input('High. Go low. Guess a number: '))

print(f'Wow! Finally! Correct number was {correct} and you gueesed it in {guesses} times')
