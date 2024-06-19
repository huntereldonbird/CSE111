import math
import datetime

# preTotal = input("What was your pre-total")
x = datetime.datetime.now().strftime("%w")
print(x)

inputSubtotal = input("Please enter your subtotal : ")

if((int(x) == 4 or int(x) == 2) and float(inputSubtotal) >= 50):
        
        DiscountedValue = (float(inputSubtotal) * 0.10)

        SalesTax = float(inputSubtotal) * 0.06

        FinalTotal = float(inputSubtotal) + SalesTax
        
        
        print("Sales tax amount: " + str(SalesTax))
        print("Total: " + str(FinalTotal))
        
else:
    SalesTax = float(inputSubtotal) * 0.06
    FinalTotal = float(inputSubtotal) + SalesTax

    print("Sales tax amount: " + str(SalesTax))
    print("Total: " + str(FinalTotal))
