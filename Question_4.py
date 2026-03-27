from Question_1 import *
from Question_3 import *
# 4a)

class OrderException(Exception):
    pass

# 4b)
class Config:
    _MAX_PIZZA = 12

class Order:
    NEXT_ORDER_ID = 1
    def __init__(self, customer: Customer, pizza: Pizza, qty: int):
        #input handling
        if type(qty) is not int:
            raise TypeError('Please use a valid quantity.')
        if qty <= 0:
            raise ValueError("Quantity must be positive!")
        if not isinstance(customer, Customer):
            raise TypeError('customer must be a Customer object.')
        if not isinstance(pizza, Pizza):
            raise TypeError('pizza must be a Pizza object.')
        
        self.__orderID = Order.NEXT_ORDER_ID
        Order.NEXT_ORDER_ID += 1
        self.__customer = customer
        self.__items = [[pizza, qty]] #to make nested list
        self.__status = "Preparing for delivery"

    @property
    def status(self) -> str: #status updates
        return self.__status
    
    @property
    def totalPrice(self) -> float:
        total_cost = 0
        for item in self.__items:
            total_cost += item[0].price * item[1]
        return total_cost

    @property
    def pizzaCount(self) -> int:
        qty = 0
        for item in self.__items:
            qty += item[1]
        return qty

    @status.setter
    def status(self, newStatus: str):
        if len(newStatus) <= 0:
            raise ValueError("Please enter a valid status.")
        self.__status = newStatus

    def addPizza(self, name: str, size: str, price: float, qty: int): #adding pizzas to an order
        #input handling
        if type(qty) is not int:
            raise TypeError('Please use a valid quantity.')
        if qty <= 0:
            raise ValueError('Quantity must be positive!')
        if len(name) < 0:
            raise ValueError("Please use a valid name!")
        if size.upper() not in ('S', 'M', 'L'):
            raise ValueError("Please use a valid size!")
        
        if qty + self.pizzaCount > Config._MAX_PIZZA:
            raise OrderException(f"Too many pizzas! Please order a maximum of {Config._MAX_PIZZA}")
        size = size.upper() #ensure all sizes are equal & names for pizzas
        name = name.title()

        for item in self.__items:
            if name == item[0].name and size == item[0].size:
                item[1] += qty
                return
        pizza = Pizza(name, size, price)
        self.__items.append([pizza, qty])

    def __str__(self):
        message = f"Order ID: {self.__orderID}\nStatus: {self.status}\n\n\
{str(self.__customer)}\n\n"
        for item in self.__items: #to add each items' details
            message += f"{item[0].name} - {item[0].size} - ${item[0].price:.2f} x {item[1]}\n"
        message += f"Total price: ${self.totalPrice:.2f}"
        return message
    
# 4c)

from datetime import datetime

class DeliveryRound:
    def __init__(self, roundName: str, deliveryPartner: DeliveryPartner):
        #input handling
        if type(roundName) is not str:
            raise TypeError('Please use a valid round name.')
        if len(roundName) <= 0:
            raise ValueError('Please use a valid round name.')
        if not isinstance(deliveryPartner, DeliveryPartner):
            raise TypeError('deliveryPartner must be a DeliveryPartner object.')

        self.__roundName = roundName
        self.__deliveryPartner = deliveryPartner
        self.__deliveryDateTime = datetime.now()
        self.__orders = []
    
    @property
    def orders(self):
        return self.__orders
    
    @property
    def deliveryPartner(self):
        return self.__deliveryPartner
    
    def addOrder(self, newOrder: Order): #add new order to current round
        if not isinstance(newOrder, Order):
            raise TypeError('newOrder must be a Order object.')
        
        count = 0 #counter for number of pizzas
        for order in self.orders:
            count += order.pizzaCount
        #ensures total no. of pizzas in one order never goes past the set max (12 in this case)
        if newOrder.pizzaCount + count > Config._MAX_PIZZA:
            raise OrderException(f"Too many pizzas! Please order a maximum of {Config._MAX_PIZZA}")
        self.__orders.append(newOrder)
        
    def __str__(self):
        count = 0 #same as above, counter for no. of pizzas
        for order in self.orders:
            count += order.pizzaCount
        message = f"Delivery Partner Call-Sign: {self.deliveryPartner.callSign}\n{self.__roundName}\n\
Start Time: {self.__deliveryDateTime}\n\n{len(self.orders)} Order(s): {count} pizzas total\n"
        for order in self.orders:
            message += "=" * 20 + "\n" + str(order) + "\n" #formatting
        return message


# 4d)
if __name__ == "__main__":
    print("All of the pairs listed use object composition.\n\n\
Object composition refers to a has-a relationship between classes, meaning that one object is stored as an attribute inside another object.\n\
Inheritance refers to a is-a relationship, meaning that subclasses inherit all instance variables and methods of the superclass.\n\n\
Firstly, DeliveryRound has an Order object stored as an attribute. Hence, they have object composition.\n\n\
Secondly, DeliveryRound has a DeliveryPartner object stored as an attribute, which is the superclass of a FullTimeDeliveryPartner.\Therefore, a FullTimeDeliveryPartner object can be passed to DeliveryRound, showing object composition.\n\n\
Finally, Order object has a Pizza object stored as an attribute. Thus, Order and Pizza exhibit object composition.\nAs stated above, DeliveryRound has an Order object stored as an attribute. As a result, DeliveryRound and Pizza shows object composition.")