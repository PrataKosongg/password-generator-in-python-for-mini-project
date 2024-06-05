import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        return "Error! No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    use_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lower = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
