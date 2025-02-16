from __future__ import annotations


class Student:
    """
    A class to represent a student with a name and grade.
    """

    def __init__(self, name: str, grade: int):
        """
        Initializes a Student object.

        Parameters:
        name (str): The name of the student.
        grade (int): The grade of the student.
        """
        self.name: str = name
        self.grade: int = grade

    def compare_grade(self, other_student: Student):
        """
        Compares the grades of two students and prints the name of the student with the higher grade.

        Parameters:
        other_student (Student): The student to compare with.
        """
        if self.grade > other_student.grade:
            print(f"{self.name} has a higher grade.")
        elif other_student.grade > self.grade:
            print(f"{other_student.name} has a higher grade.")
        else:
            print(f"Both students have the same grade")


s1 = Student("Alice", 90)
s2 = Student("Bob", 85)
s1.compare_grade(s2)  # Alice has a higher grade.

s3 = Student("Charlie", 90)
s1.compare_grade(s3)  # Both students have the same grade.
