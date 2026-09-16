# bank_loan.py

def evaluate_loan(age, salary, credit_score):
    if age < 21 or age > 60:
        return "Rejected: Age must be between 21 and 60 years."
    if salary < 30000:
        return "Rejected: Monthly salary must be at least ₹30,000."
    
    if credit_score >= 750:
        return "Approved"
    elif 650 <= credit_score <= 749:
        return "Approved with Guarantor"
    else:
        return "Rejected: Credit score below 650."

if __name__ == "__main__":
    print("--- Bank Loan Approval System ---")
    try:
        age = int(input("Enter Age: "))
        salary = float(input("Enter Monthly Salary (₹): "))
        credit_score = int(input("Enter Credit Score: "))
        
        status = evaluate_loan(age, salary, credit_score)
        print(f"\nLoan Decision: {status}")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")
