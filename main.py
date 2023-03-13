import csv
from datetime import datetime

with open("Menu.txt", "w") as menu_file:
    menu_file.write("Lütfen Bir Pizza Tabanı Seçiniz:\n"
    "1: Klasik\n"
    "2: Margarita\n"
    "3: TürkPizza\n"
    "4: Sade Pizza\n"
    "Topping Seçiniz:\n"
    "11: Zeytin\n"
    "12: Mantar\n"
    "13: Keçi Peyniri\n"
    "14: Et\n"
    "15: Soğan\n"
    "16: Mısır\n"
    )

class Pizza:
    def __init__(self):
        self.description = "Bir pizza"
        self.cost = 0.0
        
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

    
# -------------------------- SUBCLASSLAR --------------------------------------------
class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik pizza"
        self.cost = 20.0

class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margarita pizza"
        self.cost = 25.0

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Türk pizza"
        self.cost = 30.0

class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Sade pizza"
        self.cost = 15.0



# ---------------------------------- DECORATOR ---------------------------------
class Decorator(Pizza):
    def __init__(self, pizza):
        super().__init__()
        self.component = pizza
    
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)
    

#------------------------------------- TOPPING ----------------------------------------
class Zeytin(Decorator):
    def __init__(self, component):
        self.component = component
        self.price = 1.0
        self.description = "Zeytin"

    def get_cost(self):
        return self.price + self.component.get_cost()

    def get_description(self):
        return self.component.get_description() + ", " + self.description
    
class Mantar(Decorator):
    def __init__(self, component):
        self.component = component
        self.price = 2.0
        self.description = "Mantar"

    def get_cost(self):
        return self.price + self.component.get_cost()

    def get_description(self):
        return self.component.get_description() + ", " + self.description

class KeciPeyniri(Decorator):
    def __init__(self, component):
        self.component = component
        self.price = 3.0
        self.description = "Keçi Peyniri"

    def get_cost(self):
        return self.price + self.component.get_cost()

    def get_description(self):
        return self.component.get_description() + ", " + self.description

class Et(Decorator):
    def __init__(self, component):
        self.component = component
        self.price = 4.0
        self.description = "Et"

    def get_cost(self):
        return self.price + self.component.get_cost()

    def get_description(self):
        return self.component.get_description() + ", " + self.description

class Sogan(Decorator):
    def __init__(self, component):
        self.component = component
        self.price = 5.0
        self.description = "Soğan"

    def get_cost(self):
        return self.price + self.component.get_cost()

    def get_description(self):
        return self.component.get_description() + ", " + self.description
    
class Misir(Decorator):
    def __init__(self, component):
        self.component = component
        self.price = 6.0
        self.description = "Mısır"

    def get_cost(self):
        return self.price + self.component.get_cost()

    def get_description(self):
        return self.component.get_description() + ", " + self.description




#--------------------------------- DATABASE --------------------------------
class OrdersDatabase:
    
    def __init__(self):
        self.filename = 'Orders_Database.csv'

    def write_to_database(self, customer_id, customer_name, pizza_description, sauce_description, total_cost, card_number, card_security_code):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([customer_id, customer_name, pizza_description, sauce_description, total_cost, card_number, card_security_code, current_time])


def main():
    # Menu'yu ekrana yazdırın
    with open('Menu.txt', 'r') as f:
        menu = f.read()
        print(menu)

    # Kullanıcıdan pizza ve sos seçimlerini alın
    while True:
        try:
            pizza_choice = input('Lütfen pizza seçiminizi yapın (1-4): ')
            if pizza_choice not in ["1", "2", "3", "4"]:
                raise ValueError("Lütfen 1-4 arasında değerler girin.")
            
            sauce_choice = input('Lütfen sos seçiminizi yapın (11-16): ')
            if sauce_choice not in ['11', '12', '13', '14', '15', '16']:
                raise ValueError("Lütfen 11-16 arasında değerler girin")
            break
        except ValueError as error:
            print(error)

    # Pizza ve sos sınıflarını oluşturun
    try:
        pizza = {
            '1': KlasikPizza(),
            '2': MargaritaPizza(),
            '3': TurkPizza(),
            '4': SadePizza()
        }[pizza_choice]
    except KeyError:
        print('Hatalı pizza seçimi!')
        pizza = None

    try:
        sauce = {
            '11': Zeytin(pizza),
            '12': Mantar(pizza),
            '13': KeciPeyniri(pizza),
            '14': Et(pizza),
            '15': Sogan(pizza),
            '16': Misir(pizza)
    }[sauce_choice]
    except KeyError:
        print('Hatalı sos seçimi!')
        sauce = None

    # Toplam tutarı hesaplayın
    total_cost = sauce.get_cost()


    # Kullanıcı bilgilerini alın
    customer_name = input('Lütfen adınızı girin: ')
    customer_id = input('Lütfen TC kimlik numaranızı girin: ')
    card_number = input('Lütfen kredi kartı numaranızı girin: ')
    card_security_code = input('Lütfen kredi kartı güvenlik kodunuzu girin: ')

    # Siparişi veritabanına yazdırın
   

    """with open("siparisler.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(siparis)"""
    orders_database = OrdersDatabase()
    orders_database.write_to_database(customer_id, customer_name, pizza.description, sauce.description, total_cost, card_number, card_security_code)

if __name__ == "__main__":
    main()