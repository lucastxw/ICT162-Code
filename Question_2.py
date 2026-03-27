from Question_1 import Customer, Pizza

# 2a)
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
            raise TypeError('customer must be a Customer object.')

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
        if type(qty) is not int:
            raise TypeError('Please use a valid quantity.')
        if qty <= 0:
            raise ValueError('Quantity must be positive!')
        if len(name) < 0:
            raise ValueError("Please use a valid name!")
        if size.upper() not in ('S', 'M', 'L'):
            raise ValueError("Please use a valid size!")
        size = size.upper() #ensure all sizes are equal & names for pizzas
        name = name.title()

        for item in self.__items:
            if name == item[0].name and size == item[0].size:
                item[1] += qty
                return
        pizza = Pizza(name, size, price)
        self.__items.append([pizza, qty])

    def __str__(self):
        message = f"Order ID: {self.__orderID}\nStatus: {self.status}\n\n{str(self.__customer)}\n\n"
        for item in self.__items: #to add each items' details
            message += f"{item[0].name} - {item[0].size} - ${item[0].price:.2f} x {item[1]}\n"
        message += f"Total price: ${self.totalPrice:.2f}"
        return message
    
def main():
    # Creation of Order
    o1 = Order(Customer("Herro Tan", "999A, Sentosa Cove", 99123665), Pizza("Hawaiian Plus", "M", 9.59), 1)
    
    # write codes to add the following pizzas in this sequence
    # 1. Name: Super Supreme, Size: L, Price: 12.59, Qty: 3
    o1.addPizza("Super Supreme", "L", 12.59, 3)
    # 2. Name: Hawaiian Plus, Size: M, Price: 9.59, Qty: 3
    o1.addPizza("Hawaiian Plus", "M", 9.59, 3)
    # 3. Name: Chicken Satay, Size: L, Price: 11.59, Qty: 6
    o1.addPizza("Chicken Satay", "L", 11.59, 6)
    #
    # Print order details after these additions
    print(o1)

main()