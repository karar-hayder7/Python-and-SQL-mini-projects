def main():
    x = input(" what time  ?  ")
    hour =convert(x)
    if 7 <= hour <= 8 :
        print("breakfast time")

    elif 12 <= hour <= 13 :
        print("lunch time ")

    elif 18 <= hour <= 19 :
        print("dinner time")


def convert(time):
    hour, min = time.split(":")
    hour = float(hour)
    min = float(min)
    min  =  min / 60
    answer = hour + min

    return ( answer )







if __name__ == "__main__":
    main()
