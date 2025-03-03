

def main():
    x = input(" what is the answer   ?")
    x= x.lower().replace("-"," ").strip()
    question(x)



def question (x):
    if x == '42' or x == 'forty two':

        print("yes")
    else :

        print("no")



main()
