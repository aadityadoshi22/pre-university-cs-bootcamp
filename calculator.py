# creation of a calculator
def square(n):
    return pow(n, 2)

def main():
    x = int(input("what is x? "))
    print("The square of x is:", square(x))

main()