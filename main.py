import random
over = 0
while over != 1:
    rps = ['rock', 'paper', 'scissors']
    comp_answer = random.choice(rps)
    guess = input("rock, paper, or scissors? ").lower()
    if guess == 'paper' and comp_answer == 'rock':
        print("{0} does beat {1}!".format(guess, comp_answer))
        over = 1
    elif guess == 'rock' and comp_answer == 'scissors':
        print ("{0} does beat {1}!".format(guess, comp_answer))
        over = 1
    elif guess == 'scissors' and comp_answer == 'paper':
        print ("{0} does beat {1}!".format(guess, comp_answer))
        over = 1
    elif guess == 'scissors' and comp_answer == 'rock' or guess == 'scissors' and comp_answer == 'scissors':
        print("{0} doesn't beat {1}!".format(guess, comp_answer))
    elif guess == 'rock' and comp_answer == 'paper' or guess == 'rock' and comp_answer == 'rock':
        print ("{0} doesn't beat {1}!".format(guess, comp_answer))
    elif guess == 'paper' and comp_answer == 'scissors' or guess == 'paper' and comp_answer == 'paper':
        print ("{0} doesn't beat {1}!".format(guess, comp_answer))
