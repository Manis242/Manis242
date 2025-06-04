from django.test import TestCase
from .models import Student, Teacher, Course
from datetime import date

class ModelCreationTests(TestCase):

    def test_create_student(self):
        student = Student.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            date_of_birth=date(2005, 1, 1)
        )
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(str(student), "John Doe")

    def test_create_teacher(self):
        teacher = Teacher.objects.create(
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@example.com"
        )
        self.assertEqual(Teacher.objects.count(), 1)
        self.assertEqual(str(teacher), "Jane Smith")

    def test_create_course(self):
        teacher = Teacher.objects.create(
            first_name="Richard",
            last_name="Roe",
            email="richard.roe@example.com"
        )
        course = Course.objects.create(
            title="Introduction to Programming",
            code="CS101",
            teacher=teacher
        )
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(str(course), "Introduction to Programming")
        self.assertEqual(course.teacher.first_name, "Richard")

    def test_course_students_relationship(self):
        student1 = Student.objects.create(
            first_name="Alice",
            last_name="Wonderland",
            email="alice@example.com",
            date_of_birth=date(2006, 5, 10)
        )
        student2 = Student.objects.create(
            first_name="Bob",
            last_name="Builder",
            email="bob@example.com",
            date_of_birth=date(2004, 8, 15)
        )
        course = Course.objects.create(
            title="Advanced Mathematics",
            code="MATH202"
        )
        course.students.add(student1)
        course.students.add(student2)

        self.assertEqual(course.students.count(), 2)
        self.assertIn(student1, course.students.all())
        self.assertIn(student2, course.students.all())
