import random as rand
import string as strng

def generate_and_print_password():
    try:
        length = int(input("Enter required length of password:"))
        if length <= 0:
            print("Length should be a positive integer.")
        else:
            print(f"Requested password from (0-{length}):", ''.join(rand.choice(strng.ascii_letters + strng.digits + strng.punctuation) for _ in range(length)))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

generate_and_print_password()
