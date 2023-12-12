import os


def open_screen():
    """displaying opening screen.
        :rtype: None
        """
    print("""
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/ """)


def choose_word(file_path, index):
    """chooses a word by index from the txt file.
        :param file_path: path to words file
        :param index: the index of the chosen word from words file
        :type file_path: str
        :type index: int
        :return: The chosen word from the words file
        :rtype: str
        """
    words_file = open(file_path, "r")
    word_list = words_file.read().split(" ")
    new_index = (int(index) - 1) % len(word_list)
    chosen_word = word_list[int(new_index)]
    return chosen_word


def show_hidden_word(secret_word, old_letters_guessed):
    """returns the secret word with "_" instead of the missing letters.
        :param secret_word: secret word
        :param old_letters_guessed: list of the letters that the user guessed
        :type secret_word: str
        :type old_letters_guessed: list
        :return: the secret word with "_" instead of the missing letters
        :rtype: str
        """
    new_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            new_word += letter
        else:
            new_word += "_ "
    return new_word


def check_win(secret_word, old_letters_guessed):
    """checks if there are no more missing letters.
            :param secret_word: secret word
            :param old_letters_guessed: list of the letters that the user guessed
            :type secret_word: str
            :type old_letters_guessed: list
            :return: returns if the player has won the game
            :rtype: bool
            """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def check_valid_input(letter_guessed, old_letters_guessed):
    """checks if the letter that the user tried is valid.
                :param letter_guessed: the letter that the user guessed
                :param old_letters_guessed: list of the letters that the user guessed
                :type letter_guessed: str
                :type old_letters_guessed: list
                :return: returns if the character that the user has guessed is valid
                :rtype: bool
                """
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """checks if the letter that the user tried is valid and if it does, update the secret word respectively to the new
    state.
                    :param letter_guessed: the letter that the user guessed
                    :param old_letters_guessed: list of the letters that the user guessed
                    :type letter_guessed: str
                    :type old_letters_guessed: list
                    :return: returns if the character that the user has guessed is valid
                    :rtype: bool
                    """
    letter_guessed = letter_guessed.lower()
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.sort(key=str.lower)
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        print(' -> '.join(sorted(old_letters_guessed, key=str.lower)))
        return False


def checks_if_file_exists(file_path):
    """checks if the file path is valid
     :param file_path: file path
     :type file_path: str
     :return: returns if the file path is valid
     :rtype: bool
     """
    return os.path.isfile(file_path)


HANGMAN_PHOTOS = {1: "x-------x",

                  2:
                      """\nx-------x 
                      \n| \
                      \n|\
                      \n|\
                      \n|\
                      \n|""",

                  3:
                      """\nx-------x
                       \n|       |
                       \n|       0
                       \n|
                       \n|
                       \n| """,

                  4:
                      """\nx-------x
                      \n|       |
                      \n|       0
                      \n|       |
                      \n|
                      \n|""",

                  5:
                      """\nx-------x
                      \n|       |
                      \n|       0
                      \n|      /|\\ 
                      \n|
                      \n|""",

                  6:
                      """\nx-------x
                      \n|       |
                      \n|       0
                      \n|      /|\ 
                      \n|      / 
                      \n|""",

                  7:
                      """\nx-------x
                      \n|       |
                      \n|       0
                      \n|      /|\ 
                      \n|      / \\ """}
MAX_TRIES = 6


def main():
    open_screen()

    file_path = input("please enter file path ")
    while not checks_if_file_exists(file_path):
        print("file doesnt exist.")
        file_path = input("please enter file path ")
    index = int(input("please enter index "))
    secret_word = choose_word(file_path, index)
    num_of_tries = 0
    old_letters_guessed = []
    print(HANGMAN_PHOTOS[num_of_tries + 1])
    print(show_hidden_word(secret_word, old_letters_guessed))

    while not check_win(secret_word, old_letters_guessed) and num_of_tries < MAX_TRIES:
        letter_guessed = input("please enter a letter! ").lower()
        if len(
                letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed not in old_letters_guessed and \
                letter_guessed not in secret_word:
            print(":(")
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed not in secret_word:
                num_of_tries += 1
        print(HANGMAN_PHOTOS[num_of_tries + 1])
        print(show_hidden_word(secret_word, old_letters_guessed))
        if num_of_tries != 1:
            print("you guessed", num_of_tries, "wrong tries!")
        else:
            print("you guessed", num_of_tries, "wrong try!")
    if check_win(secret_word, old_letters_guessed):
        print("WIN")
    else:
        print("LOSE")


if __name__ == '__main__':
    main()
