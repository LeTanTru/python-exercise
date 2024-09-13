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
    suggestions = []
    for correct_word in dictionary:
        distance = dp_distance(word, correct_word)
        suggestions.append((correct_word, distance))

    suggestions.sort(key=lambda x: x[1])
    
    return suggestions[:10]

misspelled_word = "gdoo"
distance = dp_distance("float", "boat")

# dictionary = load_dictionary("spell_checker/words.txt")
# misspelled_word = "gdoo"
# suggestions = spell_check(misspelled_word, dictionary)
# for word, distance in suggestions:
#     print(f"{word} (Distance: {distance})")
