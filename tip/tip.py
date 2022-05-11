def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    # define variable dollars, use built-in function replace to replace $ with blank
    dollars = d.replace('$', '')
    # return float function to convert string (string comes from the user input from main function) to float
    return float(dollars)

def percent_to_float(p):
    # TODO
    # define variable percent, use built-in function replace to replace % with blank
    percent = p.replace('%', '')
    # return float function to convert string (string comes from the user input from main function) to float and divide by 100 to convert e.g. 10% to 0.10
    return float(percent)/100

main()