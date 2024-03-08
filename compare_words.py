import style

def compare_words(a, b):
    results = [""]*5
    letter_counts = {}
    for char in a:
        letter_counts[char] = letter_counts.get(char, 0)+1

    for i in range(5):
        if a[i] == b[i]:
            results[i] = style.style(b[i],"green")
            letter_counts[b[i]] -= 1

    for i in range(5):
        if results[i]: continue

        if b[i] in letter_counts and letter_counts[b[i]] > 0:
            results[i] = style.style(b[i], "yellow")
            letter_counts[b[i]] -= 1
        else:
            results[i] = style.style(b[i],"red")
            
    print("".join(results))