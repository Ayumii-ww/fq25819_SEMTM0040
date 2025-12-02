# Vichaya Tedumrongvanich (fq25819, SEMT0040 Summative Assessment)
# main.py

from FlowerShop import FlowerShop


def get_input(prompt, default=None):
    """
    Helper to read an integer from input, with optional default.

    Keeps asking until user gives a valid non-negative integer.
    If default is given, pressing Enter with no input returns the default.
    """
    while True:
        raw = input(prompt).strip()
        if not raw:
            if default is not None:
                return default
            print("Please enter a number.")
            continue

        if (raw.startswith("0") and raw != "0"):
            print("Invalid input. Do not include leading zeros.")
            continue
        
        try:
            value = int(raw)
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print("Invalid input, please enter an integer.")


def hire_initial_florists(shop):
    """
    Ensure at least one florist is hired at the very start of the game.
    """
    print("You must have at least one florist to start.\n")
    while len(shop.florists) == 0:
        name = input("Enter florist name: ").strip()
        if not name:
            print("Name cannot be empty.\n")
            continue

        # Ask for speciality until a valid choice is given
        while True:
            print("\nSelect speciality:")
            print("    0 = None")
            print("    1 = Fern-tastic")
            print("    2 = Be-Leaf in Yourself")
            print("    3 = You Rose to the Occasion")

            spec_choice = input("Enter number (default 0): ").strip()

            if spec_choice in ("", "0"):
                speciality = None
                break
            elif spec_choice == "1":
                speciality = "Fern-tastic"
                break
            elif spec_choice == "2":
                speciality = "Be-Leaf in Yourself"
                break
            elif spec_choice == "3":
                speciality = "You Rose to the Occasion"
                break
            else:
                print("Invalid input. Please enter 0, 1, 2, or 3.\n")

        try:
            shop.add_florist(name, speciality)
        except ValueError as e:
            print(e)
            print("Please enter a different florist.\n")


def manage_florists(shop):
    """
    Manage hiring or firing florists at the start of each month.
    """

    print(f"\nCurrent number of florists: {len(shop.florists)}")
    


    # Hiring florists
    while True:
        hire_count = get_input(
            "How many florists would you like to \033[1mHIRE\033[0m this month? (0 for none): ",
            default=0
        )

        max_hire = 4 - len(shop.florists)

        if hire_count == 0:
            break

        if max_hire <= 0:
                print("You already have maximum of 4 florists. Cannot hire more.\n")
                hire_count = 0
                break

        if hire_count > max_hire:
            print(
                f"You already have {len(shop.florists)} florist(s),"
                f"so you can only hire up to {max_hire} more this month.\n"
            )
            print("Please enter valid number.\n")
            continue
        
        break

    if hire_count > 0:

        for i in range(hire_count):
            while True:
                name = input("Please input florist name (one at a time): ").strip()
                if not name:
                    print("Name cannot be empty.")
                    continue
                # Ask for speciality until a valid choice is given
                while True:
                    print("\nSelect speciality:")
                    print("    0 = None")
                    print("    1 = Fern-tastic")
                    print("    2 = Be-Leaf in Yourself")
                    print("    3 = You Rose to the Occasion")

                    spec_choice = input("Enter number (default 0): ").strip()

                    if spec_choice in ("", "0"):
                        speciality = None
                        break
                    elif spec_choice == "1":
                        speciality = "Fern-tastic"
                        break
                    elif spec_choice == "2":
                        speciality = "Be-Leaf in Yourself"
                        break
                    elif spec_choice == "3":
                        speciality = "You Rose to the Occasion"
                        break
                    else:
                        print("Invalid input. Please enter 0, 1, 2, or 3.\n")
                            
                try:
                    shop.add_florist(name, speciality)
                    break
                except ValueError as e:
                    print(e)
                    print("Please enter a different florist.\n")

    # Firing florists
    # Must keep at least 1 florist
    max_fire = max(0, len(shop.florists) - 1)
    if max_fire == 0:
        print("You must employ at least one florist. No one can be fired.\n")
        return
    
    while True:

        fire_count = get_input(
            "How many florists would you like to \033[1mFIRE\033[0m this month? (0 for none): ", 
            default=0
        )

        if fire_count > max_fire:
            print(f"You can only \033[1mFIRE\033[0m up to {max_fire} florists this month.")
            print("Please enter a valid number.\n")
            continue
        break

    for i in range(fire_count):
        while True:
            print("\nCurrent florists you can fire:")
            for florist in shop.florists:
                print(f"  - {florist.name}")

            name = input("Enter the name of the florist to \033[1mFIRE\033[0m: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            try:
                shop.remove_florist(name)
                break
            except ValueError as e:
                print(e)
                print("Please enter a valid florist name.\n")
    
    if shop.florists:
        print("Current staff:")
        for florist in shop.florists:
            print(f"   - {florist}")
    else:
        print("Current staff: []")


def get_production_plan(shop):
    """
    Prompt the user for how many of each bouquet type to sell this month.

    Ensures that:
    - quantities are integers,
    - quantities do not exceed demand,
    - plan fits within supply and labour constraints.
    """
    bouquet_names = list(shop.bouquets.keys())

    while True:
        print("\nHow much of each bouquet would you like to sell?")

        plan = {}
        for name in bouquet_names:
            bouquet = shop.bouquets[name]
            while True:
                qty = get_input(f"{name}: ")
                if qty > bouquet.monthly_demand:
                    print(
                        "This exceeds the demand for this bouquet "
                        f"({bouquet.monthly_demand})."
                    )
                    continue
                plan[name] = qty
                break

        # Check supply and labour constraints
        if not shop.check_supply(plan):
            print(
                "\nThis production plan cannot be done with current "
                "greenhouse supplies. Please enter a smaller plan.\n"
            )
            continue

        if not shop.check_labor(plan):
            print(
                "\nThis production plan cannot be done with current "
                "florist labour capacity. Please enter a smaller plan.\n"
            )
            continue

        return plan


def restock_greenhouse(shop):
    """
    Handle user interaction for restocking the greenhouse.

    Uses FlowerShop.choose_vendor_for_supply to let the owner pick a vendor
    for each type of flower, then calls Greenhouse.restock with those prices.
    """
    from Greenhouse import Greenhouse  # local import to avoid circular hints

    stock = shop.greenhouse.current_stock()
    if (
        stock["greenery"] >= Greenhouse.MAX_GREENERY
        and stock["roses"] >= Greenhouse.MAX_ROSES
        and stock["daisies"] >= Greenhouse.MAX_DAISIES
    ):
        # Already full, nothing to do
        return 0.00

    print("\nThe greenhouse has spare capacity and needs to be restocked...\n")

    # Choose vendor for each supply type
    greenery_price = shop.choose_vendor_for_supply("greenery")
    roses_price = shop.choose_vendor_for_supply("roses")
    daisies_price = shop.choose_vendor_for_supply("daisies")
    

    # Perform the actual restock and deduct from cash
    restock_cost = shop.greenhouse.restock(
        greenery_price=greenery_price,
        roses_price=roses_price,
        daisies_price=daisies_price,
    )
    shop.cash_balance -= restock_cost

    print(f"\n    + Flower restock costs: £{restock_cost:.2f}")
    return restock_cost


def main():
    """
    Main entry point for running the FlowerShop simulation.
    """
    print("---------------------------------------------------------------")
    print("Welcome to the FlowerShop Simulator!")
    print("---------------------------------------------------------------\n")

    months = get_input(
        "How many months would you like to run the game for? (default 6): ",
        default=6,
    )

    shop = FlowerShop()
    month_counter = 0
    bankrupt_reason = None

    # Hire at least one florist before month 1 starts
    if len(shop.florists) == 0:
        hire_initial_florists(shop)

    for month in range(1, months + 1):
        month_counter = month
    

        print(f"\nMonth: {month}\n")

        #Extension: Show loan status and apply monthly interest
        if shop.has_loan():
            print(f"Current Loan Balance: £{shop.loan_balance:.2f}")
            shop.apply_loan_interest()
            shop.auto_repay_loan()

        print(
            "Before the month starts, there are some owner actions for you to carry\n"
            "out. First, review the number of staff, then decide how many bouquets to\n"
            "sell.\n"
        )

        manage_florists(shop)

        # Decide on quantities for each bouquet type
        production_plan = get_production_plan(shop)

        print("\n----------------------------------------")
        print("Month in progress...")
        print("----------------------------------------\n")

        start_cash = shop.cash_balance
        summary = shop.end_month_process(production_plan)

        print("End of month calculations:\n")
        print(f"Cash Balance, Month Start: £{start_cash:.2f}")
        print(f"    Income: £ {summary['Income from Bouquets']:.2f}")
        print("    Outgoings:")
        print(f"        Employee costs: £ {summary['Labor Cost']:.2f}")
        print(f"        Greenhouse costs: £ {summary['Greenhouse Cost']:.2f}")
        print(f"        Rent: £ {summary['Rent Paid']:.2f}\n")

        # Show current status
        print("Current shop status:\n")
        print("    Current staff:", [str(florist) for florist in shop.florists])
        stock = shop.greenhouse.current_stock()
        print("\n    Greenhouse quantity:")
        print(f"        Greenery: {stock['greenery']}")
        print(f"        Roses: {stock['roses']}")
        print(f"        Daisy: {stock['daisies']}")
        
        

        # Restock greenhouse (vendor choice is handled inside)
        restock_greenhouse(shop)

        print(f"    End of month Cash Balance: £{shop.cash_balance:.2f}\n")

        if shop.bankrupt():
            print("Warning: Your cash balance is below £0.\n")
            choice = input(
                "Would you like to take a bank loan to try to save the shop? (y/n):"
            ).strip().lower()

            if choice == "y":
                
                needed = -shop.cash_balance 

                #Estimate next month fixed cost
                estimate_salaries = 0.0
                for florist in shop.florists:
                    estimate_salaries += florist.monthly_salary()

                from Greenhouse import Greenhouse  # local import 
                estimate_greenhouse = (
                    Greenhouse.MAX_GREENERY * Greenhouse.COST_GREENERY +
                    Greenhouse.MAX_ROSES * Greenhouse.COST_ROSES +
                    Greenhouse.MAX_DAISIES * Greenhouse.COST_DAISIES
                )

                estimate_rent = FlowerShop.MONTHLY_RENT

                buffer = estimate_salaries + estimate_greenhouse + estimate_rent
                suggested_loan = needed + buffer

                print(
                    f"\nYou need at least £{needed:.2f} to stay."
                    f" to get back to zero cash."
                )

                print(
                    "Based on your current staff and a full greenhouse, "
                    "next month's estimated fixed costs are roughly:\n"
                    f"    Rent:             £{estimate_rent:.2f}\n"
                    f"    Florist salaries: £{estimate_salaries:.2f}\n"
                    f"    Greenhouse cost:  £{estimate_greenhouse:.2f}\n"
                    f"Total estimated buffer needed: £{buffer:.2f}\n"
                )

                print(
                    f"For safety, we suggest borrowing about £{suggested_loan:.2f} "
                    f"(you can change this).\n"
                )
                
                #Ask how much to borrow
                while True: 
                    raw = input("\nEnter loan amount to borrow: £").strip()
                    try:
                        amount = float(raw)
                        if amount <= 0:
                            print("Loan amount must be positive\n")
                            continue
                        break
                    except ValueError as e:
                        print(e)
                        print("Please enter a valid loan amount.\n")

                if amount < suggested_loan:
                    bankrupt_reason = "below_suggested"
                    print(
                        "\nThe loan you chose is less than the suggested amount"
                    )
                    break

                shop.take_loan(amount)

                if shop.bankrupt():
                    bankrupt_reason = "insufficient_loan"
                    print(
                        "\nEven after taking a loan, your cash balance is still negative . "
                        "The shop has gone bankrupt.\n"
                    )
                    break

            else: 
                bankrupt_reason = "refused_loan"
                break

    print("\n***********************************************************************")
    if shop.bankrupt():
        # Shop ended early due to bankruptcy
        if bankrupt_reason == "insufficient_loan":
            print(
                f"You planned to run the shop for {months} months, "
                f"but it went bankrupt in month {month_counter}."
            )
            print(
                "Even after taking a bank loan, your cash balance was still below £0,\n"
                "so you could not cover this month's expenses. The simulation has ended."
            )
        elif bankrupt_reason == "refused_loan":
            print(
                f"You planned to run the shop for {months} months, "
                f"but it went bankrupt in month {month_counter}."
            )
            print(
                "Your cash balance fell below £0 and you chose not to take a bank loan,\n"
                "so there was not enough money to pay this month's costs."
            )
        elif bankrupt_reason == "below_suggested":
            print(
                f"You planned to run the shop for {months} months, "
                f"but it went bankrupt in month {month_counter}.\n"
            )
            print(
                "You took a loan that was smaller than the suggested amount based on\n"
                "your deficit and next month's fixed costs, so the shop did not have"
                "enough money to continue operating."
            )
        else:
            # Just in case we hit bankruptcy without the loan logic
            print(
                f"The shop has gone bankrupt in month {month_counter} because your\n"
                f"cash balance fell below £0. The simulation has ended."
            )
    else:
        # Completed all months
        print(
            f"Congratulations! You have completed the simulation "
        )
    


if __name__ == "__main__":
    main()