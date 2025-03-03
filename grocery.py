dic={}


while True :
    try:
        i = input().upper()

        if i in dic :
            dic[i] += 1
        else :
            dic[i] = 1



    except EOFError :

        for key , value in sorted(dic.items()) :
            print (f"{value} {key}")

        break

