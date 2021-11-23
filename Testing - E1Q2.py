from typing import ClassVar


class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: ClassVar[float] = 1.25
    fuel_consumption: float
    fuel: float
    capacity: float
    horse_power: float

    def __init__(self, fuel: float, horse_power: float):
        self.fuel = fuel
        self.capacity = self.fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        fuel_needed = self.fuel_consumption * kilometers
        if self.fuel < fuel_needed:
            raise Exception("Not enough fuel")
        self.fuel -= fuel_needed

    def refuel(self, fuel):
        if self.fuel + fuel > self.capacity:
            raise Exception("Too much fuel")
        self.fuel += fuel

    def __str__(self):
        return f"The vehicle has {self.horse_power} " \
               f"horse power with {self.fuel} fuel left and {self.fuel_consumption} fuel consumption"

****************************************************************************************************

import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    DEFAULT_FC = 1.25

    def setUp(self):
        self.v = Vehicle(80, 161)

    def test_init(self):
        fuel = 80
        hp = 161
        default_fc = 1.25
        vehicle = Vehicle(fuel, hp)
        self.assertEqual(vehicle.fuel, fuel)
        self.assertEqual(vehicle.capacity, fuel)
        self.assertEqual(vehicle.horse_power, hp)
        self.assertEqual(vehicle.fuel_consumption, default_fc)

    def test_drive(self):
        km = 20
        remaining_fuel = 55
        self.v.drive(km)
        self.assertEqual(self.v.fuel, remaining_fuel)

    def test_drive_exception_raise(self):
        km = 100
        with self.assertRaises(Exception) as e:
            self.v.drive(km)
        self.assertEqual("Not enough fuel", str(e.exception))

    def test_refuel(self):
        self.v.fuel -= 20
        self.v.refuel(10)
        self.assertEqual(self.v.fuel, 70)

    def test_refuel_exception(self):
        with self.assertRaises(Exception) as e:
            self.v.refuel(5)
        self.assertEqual("Too much fuel", str(e.exception))

    def test_str(self):
        self.assertEqual(f"The vehicle has {self.v.horse_power} horse power with {self.v.fuel} fuel left and {self.v.fuel_consumption} fuel consumption", str(self.v))

