#Create a function that will randomly generate Lottery numbers
#Input (or parameter) should be the quantity of numbers that we'd like to have generated.
#Function should return a list of generated numbers.
#write a function a way that it won't have repeating numbers.

import random

print "Welcome to the Lottery numbers generator!"

def main():
    while True:
        try:
            quantity_of_numbers = int(raw_input("\nPlease enter how many random numbers would you like to have:\n>> "))
        except ValueError:
            print "\nPlease enter a number!"
            continue
            
            random_numbers(quantity_of_numbers)

            question_yes_or_no = raw_input("\nAgain? (yes/no):\n>> ")
            if question_yes_or_no == "yes":
                continue
            elif question_yes_or_no == "no":
                print "END"
                break




def random_numbers(quantity_of_number):
    numbers = random.sample(range(10000), k=quantity_of_number) #erstellt eine Liste mit random numbers
    print numbers
    return numbers




if __name__ == '__main__':
    main()


