class Student:
    def __init__(self, name: str, courses=None):
        if courses is None:
            courses = {}
        self.name = name
        self.courses = courses  # {course_name: [notes]}

    def enroll(self, course_name: str, notes, add_course_notes: str = ""):
        if course_name in self.courses.keys():
            [self.courses[course_name].append(x) for x in notes]
            return "Course already added. Notes have been updated."

        if add_course_notes == "Y" or add_course_notes == "":
            self.courses[course_name] = notes
            return "Course and course notes have been added."

        self.courses[course_name] = []
        return "Course has been added."

    def add_notes(self, course_name, notes):
        if course_name in self.courses.keys():
            self.courses[course_name].append(notes)
            return "Notes have been updated"
        raise Exception("Cannot add notes. Course not found.")

    def leave_course(self, course_name):
        if course_name in self.courses.keys():
            self.courses.pop(course_name)
            return "Course has been removed"
        raise Exception("Cannot remove course. Course not found.")

*******************************************************************************

from project.student import Student

import unittest


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.s = Student("Harry")

    def test_init(self):
        s = Student("Harry")
        self.assertEqual(s.name, "Harry")
        self.assertEqual(s.courses, {})

    def test_init_with_course(self):
        s = Student("Harry", {"Python": ["note 1"]})
        self.assertEqual(s.name, "Harry")
        self.assertEqual(s.courses, {"Python": ["note 1"]})

    def test_init_with_none_course(self):
        s = Student("Harry", None)
        self.assertEqual(s.name, "Harry")
        self.assertEqual(s.courses, {})

    def test_enroll_duplicate_course(self):
        self.s.courses = {"Python": ["note1"]}
        res = self.s.enroll("Python", ["note2"])
        self.assertEqual("Course already added. Notes have been updated.", res)
        self.assertEqual(["note1", "note2"], self.s.courses["Python"])

    def test_enroll_new_course_with_notes(self):
        res = self.s.enroll("Python", ["note1"])
        self.assertEqual(res, "Course and course notes have been added.")
        self.assertEqual(self.s.courses["Python"], ["note1"])

    def test_enroll_new_course_without_notes(self):
        res = self.s.enroll("Python", ["note1"], "no")
        self.assertEqual(res, "Course has been added.")
        self.assertEqual(self.s.courses["Python"], [])

    def test_enroll_new_course_with_adding_notes(self):
        res = self.s.enroll("Python", ["note1", "note2"], "Y")
        self.assertEqual(res, "Course and course notes have been added.")
        self.assertEqual(self.s.courses["Python"], ["note1", "note2"])

    def test_enroll_in_existing_course_with_adding_notes(self):
        self.s.enroll("Python", ["note1", "note2"], "Y")
        res = self.s.enroll("Python", ["note3"], "Y")
        self.assertEqual(res, "Course already added. Notes have been updated.")
        self.assertEqual(self.s.courses["Python"], ["note1", "note2", "note3"])

    def test_add_notes(self):
        self.s.courses = {"Python": []}
        res = self.s.add_notes("Python", "note1")
        self.assertEqual("Notes have been updated", res)
        self.assertEqual(["note1"], self.s.courses["Python"])

    def test_add_notes_exception(self):
        with self.assertRaises(Exception) as e:
            self.s.add_notes("Java", "note_fail")
        self.assertEqual(str(e.exception), "Cannot add notes. Course not found.")
        self.assertEqual(self.s.courses, {})

    def test_leave_course(self):
        self.s.courses = {"Python": []}
        res = self.s.leave_course("Python")
        self.assertEqual(res, "Course has been removed")
        self.assertEqual(self.s.courses, {})

    def test_leave_course_exception(self):
        with self.assertRaises(Exception) as e:
            self.s.leave_course("Java")
        self.assertEqual(str(e.exception), "Cannot remove course. Course not found.")
