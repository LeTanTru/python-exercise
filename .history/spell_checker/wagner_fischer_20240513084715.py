def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def wagner_fischer(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    if len_s1 > len_s2:
        s1, s2 = s2, s1
        len_s1, len_s2 = len_s2, len_s1

    current_row = range(len_s1 + 1)
    for i in range(1, len_s2 + 1):
        previous_row, current_row = current_row, [i] + [0] * len_s1
        for j in range(1, len_s1 + 1):
            add, delete, change = previous_row[j] + 1, current_row[j-1] + 1, previous_row[j-1]
            if s1[j-1] != s2[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[len_s1]

def spell_check(word, dictionary):
    suggestions = []

    for correct_word in dictionary:
        distance = wagner_fischer(word, correct_word)
        suggestions.append((correct_word, distance))

    suggestions.sort(key=lambda x: x[1])
    return suggestions[:10]

def edit_distance(i, j):
    if memo[i][j] != -1:
        return memo[i][j]
    if i == 0:
        memo[i][j] = j
    elif j == 0:
        memo[i][j] = i
    else:
        memo[i][j] = min(edit_distance(i - 1, j) + 1,        #Deletion
                         edit_distance(i, j - 1) + 1,        #Insertion
                         edit_distance(i - 1, j - 1) + 
                           (0 if s1[i - 1] == s2[j - 1] else 1)) #Substitution
    return memo[i][j]

dictionary = load_dictionary("spell_checker/words.txt")
misspelled_word = "gdoo"
suggestions = spell_check(misspelled_word, dictionary)
print(f"Top 10 suggestions for '{misspelled_word}':")
for word, distance in suggestions:
    print(f"{word} (Distance: {distance})")
