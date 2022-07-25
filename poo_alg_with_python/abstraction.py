
class WashingMachine:
    
    def __init__(self):
        pass

    def wash(self, stat_temperature = 'hot'):
        self._fill_tank(stat_temperature)
        self._add_soap()
        self._wash()
        self._centrifuge()

    def _fill_tank(self, stat_temperature):
        print(f'Filling the tank with {stat_temperature} water')

    def _add_soap(self):
        print('Adding soap')

    def _wash(self):
        print('Washing clothes')

    def _centrifuge(self):
        print('Centrifuging clothes')


if __name__ == '__main__':
    washing_mach_1 = WashingMachine()
    washing_mach_1.wash()