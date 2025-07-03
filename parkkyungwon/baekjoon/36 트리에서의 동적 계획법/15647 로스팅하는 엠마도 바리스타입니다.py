import sys



class Tree():
    def __init__(self, N, start_node, edge):
        self.edge = edge
        self.num_of_children = [None] * N
        self.cum_distance = [None] * N
        self.distance_if_being_root = [None] * N
    
        self.init_dfs(start_node)
        self.change_root_dfs(start_node)

    def init_dfs(self, node):
        self.num_of_children[node] = 0
        self.cum_distance[node] = 0

        for child, distance in self.edge[node]:
            if self.num_of_children[child] is not None: continue
            self.init_dfs(child)

            self.num_of_children[node] += self.num_of_children[child] + 1
            self.cum_distance[node] += self.cum_distance[child] + distance * (self.num_of_children[child] + 1)

    def change_root_dfs(self, node):
        self.distance_if_being_root[node] = self.cum_distance[node]

        for child, distance in self.edge[node]:
            if self.distance_if_being_root[child] is not None: continue
            
            self.num_of_children[node] -= self.num_of_children[child] + 1
            self.cum_distance[node] -= self.cum_distance[child] + distance * (self.num_of_children[child] + 1)

            self.num_of_children[child] += self.num_of_children[node] + 1
            self.cum_distance[child] += self.cum_distance[node] + distance * (self.num_of_children[node] + 1)

            self.change_root_dfs(child)

            self.num_of_children[child] -= self.num_of_children[node] + 1
            self.cum_distance[child] -= self.cum_distance[node] + distance * (self.num_of_children[node] + 1)

            self.num_of_children[node] += self.num_of_children[child] + 1
            self.cum_distance[node] += self.cum_distance[child] + distance * (self.num_of_children[child] + 1)

    def get_distance_if_being_root(self):
        return self.distance_if_being_root



def main():
    readline = sys.stdin.readline

    N = int(readline())
    edge = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        u, v, d = map(int, readline().split())
        edge[u].append((v, d))
        edge[v].append((u, d))
    
    answer = Tree(N + 1, 1, edge).get_distance_if_being_root()

    print(*answer[1:], sep='\n')
    

sys.setrecursionlimit(3 * 10**5 + 10)
main()
