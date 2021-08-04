# Import random to choose a random word to play with as the solution
import random


def select_solution():
    """Returns a random word selected from the list to play with as the solution.
    INPUT: none
    OUTPUT: One random word from the file as a string
    """
    # Open the document and extract the contents as a list, then automatically close
    with open('word_list.txt', 'r') as imported_file:
        word_list = []
        for line in imported_file:
            word_list.append(line.strip())

    # Randomly choose a word from this list to use as the solution
    output = random.choice(word_list)
    return output


def create_list(solution):
    """Creates a list of the length of the solution with each item populated with a single '*'
    INPUT: Solution as a string
    OUTPUT: List length of string filled with '*'
    """
    output = []
    # Populate the output with '*' for as many values as are in the solution
    for i in range(len(solution)):
        output.append('*')

    return output


def print_status(displayed_word_list, lives):
    """"Print function that informs the user of the number of lives left and the progress in the game
    INPUT: List of solved/unsolved letters, Number of Lives
    OUTPUT: Print of 1 string describing lives left, print of 1 string displaying the game. No return
    """
    # Inform user of number of lives remaining
    print("Lives: {}".format(lives))

    # Create a single string from the displayed_word_list to print
    word_output = ""
    for i in range(len(displayed_word_list)):
        word_output += displayed_word_list[i]

    # Print the current status of the game showing which letters have been discovered and still remain
    print(word_output)


def letter_check(guess, solution, displayed_word_list, lives):
    """Checks if the guessed letter appears in the solution, and amends displayed_word_list and lives accordingly
    INPUT: guess as str, solution as str, displayed_word_list as list, lives_as int
    OUTPUT: returns updated lives as an int, displayed_word_list updated as it is mutable without return
    """
    # Automatically set any letters are found in the solution to be False
    found = False

    # Check each letter of the solution to see if the guessed letter appears in it
    for i in range(len(solution)):
        if guess == solution[i]:
            # Acknowledge that the guess was correct so that a life is not later removed
            found = True
            # Update the list from a '*' with the guessed letter in the correct locations
            displayed_word_list[i] = guess

    # If the guess did not match any of the letters in the solution, remove a life
    if found == False:
        lives -= 1

    return lives


# Initialise the program by choosing a solution, creating a list of '*' which will be updated, and set number of lives
solution = select_solution()
displayed_word_list = create_list(solution)
lives = 7

# While the user has lives, and still has outstanding letters to guess
while lives != 0 and '*' in displayed_word_list:
    # Print number of lives, and display the current status of the solution
    print_status(displayed_word_list, lives)

    # Accept user input, and make it lowercase to match solution
    guess = input("Please enter your next guess: ").lower()

    # Check if the input is in the word and update the displayed_word_list and lives accordingly
    lives = letter_check(guess, solution, displayed_word_list, lives)

# When game is complete, print status a final time to show completed word or all lives lost
print_status(displayed_word_list, lives)

# If lost, print that the user has lost
if lives == 0:
    print("you lose")

# If won, print that the user has won
elif '*' not in displayed_word_list:
    print("congratulations you win")
