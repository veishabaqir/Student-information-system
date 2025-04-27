import datetime

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.attendance = []

    def mark_attendance(self, date=None):
        if date is None:
            date = datetime.date.today()
        self.attendance.append(date)

    def get_attendance_report(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "attendance": self.attendance
        }

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id in self.students:
            print(f"Student ID {student_id} already exists.")
        else:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} added successfully.")

    def mark_attendance(self, student_id, date=None):
        if student_id in self.students:
            self.students[student_id].mark_attendance(date)
            print(f"Attendance marked for student ID {student_id}.")
        else:
            print(f"Student ID {student_id} not found.")

    def generate_report(self):
        report = []
        for student in self.students.values():
            report.append(student.get_attendance_report())
        return report

# Example usage
if __name__ == "__main__":
    system = StudentManagementSystem()
    system.add_student(1, "Alice")
    system.add_student(2, "Bob")
    
    system.mark_attendance(1)
    system.mark_attendance(2, datetime.date(2023, 10, 1))
    
    report = system.generate_report()
    for student_report in report:
        print(student_report)