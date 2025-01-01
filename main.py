def main():
    with open("books/frankenstein.txt") as f:

        full_text = f.read()
        full_text_lower = full_text.lower()

        #print(full_text)
        #print(len(full_text.split()))

        char_dictionary = {}
        for char in full_text_lower:
            if char in char_dictionary:
                char_dictionary[char] += 1
            else:
                char_dictionary[char] = 1
        
        sorted_char_dictionary = dict(sorted(char_dictionary.items(), key=lambda item: item[1], reverse=True))

        print(sorted_char_dictionary)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(full_text.split())} words found in the document")
        print("")
        for letters in sorted_char_dictionary:
            if letters.isalpha():
                print(f"The '{letters}' character was found {sorted_char_dictionary[letters]} times")
        print("--- End report ---")

main()