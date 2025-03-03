def main():
    word = input("Tell me? ")
    print(shorten(word))  # Print the returned value

def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]  # Fixed vowels list
    out = ""

    for c in word:
        if c not in vowels:
            out += c  # Append only non-vowel characters

    return out  # Return the modified word

if __name__ == "__main__":
    main()
