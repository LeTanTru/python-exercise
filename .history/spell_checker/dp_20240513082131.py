def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def dp_distance(a, b):
    n = len(a)
    m = len(b)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,
                           dp[i][j - 1] + 1,
                           dp[i - 1][j - 1] + cost)
    return dp[n][m]

def spell_check(word, dictionary):
