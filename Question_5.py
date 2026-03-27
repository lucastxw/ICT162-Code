from Question_1 import *
from Question_3 import *
from Question_4 import *

# 5a

class PizzaHouse:
    def __init__(self):
        self.__deliveryPartners = {}
        self.__deliveryRounds = []

        try:#error handling
            with open('./Appendix_A.txt', 'r') as f: #i hope this is the format needed
                header = f.readline().strip().split(",") #header not needed
                for line in f:
                    name, call_sign, salary, employment = line.strip().split(',')
                    #determining the type of employment (can also check off of the basic salary)
                    if employment == "Full-time":
                        employee = FullTimeDeliveryPartner(call_sign, name, float(salary))
                    else: #part-time
                        employee = PartTimeDeliveryPartner(call_sign, name)
                    #adding the new partner into the dictionary
                    self.__deliveryPartners[call_sign] = {'partner': employee, 'assigned': False, 'rounds': 0}
        except FileNotFoundError:
            raise FileNotFoundError("Appendix A not found!")

    def addOrder(self, customer: Customer, pizza: Pizza, qty: int):
        #creation of new order
        new_order = Order(customer, pizza, qty)
        
        #check if there are existing orders
        if len(self.__deliveryRounds) > 0:
            for i in self.__deliveryRounds:
                try:#ensures that no error is thrown back if >12 orders 
                    i.addOrder(new_order)
                    chosen_deliveryRound = i
                    return #ends after new order has been added to an available round
                
                except OrderException:#continues passing through the loop
                    continue

        chosen_rider = None

        for i in self.__deliveryPartners.values():#for delivery partner obj, has he been assigned yet?
            if i['assigned'] == False:
                chosen_rider = i
                break

        #no other available riders
        if not chosen_rider:
            raise Exception("No riders available!")
        
        #name creationa for delivery round because i don't know
        round_number = len(self.__deliveryRounds) + 1
        chosen_deliveryRound = DeliveryRound(f'Route-{round_number}', chosen_rider['partner'])
        
        #as per the qn, appends new round to the round list, adds order to the new round, then sets the
        #rider status
        self.__deliveryRounds.append(chosen_deliveryRound)
        chosen_deliveryRound.addOrder(new_order)
        chosen_rider['assigned'] = True

    def deliveredRound(self, roundName):#change status of round
        if len(roundName) == 0:
            raise ValueError("Please use a valid round name.")
        for round in self.__deliveryRounds:
            if roundName in str(round):#since the round name IS A PRIVATE VARIABLE???
                for order in round.orders:#checks if all orders are not delivered yet
                    if order.status == "Delivered":
                        raise OrderException("Round has already been delivered!")
                for order in round.orders:#finally changes all the status
                    order.status = "Delivered"

                #resets the status for delivery partner and increases the no. of rounds they completed
                self.__deliveryPartners[round.deliveryPartner.callSign]['assigned'] = False
                self.__deliveryPartners[round.deliveryPartner.callSign]['rounds'] += 1
                return
        raise OrderException("Delivery round not found") #if none of these happens, order exception raised
            

    def listDeliveryRounds(self):
        message = ""
        for round in self.__deliveryRounds: 

    #since some of the needed details are private attributes, im just calling the DeliveryRound class 
            
            message += "="*20 + f"\nDelivery Partner Name: {round.deliveryPartner.name}\n{str(round)}" + "="*20 + "\n"
        return message
    
#5b
def main():
    ph = PizzaHouse()
    
    #creating necessary objects
    #pizzas first
    p1 = Pizza('pepperoni', 'l', 10.67)
    p2 = Pizza('hawaiian', 'l', 12)
    p3 = Pizza('cheesey delight', 'M', 16)
    p4 = Pizza('dirty veggies', 'S', 20)

    #customers
    c1 = Customer("Lah Rence Won", 'le It\'s anar, Orchard Road', 88888888)
    c2 = Customer("Famous Yee", "27 Napier Rd, Singapore", 66667777)
    c3 = Customer("Sab. Capentry", "Woodlands foRest", 98765432)

    # 10 orders
    ph.addOrder(c1, p1, 5) #5 pizzas in r1
    ph.addOrder(c2, p2, 5) # 10 total pizzas in r1
    ph.addOrder(c3, p4, 5) # testing creation of a new round due to complete round
    ph.addOrder(c1, p3, 2) #filling up r1
    ph.addOrder(c2, p1, 7) # r2 filled up
    ph.addOrder(c3, p2, 12) # large order
    ph.addOrder(c1, p3, 1) #small order
    ph.addOrder(c1, p3, 5) # testing if qty just goes up
    ph.addOrder(c1, p3, 6) #same as above
    ph.addOrder(c3, p4, 3) #smallish order

    #show all orders currently
    print(f"{'='*20}\nFirst Output\n{'='*20}")
    print(ph.listDeliveryRounds())

    #simulate actual updates
    #first, completing route 1

    print(f"{'='*20}\nError Testing\n{'='*20}")
    try:
        ph.deliveredRound("Route-1")
    except Exception as e:
        print(f"Error, incorrect output: {e}")

    #fake route
    try:
        ph.deliveredRound("Route-99")
    except Exception as e:
        print(f"Correct Output: {e}")
    
    try:
        ph.deliveredRound("Route-1")
    except Exception as e:
        print(f"Correct Output: {e}")

    print(f"{'='*20}\nFinal Output\n{'='*20}")

    #show status change & round increase
    print(ph.listDeliveryRounds())

if __name__ == "__main__":
    main()