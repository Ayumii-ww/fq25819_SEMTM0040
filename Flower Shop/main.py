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


    # Hiring
    hire_count = get_input(
        "How many florists would you like to **HIRE** this month? (0 for none): ",
         default=0
    )

    if hire_count > 0:
        for i in range(hire_count):
            if len(shop.florists) >= 4:
                print("You already have the maximum of 4 florists. Cannot hire more.\n")
                break

            while True:
                name = input("Please input florist name: ").strip()
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
                except ValueError as exc:
                    print(exc)
                    print("Please try a different name.\n")

    # Firing
    # Must keep at least 1 florist
    max_fire = max(0, len(shop.florists) - 1)
    if max_fire == 0:
        print("You must employ at least one florist. No one can be removed.\n")
        return

    fire_count = get_input("How many florists would you like to **fire** this month? (0 for none): ", default=0)

    if fire_count > max_fire:
        print(f"You can only fire up to {max_fire} florists this month.")
        fire_count = max_fire

    for _ in range(fire_count):
        while True:
            name = input("Enter the name of the florist to remove: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            try:
                shop.remove_florist(name)
                break
            except ValueError as exc:
                print(exc)
                print("Please enter a valid florist name.\n")


