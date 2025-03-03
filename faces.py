def main():
    ix = input('write what ever ? ')
    print(change(ix))


def change(a):
    modified =a.replace(":)","🙂")
    modified =modified.replace(":(","🙁")
    return modified


main()


