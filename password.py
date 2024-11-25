import random
import string

def generate_password(length, use_special_chars, use_numbers, use_uppercase):
    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ""
    numbers = string.digits if use_numbers else ""
    special = string.punctuation if use_special_chars else ""
    
    # Combine character pools
    all_chars = lower + upper + numbers + special
    
    if not all_chars:
        print("Error: No character types selected!")
        return None
    
    # Generate password
    password = "".join(random.choices(all_chars, k=length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    
    # Get user input
    length = int(input("Enter password length: "))
    use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    
    # Generate and display password
    password = generate_password(length, use_special_chars, use_numbers, use_uppercase)
    if password:
        print(f"\nGenerated Password: {password}\n")

if __name__ == "__main__":
    main()
