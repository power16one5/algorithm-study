class ModComb:
    def __init__(self, mod):
        self.mod = mod
        self.facs, self.facs_invs = self.get_facs_invs()

    def get_facs_invs(self):
        facs = [1] * self.mod
        invs = [1] * self.mod
        facs_invs = [1] * self.mod

        for i in range(2, self.mod):
            facs[i] = facs[i - 1] * i % self.mod
            q, r = divmod(self.mod, i)
            invs[i] = -q * invs[r] % self.mod
        
        for i in range(2, self.mod):
            facs_invs[i] = invs[facs[i]]
        
        return facs, facs_invs
    
    def comb(self, n, k):
        if n < k:
            return 0
        
        return self.facs[n] * self.facs_invs[k] * self.facs_invs[n - k] % self.mod

    def lucas(self, n, k):
        total = 1

        while n or k:
            total = total * self.comb(n % self.mod, k % self.mod) % self.mod

            n //= self.mod; k //= self.mod
        
        return total


def main():
    N, K, M = map(int, input().split())
    mod_comb = ModComb(M)
    print(mod_comb.lucas(N, K))


main()
