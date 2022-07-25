class Automovil:

    def __init__(self, model, branch, color):
        self.model = model
        self.branch = branch
        self.color = color
        self._status = 'en_reposo'
        self._motor = Motor(cylinders=4)

    def accelerate(self, type = 'despacio'):
        if type == 'rapida':
            self._motor.inject_gasoline(10)
        else:
            self._motor.inject_gasoline(3)
        
        self._status = 'en_movimiento'


class Motor:

    def __init__(self, cylinders, type='gasoline'):
        self.cylinders = cylinders
        self.type = type
        self._temperature = 0

    def inject_gasoline(self, quantity):
        pass


auto_1 = Automovil('SV2', 'Soto', 'blue')
print(auto_1.branch)
print(auto_1._status)