class RentApartment:

    RENTAL_SERVICE_FEE = 100 # eur per month
    STUDIO_SIZE_LIMIT = 32 # m2
    ONE_BEDROOOM_SIZE_LIMIT = 45 # m2
    STUDIO_PRICE_LEVEL = 25 # eur/m2
    ONE_BEDROOOM_PRICE_LEVEL = 20 # eur/m2
    LARGE_PRICE_LEVEL = 18 # eur/m2
    TRANSFER_TAX = 0.02

    def __init__(self, address, rent, maintenance_charge, size, free_of_debt_price):
        self.__address = address
        self.__rent = rent
        self.__maintenance_charge = maintenance_charge
        self.__size = size
        self.__free_of_debt_price = free_of_debt_price
        self.__rental_service = False
        self.__renovation_costs = 0

    def get_address(self):
        return self.__address

    def get_rent(self):
        return self.__rent

    def get_maintenance_charge(self):
        return self.__maintenance_charge

    def get_size(self):
        return self.__size

    def get_price(self):
        return self.__free_of_debt_price

    def get_renovation_costs(self):
        return self.__renovation_costs

    def update_rental_service(self):
        if self.__rental_service == False:
            self.__rental_service = True
        else:
            self.__rental_service = False
        return self.__rental_service

    def increase_rent(self, new_rent):
        if new_rent > self.__rent:
            self.__rent = new_rent
            return True
        else:
            return False

    def add_renovation_costs(self, costs):
        self.__renovation_costs += costs

    def calculate_square_meter_rent(self):
        return self.__rent / self.__size

    def calculate_rental_income(self):
        monthly_rent_income = self.get_rent()
        if self.__rental_service == True:
            monthly_expenses = self.get_maintenance_charge() + RentApartment.RENTAL_SERVICE_FEE
        else:
            monthly_expenses = self.get_maintenance_charge()
        debt_free_price = self.get_price()
        transfer_tax = debt_free_price * RentApartment.TRANSFER_TAX
        renovation_cost = self.get_renovation_costs()
        return (monthly_rent_income - monthly_expenses) * 12 / (debt_free_price + transfer_tax + renovation_cost) * 100

    def compare_rental_incomes(self, other):
        if self.calculate_rental_income() > other.calculate_rental_income():
            return 1
        elif self.calculate_rental_income() < other.calculate_rental_income():
            return -1
        elif self.calculate_rental_income() == other.calculate_rental_income():
            return 0

    def calculate_return_on_equity(self, down_payment, loan_interest):
        monthly_rent_income = self.get_rent()
        if self.__rental_service == True:
            monthly_expenses = self.get_maintenance_charge() + RentApartment.RENTAL_SERVICE_FEE
        else:
            monthly_expenses = self.get_maintenance_charge()
        return (monthly_rent_income - monthly_expenses - loan_interest) * 12 / down_payment * 100

    def check_price_level(self):
        if self.__size < RentApartment.STUDIO_SIZE_LIMIT:
            if self.calculate_square_meter_rent() >= RentApartment.STUDIO_PRICE_LEVEL:
                return True
            else:
                return False
        elif RentApartment.STUDIO_SIZE_LIMIT <= self.__size < RentApartment.ONE_BEDROOOM_SIZE_LIMIT:
            if self.calculate_square_meter_rent() >= RentApartment.ONE_BEDROOOM_PRICE_LEVEL:
                return True
            else:
                return False
        elif self.__size >= RentApartment.ONE_BEDROOOM_SIZE_LIMIT:
            if self.calculate_square_meter_rent() >= RentApartment.LARGE_PRICE_LEVEL:
                return True
            else:
                return False

    def __str__(self):
        if self.__rental_service == True:
            rental_service_status = str("in u, se")
        else:
            rental_service_status = str("not in use")

        string = "Address: " + str(self.get_address()) + "\n" + \
                "Maintenance charge: " + str(self.get_maintenance_charge()) + " eur" + "\n" + \
                "Size: " + str(self.get_size()) + " m2" + "\n" + \
                "Rent: " + str(self.get_rent()) + " eur" + "\n" + \
                "Rental service: " + rental_service_status
        return string
