# A simple program to calculate the square of a number

def calculate_square(number):
    return number ** 2

# Example usage
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The square of {num} is {calculate_square(num)}")