def bigger_is_greater(w):
    # Find the rightmost character that is smaller than the character to its right
    for i in range(len(w)-2, -1, -1):
        if w[i] < w[i+1]:
            break
    else:
        # If there is no such character, return "no answer"
        return "no answer"
    
    # Find the smallest character to the right of w[i] that is greater than w[i]
    for j in range(len(w)-1, i, -1):
        if w[j] > w[i]:
            break
    
    # Swap w[i] and w[j]
    w = list(w)
    w[i], w[j] = w[j], w[i]
    
    # Reverse the substring to the right of i
    w[i+1:] = reversed(w[i+1:])
    
    return ''.join(w)

def main():
    t = int(input().strip())
    for i in range(t):
        w = input().strip()
        result = bigger_is_greater(w)
        print(result)

if __name__ == '__main__':
    main()