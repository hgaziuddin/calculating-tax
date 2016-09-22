cost = 1
totalcost = 0
taxPercentage = .06

def tax(TotalCost):
    print("Your subtotal is: " + str(TotalCost) + "$")
    finalcost = TotalCost * taxPercentage
    print("Your tax is: " + str(finalcost))
    print("And Your grand total is: " + str(finalcost + TotalCost))

while cost > 0:
    print("Please enter the value of your item, or to finish the process enter '0'\n")
    cost = raw_input()
    cost = float(cost)
    totalcost += cost
    if cost == 0:
        tax(totalcost)
        break
    print("\nYour total so far is: " + str(totalcost) + "$")
