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

        speciality = input(
            "Enter speciality bouquet name (or leave blank for none): "
        ).strip()
        if not speciality:
            speciality = None

        try:
            shop.add_florist(name, speciality)
        except ValueError as e:

            # Duplicate name or too many florists (more than 4)
            print(e)
            print("Please enter a different florist.\n")


def manage_florists(shop):
    """
    Manage hiring or firing florists at the start of each month.
    """

    print(f"\nCurrent number of florists: {len(shop.florists)}")
    if shop.florists:
        print("Current staff:")
        for florist in shop.florists:
            print(f"   - {florist}")
    else:
        print("Current staff: []")


    # Hiring florists
    hire_count = get_input(
        "How many florists would you like to **HIRE** this month? (0 for none): ",
         default=0
    )

    if hire_count > 0:
        for iด in range(hire_count):
            if len(shop.florists) >= 4:
                print("You already have the maximum of 4 florists. Cannot hire more.\n")
                break

            while True:
                name = input("Please input florist name (one at a time): ").strip()
                if not name:
                    print("Name cannot be empty.")
                    continue

                speciality = input(
                    "Enter speciality bouquet name (or leave blank for none): "
                ).strip()
                if not speciality:
                    speciality = None

                try:
                    shop.add_florist(name, speciality)
                    break
                except ValueError as e:
                    print(e)
                    print("Please try a different name.\n")

    # Firing florists
    # Must keep at least 1 florist
    max_fire = max(0, len(shop.florists) - 1)
    if max_fire == 0:
        print("You must employ at least one florist. No one can be fired.\n")
        return

    fire_count = get_input("How many florists would you like to **FIRE** this month? (0 for none): ", default=0)

    if fire_count > max_fire:
        print(f"You can only **FIRE up to {max_fire} florists this month.")
        fire_count = max_fire

    for i in range(fire_count):
        while True:
            name = input("Enter the name of the florist to **FIRE**: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            try:
                shop.remove_florist(name)
                break
            except ValueError as exc:
                print(exc)
                print("Please enter a valid florist name.\n")


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
        return 0.0

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

    # Hire at least one florist before month 1 starts
    if len(shop.florists) == 0:
        hire_initial_florists(shop)

    for month in range(1, months + 1):
        month_counter = month
        if shop.bankrupt():
            break

        print(f"\nMonth: {month}\n")
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
        print(f"        Greenery: {stock['greenery']}\n")
        print(f"        Roses: {stock['roses']}")
        print(f"        Daisy: {stock['daisies']}")
        

        # Restock greenhouse (vendor choice is handled inside)
        restock_greenhouse(shop)

        print(f"    End of month Cash Balance: £{shop.cash_balance:.2f}\n")

        if shop.bankrupt():
            break

    print("\n***********************************************************************")
    if shop.bankrupt():
        print("\nUnfortunately, the shop has gone bankrupt. The simulation has ended.")
    else:
        print("\nCongratulations! You have completed the simulation!")
    print("***********************************************************************\n")


if __name__ == "__main__":
    main()