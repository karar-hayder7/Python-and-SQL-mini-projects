
import requests
import sys
import json
import pandas


def main():

    try:
        x = sys.argv[1]

        if len(sys.argv) < 2:
            print("Missing command-line argument")
            return

        if not is_valid_number(x):

            sys.exit("Command-line argument is not a number")

        x = float(x)
        if x <= 0:
            print("argument can not be less that 0 ")
            return

        responds = requests.get(" https://api.coincap.io/v2/assets/bitcoin")
        responds.raise_for_status()
        res = responds.json()

        # print(json.dumps(res,indent = 2))

        btc = res["data"]
        price = float(btc["priceUsd"])
        total = price * float(sys.argv[1])
        print(f"${total:,.4f}")

        df = pandas.DataFrame([btc])
        print(df["id"])




    except requests.exceptions.HTTPError as err:

        sys.exit(err)
        ...

    except ValueError as value:

        sys.exit(value)
        ...


def is_valid_number(s):
    """Returns True if the string is a valid number (integer or float), otherwise False."""
    try:
        float(s)
        return True
    except ValueError:
        return False


main()
