from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("name", 2021, 9.8)

    def test_init_movie(self):
        self.assertEqual("name", self.movie.name)
        self.assertEqual(2021, self.movie.year)
        self.assertEqual(9.8, self.movie.rating)
        self.assertListEqual([], self.movie.actors)

    def test_name_property_cannot_be_empty_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""

        self.assertEqual(f"Name cannot be an empty string!", str(ex.exception))

    def test_year_property_is_not_in_correct_range_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1800

        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor_correct_plus_raises(self):
        self.assertListEqual([], self.movie.actors)
        res = self.movie.add_actor("name")
        self.assertListEqual(["name"], self.movie.actors)

        res1 = self.movie.add_actor("name")
        self.assertEqual(f"name is already added in the list of actors!", res1)

    def test_greater_than_between_two(self):
        self.movie2 = Movie("name2", 2020, 9.1)
        expected = '"name" is better than "name2"'
        self.assertEqual(expected, self.movie.__gt__(self.movie2))

    def test_greater_than_second_option(self):
        self.movie2 = Movie("name2", 2020, 9.9)
        expected = '"name2" is better than "name"'
        self.assertEqual(expected, self.movie.__gt__(self.movie2))

    def test_string_representation(self):
        self.assertEqual("name", self.movie.name)
        self.assertEqual(2021, self.movie.year)
        self.assertEqual(9.8, self.movie.rating)
        self.assertListEqual([], self.movie.actors)
        self.movie.add_actor("name")
        self.assertListEqual(["name"], self.movie.actors)
        result = self.movie.__repr__()
        expected = f"Name: name\n" \
               f"Year of Release: 2021\n" \
               f"Rating: 9.80\n" \
               f"Cast: name"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()