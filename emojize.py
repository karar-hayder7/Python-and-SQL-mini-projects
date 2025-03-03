#Input: :thumbs_up:
#Output: 👍
#$ python emojize.py
#Input: :thumbsup:
#Output: 👍
#$ python emojize.py
#Input: hello, :earth_africa:
#Output: hello, 🌍
#$ python emojize.py
#Input: hello, :earth_americas:
#Output: hello, 🌎



import emoji

x = input("Input")
x = emoji.emojize(x,language='alias')

print(f"Output: {x}")
