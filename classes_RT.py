class food_RT:
    def __init__(self,name,amount):
        self.__name = name
        self.__amount = amount
    
    def get_name_RT(self):
        return self.__name
    
    def get_amount_RT(self):
        return self.__amount
    
    def get_ppp_RT(self):
        return self.price_dictionary_RT.get(self.__name)

    price_dictionary_RT = {
            "Dry Cured Iberian Ham" : 177.80,
            "Wagyu Steaks" : 450.00,
            "Matsutake Mushrooms" : 272.00,
            "Kopi Luwak Coffee" : 306.50,
            "Moose Cheese" : 487.20,
            "White Truffles" : 3600.00,
            "Blue Fin Tuna" : 3603.00,
            "Le Bonnotte Potatoes" : 270.81
        }
    
    def calculate_price_RT(self):
        return self.get_ppp_RT() * self.__amount