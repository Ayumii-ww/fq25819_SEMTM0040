# Vichaya Tedumrongvanich (fq25819, SEMT0040 Summative Assesment)
# Florist.py: Florist class for managing florist details and calculating salaries and time estimates.


class Florist:
    """
    CLass Representing a florist in flower shop.

    Methods:
        monthly_salary():
             Calculate the monthly salary of the florist.
        monthly_minutes(): 
             Calculate the total monthly working in minutes of the florist.
        speciality_minutes(bouquet_name, base_minutes): 
            Calculate time taken for a bouquet based on speciality.
        __str__():
            String representation of the florist.
    """

    FIXED_HOURLY_RATE = 15.50
    FIXED_MONTHLY_HOURS = 80

    def __init__(self, name, speciality=None):
        """
        Initialize a Florist instance.
        
        Parameters:
            name (str): Name of the florist.
            speciality (str, optional): Speciality bouquet type. Defaults to None.
        """
        
        if not name:
            raise ValueError("Florist must have a name.")
        
        self.name = name
        self.speciality = speciality if speciality else "General"
        self.hourly_rate = Florist.FIXED_HOURLY_RATE
        self.monthly_hours = Florist.FIXED_MONTHLY_HOURS

    def monthly_salary(self):
        """
        Calculate the monthly salary of the florist.
        
        Returns:
            float: Monthly salary."""
        return self.hourly_rate * self.monthly_hours
    
    def monthly_minutes(self):
        """
        Calculate the total monthly working time in minutes.
        
        Returns:
            int: Total monthly working time in minutes.
    
        """

        return int(self.monthly_hours * 60)
    
    def speciality_minutes(self, bouquet_name, base_minutes):
        """
        Calculate time taken for a bouquet based on speciality.

        Parameters:
            bouquet_name (str): Name of the bouquet.
            base_minutes (int): Base time in minutes for the bouquet.

        Returns:
            int: Time taken in minutes with speciality.
        
        """
        if self.speciality is not None and bouquet_name == self.speciality:
            return int(base_minutes +1) // 2 # Speciality florists take half the time
        return base_minutes
    
    def __str__(self):
        """
        String representation of the florist.

        Returns:
            str: Formatted string with florist details.
        """
        if self.speciality:
            return f"Florist Name: {self.name}, (Speciality: {self.speciality})"
        return self.name
    

                


    
