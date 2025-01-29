import  random

def guess(x):
    random_number = random.randint(1,x)
    count_guess = 0
    while count_guess != random_number:
        count_guess = int(input(f'Guess number between 1 to {x}: '))
        if count_guess < random_number:
            print('Sorry! Guess Again. Too Low')
            print(count_guess)
            print(random_number)
        elif count_guess > random_number:
            print('Sorry! Guess Again. Too High')

    print(f'Wow, You are Correct. You guess the number {random_number}')

guess(10)