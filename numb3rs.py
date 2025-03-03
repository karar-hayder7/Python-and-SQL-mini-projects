import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))



def validate(ip):

    pattren = ip.strip()

    match = re.search(r"^[0-225]{1,3}\.[0-225]{1,3}\.[0-225]{1,3}\.[0-225]{1,3}$", pattren)
    if match :

        print (match.group())
        return True

    else :
        return False



if __name__ == "__main__":
    main()
