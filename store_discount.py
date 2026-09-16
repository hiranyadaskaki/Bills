# store_discount.py

def calculate_discount(amount):
    if amount >= 5000:
        discount_percent = 20
    elif 2000 <= amount <= 4999:
        discount_percent = 10
    else:
        discount_percent = 0

    discount_amount = (amount * discount_percent) / 100.0
    final_payable = amount - discount_amount
    return discount_percent, discount_amount, final_payable

if __name__ == "__main__":
    print("--- Online Store Discount Calculator ---")
    try:
        purchase_amount = float(input("Enter purchase amount (₹): "))
        pct, disc, final = calculate_discount(purchase_amount)
        print("\n--- Summary ---")
        print(f"Original Amount:      ₹{purchase_amount:.2f}")
        print(f"Discount Amount ({pct}%): ₹{disc:.2f}")
        print(f"Final Payable Amount: ₹{final:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid purchase amount.")
