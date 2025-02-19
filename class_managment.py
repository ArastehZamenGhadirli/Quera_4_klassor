class Teacher:
    """this the class of teacher that only get the name parameter """

    def __init__(self, name: str):
        self._name = name
        
    def get_name(self) -> str:
        """this for getting name value 
        """
        return self._name
        
    def set_name(self, name):
        """setting name value to the object 
        """
        self._name = name


class Student:
    def __init__(self, name: str):
        """intiliaze the name in Student class and a list for saving gardes of the student 

        Args:
            name (str): _description_
        """
        self.gardes = []
        self._name = name

    def get_name(self) -> str:
        """get the name of the Student

        Returns:
            str: _description_
        """
        return self._name

    def set_name(self, new_name) -> None:
        """sets new name for Student 

        Args:
            new_name (_type_): _description_
        """
        self._name = new_name

    def add_score(self, grade):
        """this method is for adding garde to the list of grade for one student 

        Args:
            grade (_type_): _description_
        """
        self.gardes.append(grade)

    def avg_score(self):
        """calculate the avrage score for each student 
        """
        while len(self.gardes) > 0:
            return sum(self.gardes) / len(self.gardes)
        


class Course:
    def __init__(self, teacher):
        """this class specify the teacher of that course and the list of hi student 

        Args:
            teacher (_type_): _description_
        """
        self.studentlist = []
        self._teacher = teacher

    def change_teacher(self, new_teacher):
        """whenever we want to change the name of the teacher we should call this method 

        Args:
            new_teacher (_type_): _description_
        """
        self._teacher = new_teacher

    def add_student(self, student):
        """add the new student to the list of student

        """
        self.studentlist.append(student)

    def grade_student(self):
        """get the score of each student by input and add them to the grades
        """
        for student in self.studentlist:
            grade = float(input(f"Enter a score for {student.get_name()} :"))
            student.add_score(grade)

    def list_garde_student(self):
        """show the list of student with the average but it is not sorted 
        """
        print("student list:")
        for student in self.studentlist:
            print(f"Name : {student.get_name()} , Avrage Score :{student.avg_score()}")



professor = Teacher("Dr. Ali")
student1 = Student("Sara")
student2 = Student("mohammad")
student3 = Student("Ali")
course = Course(professor)
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)
course.grade_student()
course.list_garde_student()
