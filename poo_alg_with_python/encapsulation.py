class PollingStation:

    def __init__(self, id, country):
        self.__id = id
        self.__country = country
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__country:
            self.__region = region
        else:
            raise ValueError(f'The region {region} is not valid in {self.__country}')


def main():
    
    station_1 = PollingStation(321, ['Cali', 'Bogota', 'Medellin', 'Barranquilla', 'Cartagena', 'Bucaramaga', 'Cartagena', 'Popayan', 'Pereira', 'Tulua', 'Palmira'])

    print(station_1.region) # --> None
    
    station_1.region = 'Cali'

    print(station_1.region) # --> Cali

    station_1.region = 'Lima'

    print(station_1.region) 

# -->Traceback (most recent call last):
#   File "/home/juansoto23/personalProjects/firstFiles/poo_alg_with_python/encapsulation.py", line 36, in <module>
#     main()
#   File "/home/juansoto23/personalProjects/firstFiles/poo_alg_with_python/encapsulation.py", line 30, in main
#     station_1.region = 'Lima'
#   File "/home/juansoto23/personalProjects/firstFiles/poo_alg_with_python/encapsulation.py", line 17, in region
#     raise ValueError(f'The region {region} is not valid in {self.__country}')
# ValueError: The region Lima is not valid in ['Cali', 'Bogota', 'Medellin', 'Barranquilla', 'Cartagena', 'Bucaramaga', 'Cartagena', 'Popayan', 'Pereira', 'Tulua', 'Palmira'] 


if __name__ == '__main__':
    main()