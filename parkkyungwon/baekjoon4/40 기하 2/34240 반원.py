def get_distance(x1, y1):
    return (x1 * x1 + y1 * y1) ** (0.5)


def ccw(x1, y1, x2, y2):
    return x1 * y2 - y1 * x2


def main():
    data = open(0).read().splitlines()

    x1, y1, x2, y2 = map(int, data[-1].split())
    a1, b1 = x2 - x1, y2 - y1
    r = get_distance(a1, b2)

    for i in range(1, len(data) - 1):
        x3, y3 = map(int, data[i])
        a2, b2 = x3 - x2, y3 - y2
        accw = ccw(a1, b1, a2, b2)

        if accw >= 0:
            answer = get_distance(x3 - x1, y3 - y1) - r
        
        elif 






