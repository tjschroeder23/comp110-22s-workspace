"""A program to test out code in."""

__author__ = "tjschroeder23"

from random import randint


def random_secret_word() -> str:
    sec_word: str = ""
    random_int: int = randint(1, 10)
    if random_int == 1:
        sec_word = "cod"
    elif random_int == 2:
        sec_word = "code"
    elif random_int == 3:
        sec_word = "codes"
    elif random_int == 4:
        sec_word = "coding"
    elif random_int == 5:
        sec_word = "hit"
    elif random_int == 6:
        sec_word = "hits"
    elif random_int == 7:
        sec_word = "hitting"
    elif random_int == 8:
        sec_word = "python"
    elif random_int == 9:
        sec_word = "tim"
    else:
        sec_word = "kellyn"
    return sec_word


def input_guess(num_characters: int) -> str:
    """User input og guesses looped to confirm correct # of caracters."""
    guess_input: str = input(f"Enter a {num_characters} character word?:  ")
    while len(guess_input) != num_characters:
        guess_input = input(f"That wasn't {num_characters} characters! Try again: ")
    return guess_input


def contains_char(search_word: str, search_character: str) -> bool:
    """A function that indicates with boolean if a character is in a word."""
    assert len(search_character) == 1
    ctcc: int = 0
    charac_found: bool = False
    while ctcc < len(search_word) and charac_found is False:
        if search_character == search_word[ctcc]:
            charac_found = True
        ctcc += 1
    return charac_found


def emojified(search_word: str, guess_word: str) -> str:
    """A function to search and see where a guess word fully or partially matches a secret word."""
    assert len(search_word) == len(guess_word)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    box_emoji: str = ""
    ctg: int = 0
   
    while ctg < len(guess_word):
        if guess_word[ctg] == search_word[ctg]:
            box_emoji += GREEN_BOX
        elif contains_char(search_word, guess_word[ctg]) is True:
            box_emoji += YELLOW_BOX
        else:
            box_emoji += WHITE_BOX
        ctg += 1        
    return box_emoji


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = random_secret_word()
    # secret_word: str = "codes"
    # secret_word: str = input("Input a secret word:  ")
    turns: int = 1
    guess: str = ""
    correct: bool = False
    while turns < 7 and correct is False:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret_word))
        emojified(secret_word, guess)
        print(emojified(secret_word, guess))
        if secret_word == guess:
            print(f"You won in {turns}/6 turns!")
            correct = True
        turns += 1
        if turns == 7 and correct is False:
            print("X/6 - Sorry, try again tomorrow!")
    return None


if __name__ == "__main__":
    main()
