"""EX02 - One Shot Wordle."""

_author_ = "730549837"

# secret_word = str("python")
secret_word: str = "python"
# word_length = int = len(secret_word)
word_length: int = len(secret_word)

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index_tracker: int = 0
guess_emoji: str = ""

user_guess: str = input(f"What is your {word_length}-letter guess? ")

# making sure guess word length is same as secret word length
# while len(user_guess) != len(secret_word):

while len(user_guess) != word_length:
    user_guess = input(f"That was not {word_length} letters! Try again: ")

# checking if characters match between secret word and guess
while index_tracker < word_length:
    character_found: bool = False
    alternate_index: int = 0
    # character matches at same position
    if user_guess[index_tracker] == secret_word[index_tracker]:
        guess_emoji = guess_emoji + GREEN_BOX
    else:
        # character doesn't match but seeing if in other positions
        while alternate_index < word_length and character_found is not True:
            if user_guess[index_tracker] == secret_word[alternate_index]:
                guess_emoji = guess_emoji + YELLOW_BOX
                # found character once and ends while loop early
                character_found = True
            else:
                alternate_index = alternate_index + 1
                # character isn't in secret word
        if character_found is not True:
            guess_emoji = guess_emoji + WHITE_BOX
    index_tracker = index_tracker + 1
print(guess_emoji)
if secret_word == user_guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")