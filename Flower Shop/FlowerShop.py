#Vichaya Tedumrongvanich (fq25819, SEMT0040 Summative Assesment)
#Shop.py: Shop class for managing shop details including: florists, bouquets, greenhouse as a core for simulation.

from Florist import Florist
from Bouquet import Bouquet
from Greenhouse import Greenhouse


class FlowerShop: 
    """
    Class Representing a flower shop.
    
    For: 
    - Cash Balance
    - Florists name and speciality
    - Greenhouse stock
    - Bouquet types and recipes prices
    """

    MONTHLY_RENT = 800.00 # Monthly rent cost for the shop (Fixed cost)

    def __init__ (self, cash_initial = 7500.00):
        """
        Initialize a Shop instance with:
        - starting cash
        - florist name (which is empty but at least 1 is hired)
        - greenhouse with full stock
        - bouquet types 

        Parameters:
            cash_initial (float, optional): Initial cash balance of the shop. Defaults to 7500.00.
        """
        self.cash_balance = cash_initial
        self.florists = []
        self.greenhouse = Greenhouse()

        self.bouquets = {} #Bonquet objected stored in dictionary

        self.bouquets["Fern-tastic"] = Bouquet(
            name = "Fern-tastic",
            greenery = 4,
            roses = 0,
            daisies = 2,
            time_preps = 20,
            selling_price = 18.50,
            monthly_demand = 175
        )

        self.bouquets["Be-Leaf in Yourself"] = Bouquet(
            name = "Be-Leaf in Yourself",
            greenery = 2, 
            roses = 1,
            daisies = 3,
            time_preps = 30,
            selling_price = 17.75,
            monthly_demand = 100
        )

        self.bouquets['You Rose to the Occasion'] = Bouquet(
            name = "You Rose to the Occasion",
            greenery = 2,
            roses = 4,
            daisies = 2,
            time_preps = 45,
            selling_price = 32.50,
            monthly_demand = 250
        )

    #Florist managment functions
    def add_florist(self, name, speciality = None):
        """
        Add a new florist if:
        - no more than 4 (maximum)
        - not duplicate

        Parameters:
            name (str): Name of the florist.
            speciality (str, optional): Speciality bouquet type. Defaults to None.
        """
        if len(self.florists) >= 4:
            raise ValueError("You already have 4 florists. Cannot add more.")
        
        if any(f.name == name for f in self.florists):
            raise ValueError(f"A florist with the name '{name}' already exists.")
        
        new_florist = Florist(name=name, speciality=speciality)
        self.florists.append(new_florist)
        print(f"Florist '{name}' is now hired.")

    def remove_florist(self, name):
        """
        Remove a florist by name:
        - at least 1 florist remains

        Parameters:
            name (str): Name of the florist to remove.
        """
        if len(self.florists) <= 1:
            raise ValueError("At least one florist must remain in the shop.")
        
        for florist in self.florists:
            if florist.name == name:
                self.florists.remove(florist)
                print(f"Florist '{name}' has been fired.")
                return
        
        raise ValueError(f"No florist found with the name '{name}'.")
    
    def total_labor_time(self):
        """
        Calculate the total monthly labor time in minutes for all florists.

        Returns:
            int: Total monthly labor time in minutes.
        """
        total_minutes = sum(florist.monthly_minutes() for florist in self.florists)
        return total_minutes
    
    ## Function check labor and order
    def check_labor(self, production_plan):
        """
        Check if order can be fulfilled with current labor capacity.
        """
        total_required_minutes = 0
        
        # Loop through each bouquet in the production plan
        for bouquet_name, quantity in production_plan.items():
            if bouquet_name not in self.bouquets:
                raise ValueError(f"Bouquet '{bouquet_name}' not found in shop.")
            
            bouquet = self.bouquets[bouquet_name]
            total_required_minutes += bouquet.time_preps * quantity
            
            avaliable = self.total_labor_time()
            if total_required_minutes > avaliable:
                return False
            return True
        
    ## Function pay labor
    def florists_pay(self):
        """
        Calculate the total monthly salary for all florists.

        Returns:
            float: Total monthly salary for all florists.
        """
        total_salary = sum(florist.monthly_salary() for florist in self.florists)
        self.cash_balance -= total_salary
        return total_salary
    
    ## Function pay rent
    def rent_pay(self):
        """
        Pay the monthly rent for the shop.

        Returns:
            float: Monthly rent paid.
        """
        self.cash_balance -= FlowerShop.MONTHLY_RENT
        return FlowerShop.MONTHLY_RENT
    
    ## Function pay greenhouse cost
    def greenhouse_costs(self):
        """
        Calculate and pay the monthly cost of the greenhouse.

        Returns:
            float: Monthly cost of the greenhouse.
        """
        cost = self.greenhouse.monthly_cost_greenhouse()
        self.cash_balance -= cost
        return cost
    
    ## Supply needed for demand
    def supply_needed(self, production_plan):
        """
        Calculate the total supplies needed for the production plan.

        Parameters:
            production_plan (dict): Dictionary with bouquet names as keys and quantities as values.
        """
        total_greenery = 0
        total_roses = 0
        total_daisies = 0

        for bouquet_name, quantity in production_plan.items():
            if bouquet_name not in self.bouquets:
                raise ValueError(f"Bouquet '{bouquet_name}' not found in shop.")
            
            bouquet = self.bouquets[bouquet_name]
            total_greenery += bouquet.greenery * quantity
            total_roses += bouquet.roses * quantity
            total_daisies += bouquet.daisies * quantity
        
        return total_greenery, total_roses, total_daisies
    
    ## Check supply
    def check_supply(self, production_plan):
        """
        Check if the greenhouse has enough supplies for the production plan.

        Parameters:
            production_plan (dict): Dictionary with bouquet names as keys and quantities as values.
        """
        needed_greenry, needed_roses, needed_daisies = self.supply_needed(production_plan)
        return self.greenhouse.least_supplies(needed_greenry, needed_roses, needed_daisies)
    
    ## Income and profit calculation
    def produce_bouquets(self, production_plan):
        """
        Produce bouquets according to the production plan and update cash balance.

        Parameters:
            production_plan (dict): Dictionary with bouquet names as keys and quantities as values.
        """
        total_income = 0.0

        for bouquet_name, quantity in production_plan.items():
            if bouquet_name not in self.bouquets:
                raise ValueError(f"Bouquet '{bouquet_name}' not found in shop.")
            
            bouquet = self.bouquets[bouquet_name]
            total_income += bouquet.selling_price * quantity
            
            # Consume supplies from greenhouse
            self.greenhouse.consume_supplies(
                used_greenery = bouquet.greenery * quantity,
                used_roses = bouquet.roses * quantity,
                used_daisies = bouquet.daisies * quantity
            )
        
        self.cash_balance += total_income
        return total_income
    
    ## End month process 
    def end_month_process(self, production_plan):
        """
        Process end-of-month operations including:
        - Paying rent
        - Paying florists
        - Paying greenhouse costs
        - Producing bouquets based on production plan
        - Depreciating greenhouse stock

        Parameters:
            production_plan (dict): Dictionary with bouquet names as keys and quantities as values.

        Returns:
            dict: Summary of end-of-month financials.
        """
        rent = self.rent_pay()
        labor_cost = self.florists_pay()
        greenhouse_cost = self.greenhouse_costs()
        income = self.produce_bouquets(production_plan)
        self.greenhouse.depreciation()



        summary = {
            "Rent Paid": rent,
            "Labor Cost": labor_cost,
            "Greenhouse Cost": greenhouse_cost,
            "Income from Bouquets": income,
            "Ending Cash Balance": self.cash_balance
        }

        return summary
    
    ## Restock 
    def restock(self):
        """
        Restock the greenhouse to maximum capacity.
        """
        cost = self.greenhouse.restock(
            greenery_price = Greenhouse.COST_GREENERY,
            roses_price = Greenhouse.COST_ROSES,
            daisies_price = Greenhouse.COST_DAISIES
        )
        self.cash_balance -= cost
        return cost
    
    def choose_vendor_for_supply(self, supply_name):
        """
        Choose a vendor for purchasing supplies.

        Parameters:
            supply_name (str): Name of the supply ("roses", "daisies", or "greenery").

        Returns:
            float: Price per unit from the chosen vendor.
        """

        EVERGREEN_ESSENTIALS = {
            "greenery": 0.95,
            "roses": 2.80,
            "daisies": 1.50,
            
        }

        FLORAGROW_DISTRIBUTORS = {
            "greenery": 1.80,
            "roses": 1.60,
            "daisies": 1.20,
            
        }

        while True:
            print(
                f"Do you want to purchase {supply_name} from Evergreen Essentials (0), "
                f"or FloraGrow Distributors (1)?"
            )
            print("Press (i) if you would like to see price information from either supplier.")
            choice = input("Input: ").strip().lower()

            if choice == "i":
                if supply_name == "roses":
                    print(f"  Evergreen: £{EVERGREEN_ESSENTIALS['roses']:.2f} / bunch")
                    print(f"  FloraGrow: £{FLORAGROW_DISTRIBUTORS['roses']:.2f} / bunch")
                elif supply_name == "daisies":
                    print(f"  Evergreen: £{EVERGREEN_ESSENTIALS['daisies']:.2f} / bunch")
                    print(f"  FloraGrow: £{FLORAGROW_DISTRIBUTORS['daisies']:.2f} / bunch")
                elif supply_name == "greenery":
                    print(f"  Evergreen: £{EVERGREEN_ESSENTIALS['greenery']:.2f} / bunch")
                    print(f"  FloraGrow: £{FLORAGROW_DISTRIBUTORS['greenery']:.2f} / bunch")
                print()
                continue

            if choice == "0":
                # Evergreen
                if supply_name == "roses":
                    return EVERGREEN_ESSENTIALS["roses"]
                elif supply_name == "daisies":
                    return EVERGREEN_ESSENTIALS["daisies"]
                elif supply_name == "greenery":
                    return EVERGREEN_ESSENTIALS["greenery"]

            elif choice == "1":
                # FloraGrow
                if supply_name == "roses":
                    return FLORAGROW_DISTRIBUTORS["roses"]
                elif supply_name == "daisies":
                    return FLORAGROW_DISTRIBUTORS["daisies"]
                elif supply_name == "greenery":
                    return FLORAGROW_DISTRIBUTORS["greenery"]

            print("Invalid input. Please enter 0, 1, or i.\n")
    
    ## Bankrupt or not 
    def bankrupt(self):
        """
        Check if the shop is bankrupt.

        Returns:
            bool: True if bankrupt, False otherwise.
        """
        return self.cash_balance < 0