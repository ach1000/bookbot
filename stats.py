def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    char_counts = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sort_on(item):
    return item[1]

def sort_char_counts(char_counts):
    #char_counts_list = list(char_counts.items())
    #char_counts_list.sort(reverse=True, key=sort_on)
    #return char_counts_list

    return sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
