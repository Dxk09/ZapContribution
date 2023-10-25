def encode_password(password): # function that encodes password by incrementing each digit by three.
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def main():
    encoded_password = None  # Initialize encoded_password to None
    psw_encode = None  # Initialize psw_encode to None

    while True:
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        user_input = input("\nPlease enter an option: ")

        if user_input == '1':
            psw_encode = input("\nPlease enter your password to encode: ")
            encoded_password = encode_password(psw_encode)
            print("Your password has been encoded and stored!")

        elif user_input == '2':
            if encoded_password:
                print(f"Your encoded password is {encoded_password}, and the original password is {psw_encode}.")

        elif user_input == '3':
            break  # Exit the loop when '3' is selected

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == '__main__':
    main()
