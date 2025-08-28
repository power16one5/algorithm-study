class window_max:
    __slots__ = ('length', 'length_p1', 'value_dp', 'time_dp', 'current_time', 's', 'e')

    def __init__(self, length): 
        self.length = length
        self.length_p1 = self.length + 1
        self.value_dp, self.time_dp = [-1] * self.length_p1, [-1] * self.length_p1
        self.s, self.e = 0, 0
        self.current_time = 0

    def push_and_get_max(self, v):
        if self.time_dp[self.s] == self.current_time:
            self.s += 1
            if self.s == self.length_p1: self.s = 0

        while self.value_dp[self.e - 1] <= v and self.s != self.e:
            self.e -= 1
            if self.e < 0: self.e = self.length

        self.value_dp[self.e] = v
        self.time_dp[self.e] = self.current_time + self.length
        self.e += 1
        if self.e == self.length_p1: self.e = 0
        
        self.current_time += 1

        return self.value_dp[self.s]
    
    def clear(self):
        self.s, self.e = 0, 0
        self.current_time = 0


def main():
    _, M, C, D = map(int, input().split())    
    tempurature = map(int, input().split())

    wm = window_max((D // C * 2) + 1)
    temp = next(tempurature)
    dp = [i for i in range(M - temp, M)] + [i for i in range(M, temp - 1, -1)] + [0] * D

    for temp in tempurature:        
        for i in range(1, C + 1):
            for j in range(i, i + D, C):
                wm.push_and_get_max(dp[j])

            for j in range(i, M + 1, C):
                dp[j] = wm.push_and_get_max(dp[j + D]) + M + (j - temp if j < temp else temp - j)
            
            wm.clear()
    
    print(max(dp))


main()
