print("=" * 55)
print("Welcome to the Pattern Generator and Number Analyzer!")
print("=" * 55)

while True:
    print("\nSelect an option:")
    print("1. Generate a pattern")
    print("2. Analyze a range of numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            rows = int(input("Enter the number of rows for the pattern: "))

            print("\nPattern:")
            for i in range(1, rows + 1):
                print("* " * i)

        case 2:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))

            total = 0

            for num in range(start, end + 1):
                if num % 2 == 0:
                    print(f"Number {num} is even")
                else:
                    print(f"Number {num} is odd")

                total += num

            print(f"Sum of all numbers from {start} to {end} is: {total}")

        case 3:
            print("Exiting the program, Goodbye!")
            break

        case _:
            print("Invalid choice! Please select 1, 2, or 3.")