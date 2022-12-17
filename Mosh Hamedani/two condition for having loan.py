# if applicant has high income AND good credit
# Eligible for loan

applicant_income = input("is your income high?\n: ")
applicant_credit = input("is your financial credit high?\n: ")

if applicant_credit == "Yes" or "yes" or "YES" and applicant_income == "Yes" or "yes":
    print("Congratulations!!!!!!\nYou're Eligible for loan.")
else:
    print("Unfortunately!! You did not meet all the requirements to get our support.")