def game():
    numbers = []
    print("Enter numbers one by one. Type 'q' to finish.")

    while True:
        user_input = input("Insert number: ")

        # Stop if user enters 'q'
        if user_input.lower() == 'q':
            break

        # Validate input and add to list
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            numbers.append(int(user_input))
        else:
            print("Invalid input! Please enter a valid number or 'q' to quit.")

    if numbers:  # Check if list is not empty
        largest = max(numbers)
        smallest = min(numbers)
        print(f"Largest number is {largest}")
        print(f"Smallest number is {smallest}")
    else:
        print("No numbers were entered.")

game()
