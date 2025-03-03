dict = {
    "apple":130,
    "avocado":50,
    "sweet cherries":"100",
    "pear":100,
    "kiwifruit":"90"
}

x = input("what fruit ? ").lower()

for key,value in dict.items():
    if key == x :
        print(f"calories : {value}")
    else :
        True
