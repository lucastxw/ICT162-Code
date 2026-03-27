from abc import ABC, abstractmethod

# 3a)
class DeliveryPartner(ABC):
    FEES_PER_ROUND = 32
    def __init__(self, callSign: str, name: str):
        #input handling
        if (type(callSign) or type(name)) is not str:
            raise TypeError("Wrong data type!")
        if len(callSign) == 0:
            raise ValueError("Please use valid callsign.")
        if len(name) == 0:
            raise ValueError("Please use valid name.")
        
        self.__callSign = callSign
        self.__name = name
    
    @property
    def callSign(self):
        return self.__callSign
    
    @property
    def name(self):
        return self.__name
    
    @abstractmethod
    def computePay(self) -> float:
        pass

    def __str__(self):
        return f"Name: {self.name}      CallSign: {self.callSign}"
    

# 3b)

class FullTimeDeliveryPartner(DeliveryPartner):
    def __init__(self, callSign: str, name: str, basicSalary: float):
        #input handling
        if type(basicSalary) is not float:
            raise TypeError("Please input a valid basic salary.")
        if basicSalary < 0:
            raise ValueError("Please input a valid basic salary.")

        #inherit from superclass
        super().__init__(callSign, name)
        self.__basicSalary = basicSalary
        
    def computePay(self, rounds: int) -> float:
        return float(self.__basicSalary + rounds * DeliveryPartner.FEES_PER_ROUND)

class PartTimeDeliveryPartner(DeliveryPartner):
    #initialize class variables
    BONUS_ROUNDS = 30
    BONUS_RATE = 1.85

    def __init__(self, callSign: str, name: str):
        #inherit frm superclass
        super().__init__(callSign, name)
        
    def computePay(self, rounds: int) -> float:
        if type(rounds) is not int:
            raise TypeError("Please use a valid round number.")
        if rounds <= PartTimeDeliveryPartner.BONUS_ROUNDS:
            return float(rounds * DeliveryPartner.FEES_PER_ROUND)
        else:
            return float(PartTimeDeliveryPartner.BONUS_ROUNDS * DeliveryPartner.FEES_PER_ROUND +\
             (rounds - PartTimeDeliveryPartner.BONUS_ROUNDS) * (DeliveryPartner.FEES_PER_ROUND * PartTimeDeliveryPartner.BONUS_RATE))
        

# 3c)
if __name__ == "__main__":
    p1 = PartTimeDeliveryPartner("DP-007", "Lim Lim Kee")
    p2 = FullTimeDeliveryPartner("Maverick", "Tom Yam Kong", 1200.0)
    print(f"{p1}{' '*5}${p1.computePay(50):.2f}\n{p2}{' '*5}${p2.computePay(40):.2f}")