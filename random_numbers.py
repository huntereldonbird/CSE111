import math
import random

def main():
    numbers = [16.2, 75.1, 52.3]

    print(f"{numbers}")

    numbers = append_random_numbers(numbers)

    print(f"{numbers}")

    numbers = append_random_numbers(numbers, quantity = 2)

    print(f"{numbers}")

    words = []
 
    # Call the append_random_words function
    # to add one random word to the list.
    append_random_words(words)
    print(f"words {words}")
 
    # Call the append_random_words function
    # to add five random words to the list.
    append_random_words(words, 5)
    print(f"words {words}")



def append_random_numbers(numbers_list, quantity = 1):
    
    for _ in range(quantity):
        x = random.uniform(0, 100)
        x = round(x, 1)
        numbers_list.append(x)

    return numbers_list
    

def append_random_words(words_list, quantity=1):
    """Append quantity randomly chosen words onto the words list.
    Parameters
        words_list: A list of words where this function will
            append random words.
        quantity: The number of random words that this function
            will append onto words_list.
    Return: nothing. It's unnecessary for this function to return
        anything because this function changes the words_list.
    """
 
    # A list of words to randomly choose from.
    candidates = [
        "arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
        "join", "laugh", "love", "sleep", "smile", "speak",
        "sunshine", "toothbrush", "tree", "truth", "walk", "water"
    ]
 
    # Randomly choose quantity words and append them onto words_list.
    for _ in range(quantity):
        word = random.choice(candidates)
        words_list.append(word)

    


main()