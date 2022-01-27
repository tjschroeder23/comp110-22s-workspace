"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "tjschroeder23"

in_word: str = input("Enter a 5-character word: ")

if len(in_word) == 5:
    in_char: str = input("Enter a single character: ")
    if len(in_char) == 1:
        print("Searching for " + in_char + " in " + in_word)

        """Initializing two counters"""
        counter: int = 0
        count_yes: int = 0

        while (counter <= (len(in_word) - 1)):
            if in_word[counter] == in_char:
                print(in_char + " found at index " + str(counter))
                counter = counter + 1
                count_yes = count_yes + 1
            else:
                counter = counter + 1

        if count_yes < 1:
            print("No instances of " + in_char + " found in " + in_word)
        else:
            if count_yes > 1:
                print(str(count_yes) + " instances of " + in_char + " found in " + in_word)
            else:
                print(str(count_yes) + " instance of " + in_char + " found in " + in_word)
    else:
        print("Error: Character must be a single character.")
else:
    print("Error: Word must contain 5 characters")
