from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("name")

    def test_init_correctly(self):
        self.assertEqual("name", self.pet_shop.name)
        self.assertDictEqual({}, self.pet_shop.food)
        self.assertListEqual([], self.pet_shop.pets)

    def test_add_food_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("hrupanki", -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_unregistered_food(self):
        self.pet_shop.add_food("hrupanki", 1)
        self.assertDictEqual({"hrupanki": 1}, self.pet_shop.food)

    def test_add_existing_food_with_given_quantity(self):
        self.pet_shop.add_food("hrupanki",2)
        self.assertDictEqual({"hrupanki": 2}, self.pet_shop.food)
        res = self.pet_shop.add_food("hrupanki", 2)
        self.assertDictEqual({"hrupanki": 4}, self.pet_shop.food)
        self.assertEqual("Successfully added 2.00 grams of hrupanki.", res)

    def test_add_pet(self):
        self.assertListEqual([], self.pet_shop.pets)
        res = self.pet_shop.add_pet("Tropcho")
        self.assertEqual("Successfully added Tropcho.", res)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Tropcho")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_unexisting_name_raises(self):
        self.assertListEqual([], self.pet_shop.pets)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("hrupanki", "Tropcho")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_with_unavailable_food_raises(self):
        self.assertDictEqual({}, self.pet_shop.food)
        self.pet_shop.add_pet("Tropcho")
        self.assertListEqual(["Tropcho"], self.pet_shop.pets)
        res = self.pet_shop.feed_pet("hrupanki", "Tropcho")
        self.assertEqual('You do not have hrupanki', res)

    def test_feed_pet_food_under_100(self):
        self.pet_shop.pets = ["name"]
        self.pet_shop.food = {"food": 99}
        result = self.pet_shop.feed_pet("food", "name")
        self.assertDictEqual({"food": 1099.00}, self.pet_shop.food)
        self.assertEqual(f"Adding food...", result)

    def test_feed_pet_success(self):
        self.pet_shop.pets = ["name"]
        self.pet_shop.food = {"food": 100}
        result = self.pet_shop.feed_pet("food", "name")
        self.assertDictEqual({"food": 0}, self.pet_shop.food)
        self.assertEqual(f"name was successfully fed", result)

    def test_repr_pet_shop(self):
        self.pet_shop.pets = ["pet", "pet1", "pet2"]
        result = self.pet_shop.__repr__()
        expected = f'Shop name:\n' \
                   f'Pets: pet, pet1, pet2'
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()