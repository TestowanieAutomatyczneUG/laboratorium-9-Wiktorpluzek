import unittest
from unittest.mock import *


class Car:

    def needsFuel(self):
        pass

    def getEngineTemperature(self):
        pass

    def driveTo(self, destination):
        pass


class CarImpl:

    def __init__(self, car: Car):
        self.car = car

    def mockNeedsFuel(self):
        if self.car.needsFuel():
            return "Low fuel"
        return "No refill needed"

    def mockGetEngineTemperature(self):
        if self.car.getEngineTemperature():
            return str(self.car.getEngineTemperature())
        return "Cannot get temperature"

    def mockDriveTo(self, destination):
        if self.car.driveTo(destination):
            return "destination: " + str(destination)
        return "No destination"

class mockTest(unittest.TestCase):

    def test_fuel(self):
        car = Car
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = False
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.mockNeedsFuel(), "No refill needed")

    def test_no_fuel(self):
        car = Car
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = True
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.mockNeedsFuel(), "Low fuel")

    def test_engine_temp(self):
        car = Car
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = 60
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.mockGetEngineTemperature(), "60")

    def test_engine_no_temp(self):
        car = Car
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = None
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.mockGetEngineTemperature(), "Cannot get temperature")

    def test_destination(self):
        car = Car
        car.driveTo = Mock(name='driveTo')
        car.driveTo.return_value = "Warszawa"
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.mockDriveTo("Warszawa"), "destination: Warszawa")

    def test_no_destination(self):
        car = Car
        car.driveTo = Mock(name='driveTo')
        car.driveTo.return_value = None
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.mockDriveTo(None), "No destination")
