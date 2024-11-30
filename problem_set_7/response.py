from validator_collection import validators, errors

def main():
    # Get email address from user
    email = input("What's your email? ").strip()
    
    try:
        # Attempt to validate the email
        if validators.email(email):
            print("Valid")
    except (errors.InvalidEmailError, ValueError):
        print("Invalid")

if __name__ == "__main__":
    main()