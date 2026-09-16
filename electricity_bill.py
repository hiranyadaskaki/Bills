# electricity_bill.py

def calculate_electricity_bill(units):
    if units <= 0:
        bill = 0.0
    elif units <= 100:
        bill = units * 5.0
    elif units <= 200:
        bill = (100 * 5.0) + ((units - 100) * 7.0)
    else:
        bill = (100 * 5.0) + (100 * 7.0) + ((units - 200) * 10.0)
    return bill

if __name__ == "__main__":
    print("--- Electricity Bill Calculator ---")
    try:
        units = float(input("Enter units consumed: "))
        amount = calculate_electricity_bill(units)
        print(f"Total Units: {units}")
        print(f"Final Bill Amount: ₹{amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numerical value for units.")
