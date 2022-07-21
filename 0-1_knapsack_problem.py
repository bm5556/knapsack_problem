class KNAPSACK:
    def __init__(self, n: int, max_weight: int):
        self.max_weight = max_weight
        self.items = list()
        for _ in range(n):
            weight, value = map(int, input().split())
            self.items.append(list(weight, value))
        self.max_value = self.find_max_value(n)

    def find_max_value(self, n: int, max_value = 0):
        if n <= 0: return max_value
        elif self.items[0]:
            return self.find_max_value(n-1, max_value)
        

if __name__ == '__main__':
    N, K = map(int, input().split())
    KS = KNAPSACK(N, K)
