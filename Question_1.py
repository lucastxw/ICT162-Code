#1a)
class Customer:
    def __init__(self, name: str, address: str, contactNumber: int):
        
        #input handling
        if type(contactNumber) == float:
            raise TypeError("Please use a valid phone number!")
        if not type(name) == str:
            raise TypeError("Please use a valid name!")
        if not type(address) == str:
            raise TypeError("Please use a valid address!")

        if len(str(contactNumber)) != 8 or str(contactNumber)[0] not in ('9', '8', '6'): # for sg numbers
            raise ValueError("Please use a valid phone number!")
        if len(name) == 0:
            raise ValueError("Please use a valid name!")
        if len(address) == 0:
            raise ValueError("Please use a valid address!")
        self.__name = name.title()
        self.__address = address.title()
        self.__contactNumber = contactNumber
    
    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address
    
    @property
    def contactNumber(self):
        return self.__contactNumber

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\n\
Contact No: {str(self.contactNumber)[:4]} {str(self.contactNumber)[4:]}"
    
#1b)
class Pizza:
    def __init__(self, name: str, size: str, price: float):
        #input handling
        if not type(name) == str:
            raise TypeError("Please use a valid name!")
        if size.upper() not in ('S', 'M', 'L'):
            raise ValueError("Please use a valid size!")
        if len(name) == 0:
            raise ValueError("Please use a valid name!")
        if type(price) not in (float, int):
            raise TypeError("Please use a valid price")
        if price <= 0:
            raise ValueError("Please use a valid price!")
        
        #to standardize name / size
        self.__name = name.title()
        self.__size = size.upper()

        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size
    
    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"Name: {self.name}\nSize: {self.size}\nPrice: ${self.price:.2f}"
    


if __name__ == "__main__":
    print('='*20 + "\nCustomer Object Creation: 3 Customers, 4 Errors\n" + '='*20)
    c1 = Customer("Lah Rence Won", 'le It\'s anar, Orchard Road', '8888.888')
    c2 = Customer("Famous Yee", "27 Napier Rd, Singapore", 66667777)
    c3 = Customer("Sab. Capentry", "Woodlands foRest", 98765432)

    print(f"{c1}\n{'='*20}\n{c2}\n{'='*20}\n{c3}\n{'='*20}")

    #Error Testing
    print('='*20)
    try: #incorrect number
        c4 = Customer("Error", "IDE", 00000000)
    except Exception as e:
        print(f"Error 1 caught successfully in Customer creation! {e}")
    
    try: #incorrect name
        c4 = Customer("", "Error", 88888888)
    except Exception as e:
        print(f"Error 2 caught successfully in Customer creation! {e}")

    try: #incorrect address
        c4 = Customer("Error", "", 88888888)
    except Exception as e:
        print(f"Error 3 caught successfully in Customer creation! {e}")

    try: #incorrect number
        c4 = Customer("Error", "IDE", 8888.888)
    except Exception as e:
        print(f"Error 4 caught successfully in Customer creation! {e}")

    print('='*20)


    print('='*20 + "\nPizza Object Creation: 3 Pizzas, 5 Errors\n" + '='*20)
    p1 = Pizza('pepperoni', 'l', 10.67)
    p2 = Pizza('cheesey delight', 'M', 16)
    p3 = Pizza('dirty veggies', 'S', 20)

    print(f"{p1}\n{'='*20}\n{p2}\n{'='*20}\n{p3}\n{'='*20}")


    #Error Testing
    print('='*20)
    try: #incorrect name
        p4 = Pizza('', 'l', 10.67)
    except Exception as e:
        print(f"Error 1 caught successfully in Pizza creation! {e}")
    
    try: #incorrect size
        p4 = Pizza('Pizza', '', 10.67)
    except Exception as e:
        print(f"Error 2 caught successfully in Pizza creation! {e}")

    try: #incorrect size
        p4 = Pizza('Pizza', '5', 10.67)
    except Exception as e:
        print(f"Error 3 caught successfully in Pizza creation! {e}")

    try: #incorrect price
        p4 = Pizza('Pizza', 'S', 0)
    except Exception as e:
        print(f"Error 4 caught successfully in pizza creation! {e}")

    try: #incorrect price
        p4 = Pizza('Pizza', 'l', 'Zero')
    except Exception as e:
        print(f"Error 5 caught successfully in Pizza creation! {e}")

    print('='*20)

    