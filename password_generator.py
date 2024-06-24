import string
import random
import secrets

def generate_password():
    print("Welcome to the PyPassword Generator!")

    while True:
        try:
            nr_letters = int(input("How many letters would you like in your password?\n"))
            nr_symbols = int(input("How many symbols would you like?\n"))
            nr_numbers = int(input("How many numbers would you like?\n"))
            break
        except ValueError:
            print("Please enter valid numbers for letters, symbols, and numbers.")

    letters = [secrets.choice(string.ascii_letters) for _ in range(nr_letters)]
    symbols = [secrets.choice(string.punctuation) for _ in range(nr_symbols)]
    numbers = [secrets.choice(string.digits) for _ in range(nr_numbers)]

    password_list = letters + symbols + numbers
    random.shuffle(password_list)
    generated_password = ''.join(password_list)

    print(f"Your password is: {generated_password}")

if __name__ == "__main__":
    generate_password()
