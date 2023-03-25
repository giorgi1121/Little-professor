#import random module
import random


def main():
    level = get_level()
    score = examples_loop(level)
    print("Score: ", score)


def get_level():
    #make loop which checks if level is appropriate or not
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level <= 3:
                return level
                break
            else:
                continue
        except:
            pass




def generate_integer(level):
    #generate x and y with random.randint according to level
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

#define function with arguments x and y which check if user answer is correct or not
#after 3 tries it will print correct answer
def answers(x, y):
    tries = 0
    while tries < 3:
        try:
            user_answer = int(input(f"{x} + {y} = "))
            correct_answer = x + y
            if user_answer == correct_answer:
                return True
            else:
                print("EEE")
                tries += 1
        except:
            print("EEE")
            tries += 1
    print(f"{x} + {y} = {x+y}")

#define examples loop which counts 10 round with different examples and count scores
def examples_loop(level):
    round = 0
    score = 0
    while round < 10:
        x, y = generate_integer(level)
        if answers(x, y) == True:
            score += 1
        round += 1
    return score

if __name__ == "__main__":
    main()
