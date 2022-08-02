
class Person:

    def __init__(self, name):
        self.name = name

    def move(self):
        print(f'{self.name} is walking')


class Cyclist(Person):
    
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print(f'{self.name} is moving by bicycle')


def run():

    person_1 = Person('Juan')
    person_1.move() # --> Juan is walking

    cyclist_1 = Cyclist('Kate')
    cyclist_1.move() # --> Kate is moving by bicycle


if __name__ == '__main__':
    run()