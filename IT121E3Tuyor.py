try:
    username = input("Enter username: ")
    age = int(input("Enter age: "))

    with open("users.txt", "a") as file:
        file.write(f"{username} - {age}\n")

    print("\nUser saved successfully!\n")

except ValueError:
    print("Error: Age must be a number.")

except Exception as e:
    print("Unexpected error:", e)

finally:
    try:
        print("\nSaved Users:")
        with open("users.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No users saved yet.")

    print("\nSystem complete.")
