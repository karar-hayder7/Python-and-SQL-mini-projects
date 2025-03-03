import sys
from pyfiglet import Figlet
import random

arg = sys.argv[1:]

figlet = Figlet()
list_fonts = figlet.getFonts()

if len(arg) == 0:
    texto = input("Input: ")
    font = random.choice(list_fonts)
    figlet.setFont(font=font)
    print(figlet.renderText(texto))

elif len(arg) == 2 and (arg[0] in ["-f", "--font"]):
    if arg[1] in list_fonts:
        texto = input("Input: ")
        figlet.setFont(font=arg[1])
        print(figlet.renderText(texto))
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")


