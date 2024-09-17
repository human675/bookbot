def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()
    word_count = 0
    for i in range(len(words)):
        word_count += 1
    print(word_count)
    
    lowered_string = file_contents.lower()
    character_count = {}
    for character in lowered_string:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    print (character_count)

main()