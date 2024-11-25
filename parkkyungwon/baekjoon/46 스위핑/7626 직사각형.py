import sys



class SegmentTree():
    def __init__(self, data):
        self.half = 1 << (len(data) - 1).bit_length()
        self.leng = self.half << 1
        self.tree = [0] * self.leng
        self.count_dp = [0] * self.leng
        self.cum_tree = [0] * self.leng

        for i, v in enumerate(data, start=self.half):
            self.cum_tree[i] = v

        for i in range(self.half - 1, 0, -1):
            j = i << 1
            self.cum_tree[i] = self.cum_tree[j] + self.cum_tree[j + 1]
    
    def interval_add(self, s, e):
        s += self.half; e += self.half

        while s <= e:
            if s & 1:
                if not self.count_dp[s]:
                    v = self.cum_tree[s] - self.tree[s]
                    self.update(s, v)

                self.count_dp[s] += 1
                s += 1
            
            if not(e & 1):
                if not self.count_dp[e]:
                    v = self.cum_tree[e] - self.tree[e]
                    self.update(e, v)

                self.count_dp[e] += 1
                e -= 1

            s >>= 1; e >>= 1

    def interval_sub(self, s, e):
        s += self.half; e += self.half

        while s <= e:
            if s & 1:
                self.count_dp[s] -= 1

                if not self.count_dp[s]:
                    i = s << 1
                    if i < self.leng:
                        v = self.tree[i] + self.tree[i+1] - self.tree[s]
                    
                    else:
                        v = -self.tree[s]

                    self.update(s, v)

                s += 1
            
            if not(e & 1):
                self.count_dp[e] -= 1

                if not self.count_dp[e]:
                    i = e << 1
                    if i < self.leng:
                        v = self.tree[i] + self.tree[i+1] - self.tree[e]
                    
                    else:
                        v = -self.tree[e]

                    self.update(e, v)

                e -= 1

            s >>= 1; e >>= 1

    def update(self, i, v):
        if not v: 
            return

        while i and not self.count_dp[i]:
            self.tree[i] += v
            i >>= 1
    
    def get_cum_sum(self):
        return self.tree[1]
    

def sol(data):
    x_set = sorted({a[i] for a in data for i in range(2)})
    
    diff = [x_set[i+1] - x_set[i] for i in range(len(x_set) - 1)] 

    st = SegmentTree(diff)
    del diff

    v_to_i = {v: i for i, v in enumerate(x_set)}
    del x_set

    for i in range(len(data)):
        data[i][0] = v_to_i[data[i][0]]
        data[i][1] = v_to_i[data[i][1]]
    del v_to_i

    data2 = []
    for x1, x2, y1, y2 in data:
        data2.append((1, x1, x2, y1))
        data2.append((0, x1, x2, y2))

    del data
    data2.sort(key=lambda x: x[3])

    total = 0
    prev = data2[0][3]
    for a in data2:
        height = a[3] - prev
        prev = a[3]

        total += st.get_cum_sum() * height

        if a[0]:
            st.interval_add(a[1], a[2] - 1)
        
        else:
            st.interval_sub(a[1], a[2] - 1)

    return total


readline = sys.stdin.readline
N = int(readline())

data = [list(map(int, readline().split())) for _ in range(N)]

print(sol(data))
