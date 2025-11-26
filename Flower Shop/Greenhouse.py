#Vichaya Tedumrongvanich (fq25819, SEMT0040 Summative Assesment)
#Greenhouse.py: Greenhouse class for managing greenhouse details including: capacity, depreication, monthly cost.

import math

class Greenhouse:
    """
    Class Representing a greenhouse in flower shop.
    
    Methods:
        current_stock():
            Get the current stock of flowers in the greenhouse.    
        monthly_cost_greenhouse():
            Calculate the monthly cost of the greenhouse based on current stock and depreciation.
        depreciation():
            Apply monthly depreciation to the flower stock. 
        least_supplies(needed_greenery, needed_roses, needed_daisies):
            Check if greenhouse has least quantities
        consume_supplies(used_greenery, used_roses, used_daisies):
            Consume supplies from the greenhouse when make bouquet.
        restock(greenery_price, roses_price, daisies_price):
            Restock the greenhouse to maximum capacity.
    """

    MAX_GREENERY =  400  # Maximum greenery capacity of the greenhouse
    MAX_ROSES = 200      # Maximum roses capacity of the greenhouse
    MAX_DAISIES = 250    # Maximum daisies capacity of the greenhouse

    DEPRECI_GREENERY = 0.05  # Depreciation rate for greenery
    DEPRECI_ROSES = 0.40    # Depreciation rate for roses
    DEPRECI_DAISIES = 0.15   # Depreciation rate for daisies

    COST_GREENERY = 0.20   # Cost per bunch of greenery
    COST_ROSES = 1.50     # Cost per bunch of roses
    COST_DAISIES = 0.80    # Cost per bunch of daisies

    def __init__(self, roses=None, daisies=None, greenery=None):
        """
        Initialize a Greenhouse instance.
        If no values are provi

        Parameters:
            roses (int, optional): Initial amount of roses. Defaults to None.
            daisies (int, optional): Initial amount of daisies. Defaults to None.
            greenery (int, optional): Initial amount of greenery. Defaults to None.
        """
        self.grennery = Greenhouse.MAX_GREENERY if greenery is None else greenery
        self.roses = Greenhouse.MAX_ROSES if roses is None else roses
        self.daisies = Greenhouse.MAX_DAISIES if daisies is None else daisies 
    
    def current_stock(self):
        """
        Get the current stock of flowers in the greenhouse.

        Returns:
            dict: Current stock of greenery, roses, and daisies.
        """
        return {
            "greenery": self.grennery,
            "roses": self.roses,
            "daisies": self.daisies
        }
    
    def monthly_cost_greenhouse(self):
        """
        Calculate the monthly cost of the greenhouse based on current stock and depreciation.

        Returns:
            float: Monthly cost of the greenhouse.
        """

        cost_greenery = (self.grennery * Greenhouse.COST_GREENERY)
        cost_roses = (self.roses * Greenhouse.COST_ROSES)
        cost_daisies = (self.daisies * Greenhouse.COST_DAISIES)
        return cost_greenery + cost_roses + cost_daisies
    
    def depreciation(self):
        """
        Apply monthly depreciation to the flower stock.
        Round up to the nearest whole number by using math.ceil.
        """
        
        lost_greenery = math.ceil(self.grennery * Greenhouse.DEPRECI_GREENERY) # math.ceil to round up
        lost_roses = math.ceil(self.roses * Greenhouse.DEPRECI_ROSES)
        lost_daisies = math.ceil(self.daisies * Greenhouse.DEPRECI_DAISIES)

    def least_supplies(self, needed_greenery, needed_roses, needed_daisies):
        """
        Check if greenhouse has least quantities
        """
        return (
            self.grennery >= needed_greenery and
            self.roses >= needed_roses and
            self.daisies >= needed_daisies
        )

    def consume_supplies(self, used_greenery, used_roses, used_daisies):
        """
        Consume supplies from the greenhouse when make bouquet.

        Parameters:
            used_greenery (int): Amount of greenery to consume.
            used_roses (int): Amount of roses to consume.
            used_daisies (int): Amount of daisies to consume.
        """
        if not self.least_supplies(used_greenery, used_roses, used_daisies):
            raise ValueError("Not enough supplies in the greenhouse.")
        self.grennery -= used_greenery
        self.roses -= used_roses
        self.daisies -= used_daisies

    def restock(self, greenery_price, roses_price, daisies_price):
        """
        Restock the greenhouse to maximum capacity.

        Parameters:
            greenery_price (float): Price per bunch of greenery.
            roses_price (float): Price per bunch of roses.
            daisies_price (float): Price per bunch of daisies.

        Returns:
            float: Total cost of restocking.
        """
        needed_greenery = Greenhouse.MAX_GREENERY - self.grennery
        needed_roses = Greenhouse.MAX_ROSES - self.roses
        needed_daisies = Greenhouse.MAX_DAISIES - self.daisies

        total_cost = (
            (needed_greenery * greenery_price) +
            (needed_roses * roses_price) +
            (needed_daisies * daisies_price)
        )

        #Update stock to maximum after restock
        self.grennery = Greenhouse.MAX_GREENERY
        self.roses = Greenhouse.MAX_ROSES
        self.daisies = Greenhouse.MAX_DAISIES

        return total_cost


        