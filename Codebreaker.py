import random
from colorama import Fore, Style, init

init(autoreset=True)


def generate_secret_code(length=4):
    numbers = [str(i) for i in range(10)]
    return ''.join(random.sample(numbers, length))


def validate_guess(guess, length):
    return len(guess) == length and guess.isdigit()


def provide_feedback(guess, secret_code):
    correct_position = sum(guess[i] == secret_code[i] for i in range(len(guess)))

    correct_but_wrong_pos = sum(min(guess.count(digit), secret_code.count(digit)) for digit in set(guess))
    correct_but_wrong_pos -= correct_position

    return correct_position, correct_but_wrong_pos


def print_remaining_attempts(attempts, max_attempts):
    remaining_attempts = max_attempts - attempts
    print(f"{Fore.YELLOW}Remaining attempts: {remaining_attempts}")


def play_codebreaker():
    secret_code = generate_secret_code()
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        guess = input("\nEnter your 4-digit guess: ")

        if not validate_guess(guess, 4):
            print(f"{Fore.RED}Invalid guess. Please enter a 4-digit number.")
            continue

        attempts += 1
        correct_position, correct_but_wrong_pos = provide_feedback(guess, secret_code)

        print(f"{Fore.GREEN}Attempt {attempts}: {correct_position} correct position(s), "
              f"{correct_but_wrong_pos} correct but in wrong position")
        print_remaining_attempts(attempts, max_attempts)

        if guess == secret_code:
            print(f"{Fore.BLUE}Congratulations! You guessed the code in {attempts} tries.")
            break
    else:
        print(f"{Fore.RED}Game over! The secret code was {secret_code}.")


play_codebreaker()
