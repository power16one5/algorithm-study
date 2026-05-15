from random import randint
import sys



def main():
    write = sys.stdout.write

    write("500000\n")

    for _ in range(500000):
        write(f"{randint(2, 10000000)} ")

    write("\n")

main()
