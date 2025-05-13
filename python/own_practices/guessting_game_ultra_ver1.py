# Guessing game ultra Ver 1
# made by Yair Thura Linn

# random number generation
import random
def random_num():
    range_chk = False
    while not range_chk:
        s_num = int(input("Enter start of range: "))
        e_num = int(input("Enter end of range: "))
        if s_num >= e_num:
            print("Start of range must be less than end.")
        elif s_num < 0 or e_num < 0:
            print("Range must be positive.")
        else:
            myst_num = random.randint(s_num, e_num)
            range_chk = True
            return myst_num, s_num, e_num

# main program
def main():
    myst_num, s_num, e_num = random_num()
    s_num = myst_num
    e_num = myst_num
    attempt = 5
    while attempt > 0:
        input_num = int(input(f"Guess a number: "))
        if input_num != myst_num:
            attempt -= 1
            print(f"Unlucky, try again. {attempt} attempts left.")
            if attempt == 0:
                print("Out of attempts. GAME OVER.")
                break
        else:
            print(f"Correct!! \n You won the game with {attempt} Stars.")
            break

# run the program
print("Welcome to the guessing game!")
replay = True

while replay:
    game = int(input("""\n Choose an option:
        1. Play the game
        2. Exit game \n
        Your choice: """))
    
    if game == 1:
        main()
    elif game == 2:
        print("Thanks for playing!")
        replay = False
    else:
        print("Error, wrong command.")
