



price = 50
total = 0
accepted_coins = [5,25,10]

left = 50

while total < price :
    coins=int(input("fucking put it ? "))



    if coins in accepted_coins:
        total = coins + total
        left = price - total
        #total += coins  # Add the coin to the total amount inserted
        #left = price - total

        if left > 0 :

              print (f"Amount Due: {left}")

        elif left == 0 :

             print (f"Change Owed: {left}")
             break


        else :



            left =-1 *left
            print(f"Change Owed: {left}")
            break

    else :
         print (f"Amount Due: {left}")







