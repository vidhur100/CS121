'''
CS 115, Lab 12, Inheritance

Author: Vidhur Busannagari
Pledge: I pledge my honor that I have abided by the Stevens Honor System - VB
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 1 
' Implement missing sections of the Car class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Car(object):
    
    def __init__(self, make, model, mpg, tank_capacity):
        """
        Constructor for Car
        """
        self.__make = make
        self.__model = model
        self.__mpg = mpg
        self.__tank_capacity = tank_capacity

    def get_make(self):
        """
        Returns the make of car
        """
        return self.__make

    def get_model(self):
        """
        Returns the model of car
        """
        return self.__model
    
    def get_mpg(self):
        """
        Returns the mpg of car
        """
        return self.__mpg

    def get_tank_capacity(self):
        """
        Returns the tank capacity of car
        """
        return self.__tank_capacity

    def set_mpg(self, mpg):
        """
        Sets the MPG for car
        """
        self.__mpg = mpg
    
    def set_tank_capacity(self, tank_capacity):
        """
        Sets the tank capacity for car
        """
        self.__tank_capacity = tank_capacity

    def get_total_range(self):
        """
        Returns the distance a fully filled car can travel
        """
        return self.__mpg * self.__tank_capacity


    def __str__(self):
        '''A string for printing information about a car.'''
        return self.__make + ' ' + self.__model + ', MPG: ' + str(self.__mpg) \
            + ', tank capacity: ' + str(self.__tank_capacity)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 2 
' Implement missing sections of the HybridCar class. 
' Make HybridCar be a subclass of Car.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class HybridCar(Car):  

    def __init__(self, make, model, mpg, tank_capacity, battery_kWh, miles_per_kWh):
        """
        Constructor of HybridCar
        """
        super().__init__(make, model, mpg, tank_capacity)
        self.__battery_kWh = battery_kWh
        self.__miles_per_kWh = miles_per_kWh

    def get_battery_range(self):
        '''
        Returns distance a fully charged car can drive
        '''
        return self.__battery_kWh * self.__miles_per_kWh

    def get_total_range(self):
        '''
        returns the full range of the car
        '''
        return super().get_total_range() + self.get_battery_range()

    def __str__(self):
        '''A string for printing information about a car.'''
        return super().__str__() + ', battery kWh: ' + \
            str(self.__battery_kWh) + ', miles/kWh: ' + \
            str(self.__miles_per_kWh)
