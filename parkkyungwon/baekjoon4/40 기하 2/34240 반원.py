def get_distance(x1, y1):
    return (x1 * x1 + y1 * y1) ** (0.5)


class rotate_matrix:
    def __init__(self, x, y):
        self.adj = get_distance(x, y)
        self.a11, self.a12 = x / self.adj, y / self.adj
        self.a21, self.a22 = -y / self.adj, x / self.adj

    def mul(self, x, y):
        return [(self.a11 * x + self.a12 * y),
                (self.a21 * x + self.a22 * y)]


def main():
    data = open(0).read().splitlines()

    x1, y1, x2, y2 = map(int, data[-1].split())
    A = rotate_matrix(x2 - x1, y2 - y1)
    total_cost = 0

    for i in range(1, len(data) - 1):
        x3, y3 = map(int, data[i].split())
        a, b = x3 - x1, y3 - y1
        a, b = A.mul(a, b)

        if b >= 0:
            c = get_distance(a, b)
            if c > A.adj: total_cost += c - A.adj

        elif a > A.adj or a < -A.adj:
            total_cost += get_distance(abs(a) - A.adj, b)

        else:
            total_cost += abs(b)

    print(total_cost)


main()
