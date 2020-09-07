name1 = input("Enter name here:")
print("Hi " + name1 + " I'm just practicing to remember how Python works.")
print("I'm gonna try to to make a calculator. " + name1 +" the only operators you can use are +,-,*,/.")
print("You can use decimal numbers too.")
num1 = float(input("Enter number here:"))
opera = input("Enter operator:")
num2 = float(input("Enter another number:"))

# Function to Add two numbers
def add(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

if opera == "+":
    print(num1, "+", num2, "=",
          add(num1, num2))
    print("\nSo another thing to make, is a mad libs game.")
    noun = input("Insert noun here:")
    adject = input("Insert Adjective here:")
    verb = input("Insert verb here:")

    print("\nMy favourite item is a/n " + noun)
    print("It is " + adject)
    print("I like to " + verb)



elif opera == "-":
    print(num1, "-", num2, "=",
          subtract(num1, num2))
    print("\nSo another thing to make, is a mad libs game.")
    noun = input("Insert noun here:")
    adject = input("Insert Adjective here:")
    verb = input("Insert verb here:")

    print("\nMy favourite item is " + noun)
    print("It is " + adject)
    print("I like to " + verb)



elif opera == "*":
    print(num1, "*", num2, "=",
          multiply(num1, num2))
    print("\nSo another thing to make, is a mad libs game.")
    noun = input("Insert noun here:")
    adject = input("Insert Adjective here:")
    verb = input("Insert verb here:")

    print("\nMy favourite item is a/n " + noun)
    print("It is " + adject)
    print("I like to " + verb)



elif opera == "/":
    print(num1, "/", num2, "=",
          divide(num1, num2))
    print("\nSo another thing to make, is a mad libs game.")
    noun = input("Insert noun here:")
    adject = input("Insert Adjective here:")
    verb = input("Insert verb here:")

    print("\nMy favourite item is a/n " + noun)
    print("It is " + adject)
    print("I like to " + verb)


else:
    print("Invalid input")
    print("\nSo another thing to make, is a mad libs game.")
    noun = input("Insert noun here:")
    adject = input("Insert Adjective here:")
    verb = input("Insert verb here:")

    print("\nMy favourite item is a/n " + noun)
    print("It is " + adject)
    print("I like to " + verb)
    




