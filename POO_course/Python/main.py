from lib2to3.pgen2 import driver
from car import Car
from account import Account
from uberX import UberX
from card import Card
from user import User
from driver import Driver

def main():
    print('Hola mundo')
    # car = Car("AMS234", Account("Luka Modric", "415634"))
    # print(vars(car))
    # print(vars(car.driver))
    # print(car.driver.name)

    # uberx = UberX("AMS234", Account("Luisillo el Gordillo", "LLS870"), "BMW", "A50")
    # print(vars(uberx))

    # card_1 = Card(12345, "745700", "345", "12-05-2025")
    # print(vars(card_1))

    user_1 = User("Luis", "367799", "luisillo@soto.com", "klSuzuki12")
    print(vars(user_1))

    driver_1 = Driver("Zu Kulento", "233478", "zuku@lento.com", "jegLikerKaffeMedMelk11")
    print(vars(driver_1))


if __name__ == '__main__':
    main()


# OUTPUT:

# Hola mundo
# {'license': 'AMS234', 'driver': <account.Account object at 0x7fbeff9545b0>}
# {'name': 'Luka Modric', 'document': '415634'}
# Luka Modric


# ***NOTAS***

# Método constructor:

# Da un estado inicial al objeto
# Tiene el mismo nombre de la clase
# son los parámetros mínimos que necesita el objeto para 'poder vivir'