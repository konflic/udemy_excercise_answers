class Account:
    __count = 0

    def __init__(self, owner):
        self.__owner = owner
        self.__active = True
        self.__balance = 0
        self.__id = str(self.__up_counter()).zfill(6)
    
    @property
    def aid(self):
        return self.__id

    @aid.setter
    def aid(self, _id):
        return False

    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, owner):
        return False

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, balance):
        return False
    
    @classmethod
    def __up_counter(cls):
        cls.__count += 1
        return cls.__count

    def deposit(self, amount):
        if self.__active:
            self.__balance += amount
            return f"Balance: {self.balance}" 
        else:
            return "Can't deposit deactivated account"

    def withdraw(self, amount):
        if self.__active:
            if amount > self.__balance:
                return f"Not enough balance"
            else:
                self.__balance -= amount
                return f"Balance: {self.balance}"
        else:
            return "Can't withdraw from deactivated account"
    
    def close(self):
        if self.__active:
            if self.balance > 0:
                return "Can't close not empty account"
            else:
                self.__active = False
                return f"Account '{self.aid}' closed"
        else:
            return "Account already closed"
