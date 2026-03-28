def main():
    x1, y1, x2, y2, x3, y3 = map(int, open(0).read().split())

    ccw = (x2 - x1) * (y3 - y2) - (x3 - x2) * (y2 - y1)

    print(1 if ccw > 0 else -1 if ccw < 0 else 0)


main()
