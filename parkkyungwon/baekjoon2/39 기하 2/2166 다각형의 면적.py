def main():
    data = map(int, open(0).read().split())
    next(data)

    total = 0
    prev_x, prev_y = first_x, first_y = next(data), next(data)
    try:
        while True:
            curr_x, curr_y = next(data), next(data)
            total += curr_x * prev_y - prev_x * curr_y
            prev_x, prev_y = curr_x, curr_y

    except StopIteration:
            total += first_x * prev_y - prev_x * first_y

    total = round(abs(total) / 2, 1)

    print(total)


main()
