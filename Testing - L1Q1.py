class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

**************************************************************
import unittest

class WorkerTests(unittest.TestCase):
    def test_person_is_initialised_correctly(self):
        #Arrange and Act
        worker = Worker("Test", 100, 10)
        #Assert
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_energy_increased_after_rest(self):
        #Arrange
        worker = Worker("Test", 100, 10)
        self.assertEqual(10, worker.energy)
        #Act
        worker.rest()
        #Assert
        self.assertEqual(11, worker.energy)

    def test_person_works_with_negative_energy_raises(self):
        # Arrange
        worker = Worker("Test", 100, 0)
        #Act
        with self.assertRaises(Exception) as ex:
           worker.work()
        #Assert
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_money_is_increased_after_work(self):
        #Arrange
        worker = Worker("Test", 100, 10)
        self.assertEqual(10, worker.energy)
        #Act
        worker.work()
        #Assert
        self.assertEqual(100, worker.money)

    def test_worker_energy_decreased_after_work(self):
        # Arrange
        worker = Worker("Test", 100, 10)
        self.assertEqual(10, worker.energy)
        # Act
        worker.work()
        # Assert
        self.assertEqual(9, worker.energy)

    def test_get_info(self):
        # Arrange
        worker = Worker("Test", 100, 10)
        # Act
        actual_result = worker.get_info()
        expected_result = "Test has saved 0 money."
        #Assert
        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()