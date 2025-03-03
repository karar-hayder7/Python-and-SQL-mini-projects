import sys

if len(sys.argv) == 2 :


    if  sys.argv[1][-3:] != ".py":
        sys.exit(f"Not a Python file")

    try :

        with open(sys.argv[1]) as file :
            long = []
            for line in file :
                x = ""
                if line.strip() == "" or line.strip().startswith("#") :
                    continue

                long.append(line)
            print(len(long),end="")

    except FileNotFoundError:
        sys.exit("File does not exist")


elif len(sys.argv) < 2 :
    sys.exit("Too few command-line arguments")


else :
   sys.exit("Too many command-line arguments")

