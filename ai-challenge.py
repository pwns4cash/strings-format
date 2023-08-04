#!/usr/bin/env python3

secret = "This is a secret!"
    

def main():
    user_input = input("Enter your name: ")
    print("Hello, " + user_input + "!")

    user_input = input("Enter a message: ")
    print(user_input)

    
    user_input = input("Enter a format string: ")
    print(user_input.format(secret=secret))

if __name__ == "__main__":
    main()
