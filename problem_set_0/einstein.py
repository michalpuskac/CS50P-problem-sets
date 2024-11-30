#Implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

# Define the speed of light as a constant
SPEED_OF_LIGHT = 300000000 #meters per second

def formula(mass):
    """Calculates energy (in Joules) from mass (in kilograms) using E=mc^2."""
    energy = mass * SPEED_OF_LIGHT**2
    return energy

def main():
    mass = int(input("Enter mass in kilograms (M): "))
    energy = formula(mass)
    print(f" Equivalent energy (E) = {energy:,} joules")

if __name__ == "__main__":
    main()