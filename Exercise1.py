n = int(input())
word_count = {}

# sort words
for i in range(n):
    word = input().strip()

    # check is there duplicates
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# output district number
print(len(word_count))

# output number of occurrences for each distinct
for word in word_count:
    print(word_count[word], end=" ")
print()
