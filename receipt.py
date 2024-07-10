
import csv



def main():
    products_dict = read_dictionary("products.csv", 0)

    print(f"{products_dict}")



    with open("request.csv", "rt") as reqFile:
        reader = csv.reader(reqFile)

        next(reader)

        for rowlist in reader:

            temp = products_dict.get(rowlist[0])
            print(f"{temp[1]}: {rowlist[1]} @ {temp[2]}")




            
            




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