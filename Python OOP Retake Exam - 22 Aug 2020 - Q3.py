from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.card = StudentReportCard("Ivan", 8)

    def test_init_correctly(self):
        self.assertEqual("Ivan", self.card.student_name)
        self.assertEqual(8, self.card.school_year)
        self.assertDictEqual({}, self.card.grades_by_subject)

    def test_student_name_cannot_be_empty_string_assert(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("", 8)
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_school_year_range_is_not_correct_assert(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("Ivan", 15)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_add_grade(self):
        self.assertDictEqual({}, self.card.grades_by_subject)
        self.card.add_grade("Maths", 6)
        self.assertDictEqual({"Maths": [6]}, self.card.grades_by_subject)
        self.card.add_grade("Maths", 5)
        self.assertDictEqual({"Maths": [6, 5]}, self.card.grades_by_subject)

    def test_average_grade_by_subject_report(self):
        self.assertDictEqual({}, self.card.grades_by_subject)
        self.card.add_grade("Test", 6)
        self.card.add_grade("Test", 5)
        result = self.card.average_grade_by_subject()
        self.assertEqual("Test: 5.50", result)

    def test_average_grade_for_all_subjects_report(self):
        self.card.add_grade("Test", 6)
        self.card.add_grade("Test1", 5)
        result = self.card.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 5.50", result)

    def test_report_card_representation(self):
        self.card.add_grade("Test", 6)
        self.card.add_grade("Test", 6)
        self.card.add_grade("Test1", 4)
        self.card.add_grade("Test1", 4)
        expected = f"Name: Ivan\n" \
                   f"Year: 8\n" \
                   f"----------\n" \
                   f"{self.card.average_grade_by_subject()}\n" \
                   f"----------\n" \
                   f"{self.card.average_grade_for_all_subjects()}"
        self.assertEqual(expected, self.card.__repr__())


if __name__ == "__main__":
    main
