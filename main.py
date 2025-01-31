def count_words(file_contents):
    d = dict()
    for st in file_contents:
        if st.lower() not in d:
            d[st.lower()] = 1
        else:
            d[st.lower()] += 1
    return d

# def sort_on(dict):
#     return dict["num"]

if __name__ == '__main__':
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        # print(len(words))
        d = count_words(file_contents)
        # print(d)
        print("--- Begin report of books/frankenstein.txt ---")
        print(str(len(words)) + "words found in the document")
        # d.sort(reverse = True, key = sort_on)
        for char in d:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                print("The " + "\'" + char + "\'" + " character was found " + str(d[char]) + " times")
        print("--- End report ---")

    