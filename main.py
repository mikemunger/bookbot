path = "books/frankenstein.txt"

with open(path) as f:
    file_contents = f.read()

    words = file_contents.split()
    word_count = len(words)

    letter_count = {}

    for char in file_contents:
        char = char.lower()
        if letter_count.get(char):
            letter_count[char] += 1
        else:
            letter_count[char] = 1

    letter_list = []

    for k, v in letter_count.items():
        if k.isalpha():
            letter_list.append(v)

    letter_list.sort(reverse=True)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")

    for count in letter_list:
        for k, v in letter_count.items():
            if v == count:
                print(f"The '{k}' character was found {v} times")

    print("--- End report ---")
