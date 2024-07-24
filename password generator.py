import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = ''
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character type (uppercase, lowercase, digits, special) must be selected.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator App!\n")
    
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Length should be greater than zero.")
                continue
            
            use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
            use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
            use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
            use_special = input("Include special characters? (yes/no): ").lower() == 'yes'
            
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
            print(f"\nGenerated Password: {password}\n")
            
            if input("Generate another password? (yes/no): ").lower() != 'yes':
                print("Exiting Password Generator App...")
                break
        except ValueError as ve:
            print(f"Error: {ve}")
            continue

if __name__ == "__main__":
    main()
