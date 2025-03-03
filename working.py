import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):  # 1             #2        #3             #4         #5            #6
    pattren = r"^([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to ([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM)$"

    match = re.search(pattren, s)
    if match:
        first_h = int(match.group(1))
        first_m = match.group(2)
        first_t = match.group(3)

        second_h = int(match.group(4))
        second_m = match.group(5)
        second_t = match.group(6)

        if first_m is None:
            first_m = "00"

        if second_m is None:
            second_m = "00"

        if first_t == "PM" and first_h != 12:
            first_h += 12

        elif first_t == "AM" and first_h == 12:
            first_h = 0

        if second_t == "PM" and second_h != 12:
            second_h += 12

        elif second_t == "AM" and second_h == 12:
            second_h = 0

        answer = f"{first_h:02}:{first_m} to {second_h:02}:{second_m} "

        return answer.strip()
    else:
        raise ValueError


if __name__ == "__main__":
    main()
