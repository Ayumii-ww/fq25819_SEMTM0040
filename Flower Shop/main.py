from FlowerShop import FlowerShop
def get_input(prompt,default=None):
   """
   Read integer from user but if press enter return default
   """

   while True: 
        raw= input(prompt).strip()
        if raw=="":
            if default is not None:
                return default
            print("Please enter a number.")
            continue
        try:
            value = int(raw)
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("----------------------------------------------------------------")
    print("Welcome to the FlowerShop Simulator!!")
    print("----------------------------------------------------------------\n")

    months = get_input("Enter number of months to simulate (default 6): ", default=6)

    shop = FlowerShop()
    print()

    for month in range(1, months + 1):
        print(f"Month: {months}\n")

        print("Before the month starts,there are some owner actions for you to carry out.\n"
              "First, review the numer of staff,Then decide how many bouquets to sell.\n")
    
        print(f"Current Florists: {len(shop.florists)}")

        add_florist = get_input("How many florists would you like to hire? (0 for none): ")
        for i in range(add_florist):
            name = input(f"Enter name for florist {i + 1}: ").strip()
            if not name:
                print("Florist name cannot be empty. Please try again.")
                continue
            speciality = input(f"Enter speciality for florist {i + 1} (or press Enter for none): ").strip()
            try:
                shop.add_florist(name, speciality if speciality else None)
            except ValueError as e:
                print(" Error:", e)
            
       


print(main())
      