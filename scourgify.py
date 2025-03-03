import csv
from tabulate import tabulate

import sys

if len(sys.argv) == 3 :


    if  sys.argv[1][-3:] != "csv":
        sys.exit(f"Not a CSV file")

    try :

        with open(sys.argv[1],newline="") as file :

            list_dicts =[]
            reader = csv.DictReader(file)
            for line in reader :
                #print(line)
                first, last = line["name"].split(",")
                #print (first, last)
                list_dicts.append({"first" : last.strip() , "last" : first.strip() ,"house": line["house"]  } )



            #print(list_dicts)

        with open(sys.argv[2],"w",newline="") as file2 :
             writer = csv.DictWriter(file2,fieldnames=["first","last","house"])

             writer.writeheader()
             writer.writerows(list_dicts)


    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")


elif len(sys.argv) < 3 :
    sys.exit("Too few command-line arguments")


else :
   sys.exit("Too many command-line arguments")

