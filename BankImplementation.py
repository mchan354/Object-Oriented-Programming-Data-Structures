''' Class: Bank_People
 The default and utmost parent class for all bankgoers.
 This includes Customers, Employees, and Managers.
'''

class Bank_People:
    def __init__(self,name,bank_name, address,email,number):
        self.name=name
        self.address=address
        self.email=email
        self.number =number
        self.bank_name = bank_name

    def getDescription(self):
        # Ensures that getDescription() varies among each subclass as they all hold different information
        raise NotImplementedError("All subclasses of Bank_People must implement getDescription()!")

###########################

''' Class: ATM
 Serves as a different avenue for customers to withdraw and deposit money from.
 If a customer's bank does not match the ATM's affiliate bank, a fee will be posted along with the deposit/withdrawal.
'''

class ATM():
    def __init__(self,location,bank_name,fee, cash):
        self.location = location
        self.bank_name = bank_name
        self.fee = fee
        self.cash = cash

    def getDescription(self):
        print("{0} ATM\nLocation: {1} | Outsider Fee: ${2:.2f}".format(self.bank_name,self.location,self.fee))

###########################

''' Class: Employee
 The default employee of a bank. Synonymous to a bank teller.
 Contains the total count of employees and a dictionary containing all of the employee objects under their names.
 A global reference is created at the start of the test code to this dictionary for easier access outside of this class.
'''

class Employee(Bank_People):

    emp_count = 0
    employees = {}
    # standardShift stores a default shift for initialization. These times are 9 AM - 5 PM for everyday of the week.
    standardShift = {"Monday": (900, 1700),
                     "Tuesday": (900, 1700),
                     "Wednesday": (900, 1700),
                     "Thursday": (900, 1700),
                     "Friday": (900, 1700),
                     "Saturday": (900, 1700),
                     "Sunday": (900, 1700)}

    def __init__(self, name, bank_name, address, email, number, shifts = standardShift):
        Bank_People.__init__(self,name,bank_name,address,email,number)
        self.shifts = shifts    # Shifts stored per weekday in military time
        Employee.emp_count += 1
        Employee.employees[name] = self     # Adds instance to dictionary of employees for later access

    def checkShifts(self, other):
        # Returns another employee's shifts if both employees work at the same bank.
        if(isinstance(other,Employee) and other.bank_name == self.bank_name):
            return other.shifts
        else:
            print("That person doesn't work here! You can't check their shifts.")

    def __del__(self):
        # Used for when this employee is fired, decrements the employee count in addition to being removed from the
        # Employee.employees dictionary.
        Employee.emp_count -= 1

    def isWorking(self, day, time):
        # Used to check if this employee is working at a certain time on a certain day.
        """
        :param day: Name of the Weekday (Wednesday)
        :param time: Time in Military Time (1300)
        :return: True if that time is contained in the specified day's tuple
        """
        return (time >= self.shifts[day][0] and time < self.shifts[day][1])

    def swapShift(self, other, day):
        # Swaps a specific day's shift with another employee given that they both work at the same bank.

        if(isinstance(other, Employee) and other.bank_name == self.bank_name):
            temp = self.shifts[day]
            self.shifts[day] = other.shifts[day]
            other.shifts[day] = temp
        else:
            print("You can't swap your shifts with that person! They don't work at the same bank as you.")

    def __str__(self):
        return ("{} Employee\n{} | {} | {}".format(self.bank_name, self.name, self.email, self.address))

    def getDescription(self):
        print( "{} Employee\n{} | {} | {}".format(self.bank_name, self.name,self.email, self.address))

    @classmethod
    def find(cls, name):
        #Returns an employee object given their name if they exist in the employees dictionary
        if name not in Employee.employees:
            return False
        return Employee.employees[name]

    @classmethod
    def count(cls):
        #Returns total count of current employees
        return Employee.emp_count

class Manager(Employee):
    def __init__(self, name, bank_name, address, email, number, access_code,shifts=Employee.standardShift):
        Employee.__init__(self,name,bank_name,address,email,number,shifts)
        #Access Code used to differentiate between different managerial levels
        self.__access_code = access_code

    def alterShift(self,other,day,times):
        #Alters shift of an employee on a given day.
        '''
        :param other: An employee that works at the same bank as this manager
        :param day: The day being altered
        :param times: The new start and end times as a tuple. | Example: (900, 1700) = 9 AM to 5 PM
        '''
        if(isinstance(other, Employee) and other.bank_name == self.bank_name):
            other.shifts[day] = times
        else:
            print("You can't alter the shift of someone that doesn't work here!")


    def getCustomerInfo(self,other,detailed=False):
        # Retrieves information of a specific customer. If param detailed is True, the pin of the customer will also be
        # retrieved if the access code of this manager is high enough.
        if(isinstance(other, Customer)):
            if not detailed:
                return "{} - {} - ${}".format(other.name,other.address,other.checkBalance())
            else:
                if(other.getPin(access_code=self.__access_code)):
                    return "{} - {} - ${} - PIN:{}".format(other.name, other.address, other.checkBalance(), other.getPin(self.__access_code))
        else:
            print("That's not a customer!")

    def fireEmployee(self, other):
        # Attempts to fire another employee.
        # The employee being fired must work at the same bank as this manager.
        # If the other employee is also a manager, access codes will be compared to determine if this manager
        # Has the ability to fire the other.
        if(isinstance(other, Employee) and other.bank_name == self.bank_name):
            if(isinstance(other, Manager)):
                if(self.__access_code > other.__access_code):
                    print("Manager {} has been fired. They will not be missed.".format(other.name))
                    del Employee.employees[other.name]
                else:
                    print("You can't fire a manager with higher access than you!")
            else:
                print("{} has been fired. They will not be missed.".format(other.name))
                del Employee.employees[other.name]
        else:
            print("You can't fire someone who doesn't work for this bank!")

    def __str__(self):
        return "{} Manager\n{} | {} | {}\nAccess Code: {}".format(self.bank_name, self.name, self.email, self.address, self.__access_code)

    def getDescription(self):
        print("{} Manager\n{} | {} | {}\nAccess Code: {}".format(self.bank_name, self.name,self.email, self.address,self.__access_code))


class Customer(Bank_People):
    cnt = 0
    cust = {}

    def __init__(self,name, bank_name, address, email, balance, pin, number):
        Bank_People.__init__(self,name,bank_name,address,email,number)
        self.__balance = balance
        self.__pin = pin
        Customer.cnt+=1
        Customer.cust[name] = self

    def deposit(self,money, pin, source):
        # Allows a customer to deposit money. If depositing at an ATM, fees may incur if the ATM does not belong to
        # This customer's bank.

        '''
        :param money: How much money is being deposited as either an integer or float.
        :param pin: This customer's pin number.
        :param source: Where the money is being deposited. Accepts either an employee or an ATM.
        :return: The new balance,
        '''
        if(pin==self.__pin):
            fee = 0
            if (isinstance(source, ATM)):
                if (source.bank_name != self.bank_name):
                    fee += source.fee
                    if (fee > money):
                        print("Insufficient funds! Fee of ${} is greater than deposit amount!".format(source.fee))
                        return self.__balance
                source.cash += fee + money

            self.__balance += money - fee
            return self.__balance
        else:
            print("Incorrect pin!")
            return self.__balance

    def getPin(self, access_code=""):
        # Attempts to get this customer's pin. This can only be done if an access code is supplied whose 'value' is
        # greater than 'B'. This function should only be used directly by a manager.

        if(access_code >= 'B'):
            return self.__pin
        else:
            print("Access Code Not Sufficient for this Operation. This incident will be logged.")
            return False

    def changePin(self, oldPin, newPin):
        # Allows a customer to change their own pin if they can provide their old pin correctly.
        if(oldPin == self.__pin):
            self.__pin = newPin
        else:
            print("Incorrect old pin! Please try again.")

    def withdraw(self, money, pin, source):
        # Allows a customer to withdraw money. If withdrawing from an ATM, fees may incur if the ATM does not belong to
        # This customer's bank. In addition, customers do not have the ability to withdraw money directly from
        # outsider banks. A customer can, however, use another bank's ATM (with a fee).

        '''
        :param money: How much money is being deposited as either an integer or float.
        :param pin: This customer's pin number.
        :param source: Where the money is being deposited. Accepts either an employee or an ATM.
        :return: The new balance,
        '''

        if(pin==self.__pin):
            fee = 0
            if (isinstance(source, ATM)):
                if (source.bank_name != self.bank_name):
                    fee += source.fee
                    if (fee + money > self.__balance):
                        print("Insufficient funds in your account!")
                        return self.__balance
                    elif (fee + money > source.cash):
                        print("We're sorry, this ATM does not possess sufficient funds for this transaction.")
                        return self.__balance
                source.cash -= (fee + money)
                self.__balance -= (money + fee)
                return self.__balance

            if (isinstance(source, Employee)):
                if (source.bank_name != self.bank_name):
                    print(
                        "Sorry! If you're going to withdraw money from your account, you either need to do it with an employee"
                        "at your bank or at an ATM.")
                    return self.__balance
                else:
                    if (self.__balance >= money):
                        self.__balance -= money
                        return self.__balance
        else:
            print("Incorrect pin!")

    def checkBalance(self):
        return self.__balance

    def find_customer(self, name):
        # Returns a customer object given a name
        return Customer.cust[name]

    @classmethod
    def count(self):
        return Customer.cnt

    def __str__(self):
        return ( "{0} Customer\n{1} | {2} | {3} \nBalance: ${4:.2f}".format(self.bank_name, self.name,self.email, self.address,self.__balance))

    def getDescription(self):
        print( "{0} Customer\n{1} | {2} | {3} \nBalance: ${4:.2f}".format(self.bank_name, self.name,self.email, self.address,self.__balance))




########=========================== T E S T ------ C O D E =========================== ########
Customer("Henry Hunt", "BOFA", "123 America Road", "usa.today@gmail.com", 1776.00, 1234, 1234561776)
Customer("Samantha Sung", "Citibank", "1243 Alola Lane", "sammy.sung@gmail.com", 532, 8675, 3091203912)

Employee("Danny Phantom", "BOFA", "109 NonyaBusiness Lane", "d.phantom@yahoo.com", 2154523049)
Employee("Johnny Test", "Citibank", "281 College Ave", "dogsarebetterthancats@gmail.com", 2159392412)

Manager("Maria Cooke", "BOFA", "4545 FourFiveFour Street", "mariacooke@hotmail.com", 2153949394, "Z")
Manager("Awful Boss", "BOFA", "12 Cardboard Box", "awful.boss@google.com", 939493432, "A")
Manager("Connie Woode", "Citibank", "8675 Jenny's House", "co.woode@gmail.com", 5553255535, "D")

atm1 = ATM("123 Aldwyn Lane", "BOFA", "5", 10000)
atm2 = ATM("456 Redifer Road", "Citibank", 5, 13990)

emp = Employee.employees
cust = Customer.cust
