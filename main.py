import json


class Checkout:
  """
    Represents a checkout process for a store.

    Attributes:
        pricing (dict): A dictionary of items and their prices.
        deals (list): A list of deals.
        basket (list): A list of items in the checkout basket.

    Methods:
        __init__(self, basket: str): Initializes the Checkout object.
        get_total(self) -> int: Calculates the total cost of items in the checkout basket.
  """
    
  # dictionary of items and their prices
  pricing = {
    "A": 50,
    "B": 35,
    "C": 25,
    "D": 12
  }

  # array of deals
  deals = [
    {
      "item": "A", 
      "quantity": 3,
      "price": 140,
    },
    {
      "item": "B", 
      "quantity": 2,
      "price": 60,
    }
  ]
  
  basket = []
  
  def __init__(self, basket: str):
    try:
      self.basket = json.loads(basket)
    except:
      raise TypeError('Invalid JSON')
  
  
  """
    Calculates the total cost of items in the checkout basket.

    This function iterates over each item in the basket, applies any applicable deals,
    and calculates the total cost. It also validates the basket to ensure item codes
    are strings and quantities are integers greater than 0.

    Parameters:
    self (Checkout): The checkout object containing the basket and pricing information.

    Returns:
    int: The total cost of items in the basket.
  """
  def get_total(self):
    total = 0 

    # loops through basket, applies deals and calculates total
    for index, item in enumerate(self.basket):
      
      # validate the basket
      if not isinstance(item['code'], str):
        raise TypeError('Item code must be a string')
      elif not isinstance(item['quantity'], int):
        raise TypeError('Item quantity must be an integer')
      elif item['quantity'] <= 0:
        raise ValueError('Item quantity must be greater than 0')
      
      item_quant = item['quantity']
      
      # loops through deals and applies any that are applicable
      for deal in self.deals:
        if item['code'] == deal['item']:
          deal_multiple = item_quant // deal['quantity']
          cost = deal_multiple * deal['price']
          
          # adds deal price to cost and subtracts the deal quantity from the item quantity
          total += cost
          item_quant -= deal_multiple * deal['quantity']
          
      # remaining basket cost is calculated
      try:
        item_cost = self.pricing[item['code']]
      except:
        raise ValueError('Invalid item code')
      
      item_total = item_quant * item_cost
      total += item_total
      
    return total
  

