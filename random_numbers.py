import math
import random

def main():
    numbers = [16.2, 75.1, 52.3]

    numbers = append_random_numbers(numbers)

    print(f"{numbers}")

    numbers = append_random_numbers(numbers, 2)

    print(f"{numbers}")



def append_random_numbers(numbers_list, quantity = 1):
    
    i = 0
    while i < quantity:
        x = round(random.uniform(0, 100), 1)

        numbers_list.append(x)

        i = i + 1

        return numbers_list
    
        


    


main()