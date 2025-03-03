import re

m=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#print(f"{n:02}")
#9/8/1636
#September 8, 1636



while True:
    parts =[]
    user_input=input("Date: ")
    parts=re.split(r"[,\s/]+",user_input.strip())
    year= int(parts[2])
    month=parts[0]
    day= int(parts[1])


    if day > 31 :
        continue



    # the month is digigt
    if month.isdigit():
        month=int(month)

        if month > 12 :
            continue
        else :
            print(f"{year}-{month:02}-{day:02}")
            break

    #the month is text
    else:

        if month not in m :
            continue

        else :

            month= (m.index(month)) + 1

            print(f"{year}-{month:02}-{day:02}")
            break


