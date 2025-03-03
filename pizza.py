#from tabulate import grid
import csv
from tabulate import tabulate

import sys

if len(sys.argv) == 2 :


    if  sys.argv[1][-3:] != "csv":
        sys.exit(f"Not a CSV file")

    try :

        with open(sys.argv[1],newline="") as file :
            reader = csv.reader(file)
            data = []
            for row in reader :
                data.append(row)
                print (row)
           # data = [row for row in reader]
            print(tabulate( data , headers = 'firstrow' ,tablefmt ="grid"))


    except FileNotFoundError:
        sys.exit("File does not exist")


elif len(sys.argv) < 2 :
    sys.exit("Too few command-line arguments")


else :
   sys.exit("Too many command-line arguments")

