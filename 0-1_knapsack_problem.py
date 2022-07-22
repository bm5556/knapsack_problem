class KNAPSACK:
    def __init__(self, N, K) -> None:
        self.N = N
        self.MAX_WEIGHT = K
        self.items = list() #self.items[i][0] == weight, self.items[i][1] == value
        for _ in range(N):
            weight, value = map(int, input().split())
            self.items.append([weight, value])
        self.max_value = self.find_max_value(self.MAX_WEIGHT)
        

    def find_max_value(self, extra_weight: int, i: int = 0, max_value: int = 0) -> int:
    #find_max_value(i, max_value, extra_weight) means the maximum value 
    #that can be obtain from previous i+1 items
        if extra_weight < 0: return 0
        if i == self.N: return max_value
        if self.items[i][0] > extra_weight:
            return self.find_max_value(extra_weight, i+1, max_value)
        else: # self.items[i][0] <= self.MAX_WEIGHT
            left = self.find_max_value(extra_weight, i+1, max_value)
            right = self.find_max_value(extra_weight - self.items[i][0], i+1, max_value) + self.items[i][1]
            return max(left, right)

if __name__ == '__main__':
    N, K = map(int, input().split())
    KS = KNAPSACK(N, K)
    print(KS.max_value)
