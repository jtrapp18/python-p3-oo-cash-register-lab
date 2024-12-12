#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = None

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, discount):
    if isinstance(discount, float) or isinstance(discount, int):
      self._discount = discount
    else:
      raise ValueError("discount should be expressed as integer or float")
    
  def add_item(self, item, price, quantity=1):
    self.items += quantity*[item]
    self.last_transaction = quantity*price*self.apply_discount()
    self.total += self.last_transaction

    if self._discount > 0:
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def apply_discount(self):

    if self._discount == 0:
      print("There is no discount to apply.")
      return 1
    else: 
      return (1-self._discount/100)

  def void_last_transaction(self):
    self.items.pop()
    self.total = self.total - self.last_transaction

cash_register = CashRegister()
cash_register.add_item("eggs", 0.98)
print(cash_register._discount)