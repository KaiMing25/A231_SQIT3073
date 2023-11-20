import os
os.system('cls')

# monthly installment calculation
def monthly_installment_calculation(principal, interest_rate, year):
    interest_rate_per_month = (interest_rate / 100) / 12
    loan_term = year * 12
    monthly_payment = principal * ((interest_rate_per_month*((1 + interest_rate_per_month)**loan_term))/(((1 + interest_rate_per_month)**loan_term)-1))
    return monthly_payment

# total payable amount calculations
def total_payable_amount_calculation(monthly_payment, year):
    total_payable_amount = (monthly_payment * 12) * year
    return total_payable_amount

# dsr calculations
def debt_service_ratio_dsr_calculation(housing_loan, monthly_income, monthly_installment, commitments):
    total_commitments = housing_loan + commitments
    dsr = ((total_commitments + monthly_installment) / monthly_income) * 100
    return dsr

# display previous loan calculations
def display_previous_loan_calculations(loan_calculations):
    print("\n=======================================================")
    print("<<<<<<<<<<<<< PREVIOUS LOAN CALCULATIONS >>>>>>>>>>>>>>")
    print("=======================================================\n")

    for i, each in enumerate(loan_calculations, start=1):
        print(str(i) + '')
        print("PRINCIPAL                : RM " + str(round(each['principal'], 2)))
        print("MONTHLY INSTALLMENT      : RM " + str(round(each['monthly_payment'], 2)))
        print("TOTAL PAYABLE AMOUNT     : RM " + str(round(each['total_payable_amount'], 2)))
        print("DEBT SERVICE RATIO (DSR) : " + str(round(each['dsr'], 2)) + "%")
        print("YOUR ELIGIBILITY         : " + str(each['eligibility']))
        print()

# edit loan calculations
def edit_loan_calculations(loan_calculations, index):

    try:
        # show current record
        display_previous_loan_calculations([loan_calculations[index]])

        # get user input for new values
        new_monthly_income = float(input("PLEASE ENTER YOUR NEW MONTHLY INCOME                       : RM "))
        new_principal      = float(input("PLEASE ENTER YOUR NEW LOAN AMOUNT (principal)              : RM "))
        new_interest_rate  = float(input("PLEASE ENTER YOUR NEW INTEREST RATE                        : "))
        new_loan_term      = int(input("PLEASE ENTER YOUR NEW LOAN TERM IN YEARS [EXAMPLE : 10 ]   : "))
        new_housing_loan   = float(input("ENTER YOUR NEW HOUSING LOAN AMOUNT                         : RM "))
        new_commitments    = float(input("ENTER YOUR NEW OTHER POSSIBLE MONTHLY COMMITMENTS          : RM "))

        # recalculate values based on user input
        new_monthly_payment = monthly_installment_calculation(new_principal, new_interest_rate, new_loan_term)
        new_total_payable_amount = total_payable_amount_calculation(new_monthly_payment, new_loan_term)

        # update the loan record
        loan_calculations[index]['monthly_income'] = new_monthly_income
        loan_calculations[index]['principal'] = new_principal
        loan_calculations[index]['monthly_payment'] = new_monthly_payment
        loan_calculations[index]['total_payable_amount'] = new_total_payable_amount

        print("\n=======================================================")
        print("<<<<<<<<<<<< LOAN RECORD UPDATED SUCCESSFULLY >>>>>>>>>>")
        print("=======================================================")

    except ValueError:
        print("<<<<<<< THE INPUT IS INVALID. PLEASE ENTER A VALID VALUE. >>>>>>>")

# main menu
def main():
    print("==============================================================================")
    print("<<<<<<<     Welcome to Housing Loan Eligibility and DSR Calculator     >>>>>>>")
    print("==============================================================================\n")

    loan_calculations = []

    while True:
        print("-------------------------------------------------------")
        print("<<<<<<<<<<<<<< PLEASE ENTER YOUR OPTION  >>>>>>>>>>>>>>")
        print("-------------------------------------------------------")
        print("1 - CALCULATE LOAN")
        print("2 - DISPLAY PREVIOUS LOAN CALCULATIONS")
        print("3 - EDIT PREVIOUS LOAN RECORDS")
        print("4 - EXIT THE PROGRAM")
        print()

        choice = input("ENTER YOUR CHOICE IN NUMBER [1 , 2 , 3 , 4] : ")
        print()

        # option 1 - calculate loan
        if choice == '1':
            # message for monthly income
            print("\n------------------------------------------------------------------------------")
            print("<<<<<<<<<<<<<<<<<<<<  YOU MAY TELL US YOUR MONTHLY INCOME >>>>>>>>>>>>>>>>>>>>")
            print("BEFORE YOU ENTER YOUR MONTHLY INCOME, PLEASE MAKE SURE IT IS NOT A ZERO VALUE")
            print("------------------------------------------------------------------------------\n")
            
            monthly_income = float(input("MONTHLY INCOME                                  : RM "))
            principal     = float(input("PLEASE ENTER THE LOAN AMOUNT(principal)         : RM "))
            interest_rate = float(input("PLEASE ENTER YOUR ANNUAL INTEREST RATE          : "))
            year          = int(input("ENTER YOUR LOAN TERM IN YEARS [EXAMPLE : 10 ]   : "))
            housing_loan  = float(input("ENTER YOUR HOUSING LOAN AMOUNT                  : RM "))
            monthly_payment = monthly_installment_calculation(principal, interest_rate, year)
            commitments   = float(input("ENTER YOUR OTHER POSSIBLE MONTHLY COMMITMENTS   : RM "))

            dsr = debt_service_ratio_dsr_calculation(housing_loan, monthly_income, monthly_payment, commitments)

            # check the eligibility according to the dsr threshold (70%)
            if dsr <= 70:
                eligibility = "You are eligible"
            else:
                eligibility = "You are not eligible"

            # store results in loan_calculations
            loan_calculations.append(
                {'principal'            : principal, 
                 'monthly_payment'      : monthly_payment,
                 'total_payable_amount' : total_payable_amount_calculation(monthly_payment, year),
                 'dsr'                  : dsr, 
                 'eligibility'          : eligibility})
            
            # print message for completed loan calculations
            print("\n=======================================================")
            print("<<<<<<<<<<<<< LOAN CALCULATIONS COMPLETED >>>>>>>>>>>>>")
            print("=======================================================")
            
            # print the results
            print("PRINCIPAL                : RM", round(principal, 2))
            print("MONTHLY INSTALLMENT      : RM", round(monthly_payment, 2))
            print("TOTAL PAYABLE AMOUNT     : RM", round(total_payable_amount_calculation(monthly_payment, year), 2))
            print("DEBT SERVICE RATIO (DSR) :", round(dsr, 2), "%")
            print("YOUR ELIGIBILITY         :", eligibility, "\n")

        # option 2 - display previous loan calculation
        elif choice == '2':
            display_previous_loan_calculations(loan_calculations)

        # option 3 - edit previous loan records
        elif choice == '3':
            display_previous_loan_calculations(loan_calculations)

            # confirm again the index on which record to edit
            try:
                index = int(input("ENTER THE INDEX OF THE RECORD TO EDIT : ")) - 1
                print()
                if 0 <= index < len(loan_calculations):
                    # edit the selected record by passing the index
                    edit_loan_calculations(loan_calculations, index)

                    # show updated record
                    print()
                    print("------------------------------")
                    print("<<<<<<< UPDATED RECORD >>>>>>>")
                    print("------------------------------")
                    display_previous_loan_calculations([loan_calculations[index]])

                # error message when user entered an invalid input
                else:
                    print("<<<<< INVALID, PLEASE TRY AGAIN >>>>>\n\n")

            # error message when user entered an invalid input
            except ValueError:
                print("<<<<<   THE INPUT IS INVALID. PLEASE ENTER A VALID INDEX   >>>>>")

        # print message for exiting the system
        elif choice == '4':
            print("<<<<< THANK YOU FOR USING THE SYSTEM >>>>>")
            print("------------------------------------------")
            print("YOU ARE NOW EXITING THE PROGRAM , GOODBYE.\n\n")
            break

        # error message when user entered an invalid input
        else:
            print("<<<<<<< INVALID CHOICE, PLEASE TRY AGAIN, MAKE SURE YOU ENTER A VALID OPTION >>>>>>>\n")

if __name__ == "__main__":
    main()
