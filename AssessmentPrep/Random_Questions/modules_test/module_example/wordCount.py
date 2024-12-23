def count(string):
    string = string.lower()

    words_list = string.split()
    word_count = {}

    for word in words_list:
        word_count[word] = word_count.get(word, 0) + 1

    for word in sorted(word_count):
        print(f"{word}-{word_count[word]}")