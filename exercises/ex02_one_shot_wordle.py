"""A step towards wordle by creating a wordle with one shot."""

__author__ = "tjschroeder23"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
secret_word = input("Key in a secret word: ")

secret_index: int = 0
guess_index: int = 0
box_emoji: str = ""
chr_emoji: str = ""
char_found: bool = False

guess: str = input(f"What is your {len(secret_word)}-letter guess?")

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)}-letters! Try again:")

# index thru guessed word checking character in guessed word against each character in secret word
while guess_index < len(guess):
    # reset index counter for secret word and default state of temporary
    char_found = False
    secret_index = 0
    
    if guess[guess_index] == secret_word[guess_index]:
        box_emoji = box_emoji + GREEN_BOX
        chr_emoji = chr_emoji + guess[guess_index]
    else:
        while char_found is not True and secret_index < len(secret_word):
            if guess[guess_index] == secret_word[secret_index]:
                box_emoji = box_emoji + YELLOW_BOX
                chr_emoji = chr_emoji + guess[guess_index]
                char_found = True
            secret_index = secret_index + 1
        if char_found is False:
            box_emoji = box_emoji + WHITE_BOX
            chr_emoji = chr_emoji + guess[guess_index]
    guess_index = guess_index + 1
    
print(box_emoji)
print(chr_emoji)

if guess != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
