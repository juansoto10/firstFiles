

def knapsack(max_w, weights, values, n):

    if n == 0 or max_w == 0:
        return 0
    
    if weights[n - 1] > max_w:
        return knapsack(max_w, weights, values, n - 1)

    return max(values[n - 1] + knapsack(max_w - weights[n - 1], weights, values, n - 1), knapsack(max_w, weights, values, n - 1))


if __name__ == '__main__':

    values = [60, 100, 120]
    weights = [10, 20, 30]
    max_w = 50
    n = len(values)

    result = knapsack(max_w, weights, values, n)
    print(result)