import math
import random

def main():
    numbers = [16.2, 75.1, 52.3]

    print(f"{numbers}")

    numbers = append_random_numbers(numbers)

    print(f"{numbers}")

    numbers = append_random_numbers(numbers, quantity = 5)

    print(f"{numbers}")



def append_random_numbers(numbers_list, quantity = 1):
    
    for i in range(quantity):
        x = round(random.uniform(0, 100), 1)

        numbers_list.append(x)

        return numbers_list
    
        


    


main()