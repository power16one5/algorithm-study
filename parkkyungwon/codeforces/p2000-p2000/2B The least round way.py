def add_vec(tensor, vec):
    a1, a2 = vec
    for mat in tensor:
        for arr in mat:
            arr[0] += a1; arr[1] += a2


def dist_mat(tensor):
    mat1, mat2 = tensor
    while mat2 and mat2[-1][0] < mat2[-1][1]:
        mat1.append(mat2.pop())

    while mat1 and mat1[-1][0] > mat1[-1][1]:
        mat2.append(mat1.pop())


def two_axis_min(tensor):
    left_arr = []
    l, g = -1, 10 ** 9
    for a in sorted(tensor[0], key=lambda x: (x[0], x[1])):
        if l < a[0] and g > a[1]:
            left_arr.append(a)
            l, g = a[0], a[1]

    right_arr = []
    l, g = -1, 10 ** 9
    for a in sorted(tensor[1], key=lambda x: (x[1], x[0])):
        if l < a[1] and g > a[0]:
            right_arr.append(a)
            l, g = a[1], a[0]

    tensor[0], tensor[1] = left_arr, right_arr


def add_label(tensor, label):
    for mat in tensor:
        for vec in mat:
            vec.append(label)


def get_num_of_fact(x):
    answer = []
    for factor in 2, 5:
        count = 0
        while not x % factor:
            count += 1
            x //= factor
        answer.append(count)

    return answer


def main():
    INF = 10 ** 9
    data = map(int, open(0).read().split())
    n = next(data)
    data = map(get_num_of_fact, data)

    dp = [[[], []] for _ in range(n)]
    dp[0][0].append([0, 0])

    for _ in range(n):
        add_vec(dp[0], next(data))

        for i in range(1, n):
            dp[i][0].extend([a[:] for a in dp[i - 1][0]])
            dp[i][1].extend([a[:] for a in dp[i - 1][1]])
            two_axis_min(dp[i])
            add_vec(dp[i], next(data))
            dist_mat(dp[i])
        
        for i in range(n):
            add_label(dp[i], i)
    
    two_axis_min(dp[-1])
    dist_mat(dp[-1])

    left, right = dp[-1][0][0] if dp[-1][0] else [INF, INF], dp[-1][1][0] if dp[-1][1] else [INF, INF]
    flag = left[0] < right[1]

    count = left[0] if flag else right[1]

    prev = 0
    path = ""
    for curr in (left[2:] if flag else right[2:]):
        path += 'R' * (curr - prev)
        path += 'D'
        prev = curr

    print(count)
    print(path[:-1])


main()
