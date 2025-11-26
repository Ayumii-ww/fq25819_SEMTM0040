from Florist import Florist
from Bouquet import Bouquet
from Greenhouse import Greenhouse
#Vichaya Tedumrongvanich (fq25819, SEMT0040 Summative Assesment)
#Shop.py: Shop class for managing shop details including: florists, bouquets, greenhouse as a core for simulation.

class Shop: 
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
        self.florists = list[Florist] =  []
        self.greenhouse = Greenhouse()

        self.bouquets = dict[str, Bouquet] = {} #Bonquet objected stored in dictionary

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

        Parameters:
            name (str): Name of the florist.
            speciality (str, optional): Speciality bouquet type. Defaults to None.
        """
        if len(self.florists) >= 4:
            raise ValueError("You already have 4 florists. Cannot add more.")
        
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
    ## Function pay labor
    ## Function pay rent
    ## Function pay greenhouse cost
    ## Supply needed for demand
    ## Check supply
    ## Income and profit calculation
    ## End month process 
    ## Restock 
    ## Bankrupt or not 