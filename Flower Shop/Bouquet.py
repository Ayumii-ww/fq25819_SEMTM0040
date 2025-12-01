#Vichaya Tedumrongvanich (fq25819, SEMT0040 Summative Assesment)
#Boquet.py: Bouquet class for managing bouquet details including: sellingp price, recipe, time preparation, demand.

class Bouquet:
    """
    Class Representing a bouquet in flower shop.
    
    Methods:

        __str__():
            String representation of the bouquet.
    """

    def __init__ (self, name, greenery , roses,
                  daisies, time_preps, selling_price, monthly_demand):
        """
        Initialize a Bouquet instance.

        Parameters:
            name (str): Name of the bouquet.
            greenery (int): Amount of greenery in the bouquet.
            roses (int): Amount of roses in the bouquet.
            daisies (int): Amount of daisies in the bouquet.
            time_preps (int): Time in minutes to prepare.
            selling_price (float): Selling price per bouquet.
            monthly_demand (int): Monthly demand for the bouquet.
        """
        self.name = name
        self.greenery = greenery
        self.roses = roses
        self.daisies = daisies
        self.time_preps = time_preps
        self.selling_price = selling_price
        self.monthly_demand = monthly_demand
    
    def __str__(self):
        return f"{self.name} (£{self.selling_price:.2f})"