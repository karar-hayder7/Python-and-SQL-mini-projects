a = input("tell me ?  ")

x, y, z = a.split(" ")

x = int(x)
z = int(z)
if y == '+':
    answer = x + z

elif y == '-':
    answer = x - z

elif y == '*':
    answer = x * z

elif y == '/':
    answer = x / z


else :
    answer = 'not correct'


print(float(answer))
