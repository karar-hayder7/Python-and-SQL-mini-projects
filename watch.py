import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    pattren = r"src=[\"']https?://(?:www\.)?youtube\.com/embed/([0-9a-zA-Z_-]+)[\"']"


    match = re.search(pattren,s)
    if match :
        link = match.group(1)
        answer = f"https://youtu.be/{link}"
        return answer
    else:
        return match


if __name__ == "__main__":
    main()

#https://youtu.be/xvFZjo5PgG0
#https://youtu
#https://youtu/
#<iframe width="560" height="315"
#src="https://www.youtube.com/embed/QJHPlKPOc78?si=YsmI2UfJNXU6XSRN"
#title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
