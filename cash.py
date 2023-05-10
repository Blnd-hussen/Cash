def main():

    # Ask how many cents the customer is owed
    cents = get_cents()
    cents = cents * 100
    
    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    coins = quarters + dimes + nickels + pennies
    print(coins)


def get_cents():
    while True:
        cents = input("Change owed: ")
        if cents.replace(".", "").isdigit() and float(cents) > 0:
            return float(cents)
            

def calculate_quarters(cents):
    quarters = 0
    while cents >= 25:
        cents = cents - 25
        quarters += 1
    
    return quarters


def calculate_dimes(cents):
    dimes = 0
    while cents >= 10:
        cents = cents - 10
        dimes += 1
    
    return dimes


def calculate_nickels(cents):
    nickles = 0
    while cents >= 5:
        cents = cents - 5
        nickles += 1
    
    return nickles


def calculate_pennies(cents):
    pennis = 0
    while cents >= 1:
        cents = cents - 1
        pennis += 1
    
    return pennis


main()