try:
    num = int(input("Enter a number to display its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# Display the multiplication table
print(f"Multiplication Table for {num}:")
for i in range(1, 11):  # Loop from 1 to 10
    product = num * i
    print(f"{num} x {i} = {product}")
