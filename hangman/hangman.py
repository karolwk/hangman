import random
import string


def choose_random() -> str:
    """Choose the random word"""
    words = ['python', 'java', 'kotlin', 'javascript']
    return random.choice(words)


def print_output(p_set, word):
    """Prints remaining letters"""
    start = list(len(word) * "-")
    for c, v in enumerate(word):
        if v in p_set:
            start[c] = v
    print("\n" + "".join(start))


def check_word(letter, guessed) -> bool:
    """Checks if word is correct"""
    if len(letter) != 1:
        print("You should input a single letter")
        return False
    if letter in guessed:
        print("You already typed this letter")
        return False
    if letter not in string.ascii_lowercase:
        print("It is not an ASCII lowercase letter")
        return False
    return True


def check_win(guessed, word) -> bool:
    """Check for wining condition"""
    if set(guessed) == set(word):
        print(f"\n{word}\nYou guessed the word!\nYou survived!\n")
        return True
    return False


def play_game():
    tries = 0
    word = choose_random()
    good_gueses = set()
    all_gueses = set()
    while tries < 8:
        print_output(good_gueses, word)
        inp = input("Input a letter: ")
        if check_word(inp, all_gueses):
            all_gueses.add(inp)
            if inp in word:
                good_gueses.add(inp)
                if check_win(good_gueses, word):
                    return
            else:
                print("No such letter in the word")
                tries += 1
    print("You are hanged!\n")


def main():
    print("H A N G M A N")
    while True:
        inp = input('Type "play" to play the game, "exit" to quit: ')
        if inp == "exit":
            break
        if inp == 'play':
            play_game()


if __name__ == "__main__":
    main()
