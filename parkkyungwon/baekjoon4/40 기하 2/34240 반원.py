class inverse_matrix:
    def __init__(self, x, y):
        self.a11, self.a12 = x, y
        self.a21, self.a22 = -y, x
        self.det = x * x + y * y

    def mul(self, x, y):
        return [(self.a11 * x + self.a12 * y) / self.det,
                (self.a21 * x + self.a22 * y) / self.det]



def get_distance(x1, y1):
    return (x1 * x1 + y1 * y1) ** (0.5)


def main():
    data = open(0).read().splitlines()

    x1, y1, x2, y2 = map(int, data[-1].split())
    A_inv = inverse_matrix(x2 - x1, y2 - y1)
    total_cost = 0

    for i in range(1, len(data) - 1):
        x3, y3 = map(int, data[i].split())
        a, b = x3 - x1, y3 - y1
        a, b = A_inv.mul(a, b)

        if b >= 0:
            c = get_distance(a, b)
            if c > 1: total_cost += c - 1

        elif a > 1 or a < -1:
            total_cost += get_distance(abs(a) - 1, b)

        else:
            total_cost += abs(b)

    total_cost *= A_inv.det
    print(total_cost)


main()
