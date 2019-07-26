import time
import random


def play():
    count = 0
    result = random.randint(0,60)
    print(result)
    winner = []
    my_numbers = []
    name = str(input("Enter name: "))
    print("Welcome {} to Guessing game!".format(name))
    time.sleep(2)

    try:
        while count < 3:
            user_input = int(input("Enter a number: "))

            count +=1
            my_numbers.append(user_input)

            if user_input == result:
                print(name," Yeeei, You have have won on your first try!!")
                print("Winning number: ", result)
                break

            elif user_input < result:
                print(name, " Number too low")

            # If number is out of range, then kill the process
            elif user_input > 60:

                print(name," Number out of range, exiting")
                timer = 5

                while timer:
                    print(timer)
                    timer -=1
                    time.sleep(1)

                print("Good bye ", name)
                break

            else:
                print("Incorrect.")
                continue

        else:
            time.sleep(2)
            winner.append(result)

            print("Sorry \033[1m{0}\033[0m, The winning number is \033[1m{1}\033[0m : and Your numbers \033[1m{2}\033[0m"\
                  .format(name, result,my_numbers))
    except:
        print(name," That is not a number.")


play()