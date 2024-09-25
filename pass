import random
import string
def generate_password(length,use_letters,use_numbers,use_symbols):
    char_pool=""
    if use_letters:
        char_pool+=string.ascii_letters
    if use_numbers:
        char_pool+=string.digits
    if use_symbols:
        char_pool+=string.punctuation
    if not char_pool:
        print("You must select at least one character type (letters, numbers, or symbols).")
        return None
    password=''.join(random.choice(char_pool)for _ in range(length))
    return password
def main():
    print("Welcome to the Password Generator!")
    try:
        length=int(input("Enter the desired password length: "))
        if length<=0:
            print("Password length must be greater than 0.")
            return
        use_letters=input("Include letters? (y/n): ").strip().lower()=='y'
        use_numbers=input("Include numbers? (y/n): ").strip().lower()=='y'
        use_symbols=input("Include symbols? (y/n): ").strip().lower()=='y'
        password=generate_password(length,use_letters,use_numbers,use_symbols)
        if password:
            print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")
if __name__=="__main__":
    main()
