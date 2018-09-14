"""Classes for melon orders."""
from random import randint
from datetime import datetime
import doctest

class TooManyMelonsError(ValueError):
    pass
    

class AbstractMelonOrder():
    """ An abstract base clss that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        if qty > 100:
            raise TooManyMelonsError(f"No more than 100 melons.")
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_time()

    def is_rush_hour(self, order_time):
        """ 
        Returns true if order was made during rush hour (M-F, 8am-11am)

        >>>


        """
        # For testing purposes, create a date here
        #order_time = datetime(2018, 9, 15, 8, 34,)
        #order_time = datetime.now()
        if 8 <= order_time.hour < 11 and 0 <= order_time.weekday() <=4:
            return True
        return False


    def get_base_price(self):
        """ Base_price uses surge pricing (random value betwee $5 and $9 
        plus an extra $4 if 
        """
        base_price = randint(5,9)
        if self.is_rush_hour(datetime.now()):
            base_price += 4
        return base_price

    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()
        if self.species == "christmas melons":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == 'international' and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    order_type = "government"
    passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17
    
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""
        return self.country_code

    # def get_total(self):
    #     total = super().get_total()
    #     if self.qty < 10:
    #         total += 3
    #     return total
