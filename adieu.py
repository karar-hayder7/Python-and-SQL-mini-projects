#Adieu, adieu, to Liesl
#Adieu, adieu, to Liesl and Friedrich
#Adieu, adieu, to Liesl, Friedrich, and Louisa
#Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
#Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
#
#
#
#$ python adieu.py
#Name: Liesl
#Name:
import sys


x = []
while True:
    try:
        x.append(input("Name: "))
    except EOFError:
        break  # Exit the loop on EOF

if len(x) == 1:
    print(f"Adieu, adieu, to {x[0]}")
elif len(x) == 2:
    print(f"Adieu, adieu, to {x[0]} and {x[1]}")
else:
    middle_part = ", ".join(x[1:-1])
    print(f"Adieu, adieu, to {x[0]}, {middle_part}, and {x[-1]}")
