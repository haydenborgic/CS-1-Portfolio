#LoanPayment.pt

"""
This program will take the principal, interest rate, and number of years on a loan
and give the user the monthly payment, the total of the payments over the years, 
and the total interest paid over the given time period. It will then print an 
amortization table breaking down how each monthly payment is divided into paying
the interest and principal.
"""


def loan_payment(loan_principal, loan_interest, time_of_loan):
    monthly_payment = (loan_principal * (loan_interest / 12)) / (1 - (1 + loan_interest / 12) ** (-12 * time_of_loan))
    return monthly_payment




loan_amount = float(input("Enter the loan amount: "))
loan_rate = float(input("Enter annual rate as a decimal: "))
loan_length = int(input("Enter the number of years of the loan: "))

pay_monthly = loan_payment(loan_amount, loan_rate, loan_length)
total_payments1 = pay_monthly * 12 * loan_length
total_interest1 = total_payments1 - loan_amount



print(f"\nThe monthly payment will be ${pay_monthly:.2f}")
print(f"The total payments over {loan_length} years will be ${total_payments1:.2f}")
print(f"The total interest paid over {loan_length} years will be ${total_interest1:.2f}")



print("\n \nLoan Amorization Table: \n \nMonth \t Interest payment \t Principal Payment \t Remaining Balance")


remaining_balance1 = loan_amount
interest_payment = 0
month = 1

while month <= loan_length * 12:
    interest_payment = 1/12 * loan_rate * remaining_balance1
    principal_payment = pay_monthly - interest_payment
    remaining_balance1 = remaining_balance1 - principal_payment
    print(f"{month} \t \t {interest_payment:.2f} \t \t \t {principal_payment:.2f} \t \t \t {remaining_balance1:.2f}")
    month += 1