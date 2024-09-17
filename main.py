def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()
    word_count = 0
    for i in range(len(words)):
        word_count += 1
    
    lowered_string = file_contents.lower()
    character_count = {}
    for character in lowered_string:
        if character.isalpha():
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
    
    
    print ("--- Begin report of books/frankenstein.txt ---")
    print (f"{word_count} words found in the document")
    print()
    character_list = list(character_count.items())
    character_list.sort(reverse=True, key=lambda x:x[1])
    for i in character_list:
        print(f'The \'{i[0]}\' character was found {i[1]} times')
    

    print('--- End report ---')
    


main()