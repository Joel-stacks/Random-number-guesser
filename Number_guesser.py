#Random number generator here
import random
x = random.randint(1,10)

#Phases
win = 'Congratulations you guessed correctly'
low = 'Your guess was too low, try a higher number'
high = 'Your guess was too high, try a lower number'

y = 0

while y != x :

    y = input('Guess a number between one and ten:')
    y = int(y)

    if y == x :
        print(win)

    elif y > x :
        print(high)

    else:
        print(low)
