class KNAPSACK:
    def __init__(self, N, K) -> None:
        self.DP = list(list(0 for _ in range(K+1)) for _ in range(N+1))
        self.N = N
        self.MAX_WEIGHT = K
        self.weights = [0]; self.values = [0]
        for _ in range(N):
            weight, value = map(int, input().split())
            self.weights.append(weight); self.values.append(value)
        self.find_max_value()

    def find_max_value(self, i: int = 1) -> None:
    #find_max_value(i) obtain max_values from previous i items and each weights
    #also, this saves that self.DP[i][current_weight] == max_value
    #Thus we can obtain the max_value that equals to self.DP[self.N][self.MAX_WEIGHT]
        if (i > self.N or self.MAX_WEIGHT <= 0): return
        
        if self.weights[i] > self.MAX_WEIGHT:
            self.DP[i] = self.DP[i-1].copy()
            return self.find_max_value(i+1)
        else: # self.weights <= self.MAX_WEIGHT
            self.DP[i] = self.DP[i-1].copy()
            extra_weight = self.MAX_WEIGHT - self.weights[i]
            for previous_weight in range(extra_weight+1):
                current_weight = previous_weight + self.weights[i]
                previous_value = self.DP[i-1][current_weight]
                current_value = self.DP[i-1][previous_weight] + self.values[i]
                self.DP[i][current_weight] = max(previous_value, current_value)
            return self.find_max_value(i+1)
    
    def max_value(self) -> int:
        return self.DP[self.N][self.MAX_WEIGHT]


if __name__ == '__main__':
    N, K = map(int, input().split())
    KS = KNAPSACK(N, K)
    print(KS.max_value())
