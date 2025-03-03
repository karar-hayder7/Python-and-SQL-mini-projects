chars = input("camel name ?")
snake=""
for char in chars:

    if char.isupper():
        snake += '_'+ char.lower()

    else :
       snake += char

print(f"snake_name : {snake}")
