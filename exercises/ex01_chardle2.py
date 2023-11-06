"""EX01 - Chardle2 - A cute step toward Wordle."""

__author__ = "tjschroeder23"

in_word: str = input("Enter a 5-character word: ")
if len(in_word) == 5:
    in_char: str = input("Enter a single character: ")
    if len(in_char) == 1:
        print("Searching for " + in_char + " in " + in_word)

        """Initializing one counters"""
        count_yes: int = 0
    
        if in_word[0] == in_char:
            print(in_char + " found at index 0")
            count_yes = count_yes + 1
        if in_word[1] == in_char:
            print(in_char + " found at index 1")
            count_yes = count_yes + 1
        if in_word[2] == in_char:
            print(in_char + " found at index 2")
            count_yes = count_yes + 1
        if in_word[3] == in_char:
            print(in_char + " found at index 3")
            count_yes = count_yes + 1
        if in_word[4] == in_char:
            print(in_char + " found at index 4")
            count_yes = count_yes + 1
            
        if count_yes < 1:
            print("No instances of " + in_char + " found in " + in_word)
        else:
            if count_yes > 1:
                print(str(count_yes) + " instances of " + in_char + " found in " + in_word)
            else:
                print(str(count_yes) + " instance of " + in_char + " found in " + in_word)
    else:
        print("Error: Character must be a single character.")
        exit()
else:
    print("Error: Word must contain 5 characters")
    exit()
    
