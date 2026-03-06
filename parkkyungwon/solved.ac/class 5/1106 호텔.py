def main():
    data = map(int, open(0).read().split())

    C, N = next(data), next(data)

    cities = [(next(data), next(data)) for _ in range(N)]
    cities.sort(key=lambda x: x[1], reverse=True)
    length = C + cities[0][1]

    INF = float('inf')
    dp = [INF] * length
    dp[0] = 0

    for cost, people in cities:
        for i in range(0, length - people):
            if dp[i] == INF: continue

            next_people = i + people
            next_cost = dp[i] + cost

            if dp[next_people] > next_cost:
                dp[next_people] = next_cost

    print(min(dp[C:]))


main()
