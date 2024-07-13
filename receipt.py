
import csv
from datetime import datetime



def main():

    WeekDay = datetime.now().strftime("%w")

    products_dict = read_dictionary("products.csv", 0)

    print("Inkom Emporium")
    subtotal = 0
    itemTotal = 0


    with open("request.csv", "rt") as reqFile:
        reader = csv.reader(reqFile)

        next(reader)

        for rowlist in reader:

            temp = products_dict.get(rowlist[0])
            print(f"{temp[1]}: {rowlist[1]} @ {temp[2]}")

            itemTotal = itemTotal + int(rowlist[1])
            subtotal = subtotal + (float(temp[2]) * float(rowlist[1]))
                    

            subtotal = round(subtotal, 2)

            tax = subtotal * 0.06
            tax = round(tax, 2)

            Total = subtotal + tax

    if(int(WeekDay) == 4 or int(WeekDay) == 2):

        print("NOT HERE THOUGH")

        Discounted = Total - (Total*0.1)


        print(f"Number of Items: {itemTotal}")
        print(f"Subtotal: {subtotal}")
        print(f"Sales Tax: {tax}")
        print(f"Total w/ Tuesday Discount: {Discounted}")
        print("Thank you for shopping at the Inkom Emporium")

        currentDateTime = datetime.now(tz=None)


        print(f"{currentDateTime:%A %I %M %p}")
    else:

        print("here")

        print(f"Number of Items: {itemTotal}")
        print(f"Subtotal: {subtotal}")
        print(f"Sales Tax: {tax}")
        print(f"Total: {Total}")
        print("Thank you for shopping at the Inkom Emporium")

        currentDateTime = datetime.now(tz=None)

        print(f"{currentDateTime:%A %I %M %p}")
        
            
        




            
            




def read_dictionary(fileName, KeyIndex):

    dictionary = {}


    with open(fileName, "rt") as file:
        reader = csv.reader(file)

        next(reader)

        for rowlist in reader:

            if(len(rowlist) != 0):

                Key = rowlist[KeyIndex]

                dictionary[Key] = rowlist

    return dictionary




if __name__ == "__main__":
    main()